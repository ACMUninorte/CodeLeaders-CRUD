from authentication.models import Profile, User


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

        Profile.objects.create(user=user, **profile_data)

        # add random password, may be ignored by using
        # UNUSABLE PASSWORD of django internals

        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=["password"])

    return user


#
