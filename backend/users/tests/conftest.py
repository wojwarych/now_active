import pytest
from model_mommy import mommy

from users.models import User


@pytest.fixture
def student_user_model():
    return mommy.make(
        User,
        is_trainer=False,
        is_student=True,
        phone_number=123456789
    )
