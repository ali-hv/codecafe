import logging
from django.shortcuts import render, get_object_or_404, redirect
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from django.urls import reverse

from courses.views import register_items, delete_failed_temporary_order
from cart.models import UserCart, TemporaryOrder


def go_to_gateway_view(request):
    user_cart = get_object_or_404(UserCart, user=request.user)
    amount = user_cart.get_payable_amount() * 10  # convert the amount from RIAL to TOMAN

    user_mobile_number = '+989112221234'

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url('/callback-gateway/')
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        bank_record = bank.ready()

        temp_order = TemporaryOrder.objects.create(user=request.user,
                                                   tracking_code=bank_record.tracking_code)
        temp_order.courses.set(user_cart.courses.all())
        temp_order.save()

        # هدایت کاربر به درگاه بانک
        context = bank.get_gateway()
        return render(request, 'payment/redirect_to_bank.html', context=context)
    except AZBankGatewaysException as e:
        logging.critical(e)
        return render(request, 'payment/redirect_to_bank.html')


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        register_items(request, tracking_code)
        return redirect('users:user_courses')

    delete_failed_temporary_order(tracking_code)

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")