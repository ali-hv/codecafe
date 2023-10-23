from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
from payment.views import go_to_gateway_view, callback_gateway_view
import os

if 'ADMIN_PANEL_URL' in os.environ:
    admin_panel_url = os.environ['ADMIN_PANEL_URL']
else:
    admin_panel_url = 'admin/'

urlpatterns = [
    path(admin_panel_url, admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('courses/', include('courses.urls')),
    path('user/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('callback-gateway/', callback_gateway_view),
    path('go-to-gateway/', go_to_gateway_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
