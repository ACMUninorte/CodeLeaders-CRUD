from authentication.emails import WelcomeEmail
from authentication.models import User


def get_or_create_user(data):

    data = data.copy()

    username = data.pop("username")

    profile_data = {}
    profile_fields = ["student_code", "career", "first_name", "last_name"]

    for profile_field in profile_fields:
        if profile_field in data:
            profile_data[profile_field] = data.pop(profile_field)

    user, created = User.objects.get_or_create(username=username, defaults=data)

    if created:
        # Before adding signals Profile.objects.create(user=user, **profile_data)
        user_profile = user.profile
        for k, v in profile_data.items():
            setattr(user_profile, k, v)
        user_profile.save()

        # add random password, may be ignored by using
        # UNUSABLE PASSWORD of django internals
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=["password"])

    return user


def send_welcome_email(user):
    WelcomeEmail(context={"user": user}).send([user.email])
