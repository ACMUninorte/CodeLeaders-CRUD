from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from djoser import email, utils
from templated_mail.mail import BaseEmailMessage


class PassResetEmail(email.PasswordResetEmail):
    template_name = "email/reset.html"


class WelcomeEmail(BaseEmailMessage):
    template_name = "email/welcome.html"

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.WELCOME_URL.format(**context)
        return context
