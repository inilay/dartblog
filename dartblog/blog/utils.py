from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    use_https = False
    context = {
        "domain": current_site.domain,
        "user": user,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        "token": default_token_generator.make_token(user),
        "protocol": "https" if use_https else "http"
    }
    message = render_to_string('registration/verify_email.html', context=context)
    # email = EmailMessage(
    #     'Verify email',
    #     message,
    #     'pillaw@mail.ru',
    #     to=[user.email],
    #     fail_silently=False
    # )
    # email.send()
    send_mail( 'Verify email',
        message,
        'pillaw@mail.ru',
        [user.email],
        fail_silently=False)

