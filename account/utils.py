from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    activation_url = f'http://localhost:8000/v1/api/account/activate{activation_code}'
    message = f'Please activate your account here: {activation_url}'
    send_mail('Activate your account', message, 'kuiruk_mai@forum.com', [email, ], fail_silently=False)

