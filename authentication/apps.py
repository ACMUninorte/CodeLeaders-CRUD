from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = "authentication"

    def ready(self) -> None:
        from authentication import signals

        return super().ready()
