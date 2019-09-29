from django.db.utils import DataError

import pytest

from users.models import User

pytestmark = pytest.mark.django_db


def test_student_is_correctly_saved(student_user_model):
    student = User.objects.get(pk=student_user_model.id)
    assert student.is_student is True
    assert student.is_staff is False
    assert len(student.phone_number) <= 9
    assert student.phone_number == '123456789'


def test_student_throws_error_over_9_nums_in_phone_num():
    with pytest.raises(DataError):
        student = User(phone_number='1234567890')
        student.save()
