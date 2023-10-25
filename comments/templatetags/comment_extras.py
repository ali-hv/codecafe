from django.template.defaulttags import register


@register.filter
def is_accepted(reply):
    return reply.filter(accepted=True)
