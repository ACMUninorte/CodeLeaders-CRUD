from django.test import TestCase

from authentication.helpers import get_or_create_user
from authentication.models import User
from core.tests.assertions import InstanceAssertionsMixin

test_data_1 = {
    "username": "pedcasa",
    "email": "pedroski@uninorte.edu.co",
    "first_name": "Pedro",
    "last_name": "Capasto",
    "career": "Ing sistemas",
    "student_code": "3222222",
}

user1_data = {
    "username": "user1",
    "email": "u1@example.com",
}


class TestManualRegisterSerializer(TestCase, InstanceAssertionsMixin):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(**user1_data)

    def test_create_user(self):

        user = get_or_create_user(test_data_1)
        self.assert_instance_exists(User, username=test_data_1["username"])

        # test profile
        self.assertEqual(user.profile.career, test_data_1["career"])
        self.assertEqual(user.profile.student_code, test_data_1["student_code"])

    def test_create_without_profile_data(self):

        test_data = test_data_1.copy()

        test_data.pop("career")
        test_data.pop("student_code")

        user = get_or_create_user(test_data)
        self.assert_instance_exists(User, username=test_data["username"])

        self.assertEqual(user.profile.career, "")
        self.assertEqual(user.profile.student_code, "")

    def test_get_user(self):

        # before "creating" the user, the total of users is 1
        self.assertEqual(User.objects.all().count(), 1)
        user = get_or_create_user(user1_data)
        self.assertEqual(user.pk, self.user1.pk)
        # after "creating" the user, is still 1, that means it was retrieve it
        self.assertEqual(User.objects.all().count(), 1)
