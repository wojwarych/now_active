import pytest

pytestmark = pytest.mark.django_db


def test_manager_home_view(client, django_user_model):
    username = "test_user"
    password = "pass123"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.parametrize(
    'url',
    [
        ('/'),
        ('/manager/students'),
        ('/manager/trainers'),
        ('/manager/groups'),
    ],
)
def test_manager_not_logged_user_redirected(url, client):
    response = client.get(url)
    assert response.status_code == 302


def test_manager_non_existent_url_bad_request(client, django_user_model):
    username = "test_user"
    password = "pass123"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/manager/non-existent-url')
    assert response.status_code == 404


def test_manager_students_view(client, django_user_model):
    username = "test_user"
    password = "pass123"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/manager/students')
    assert response.status_code == 200


def test_manager_trainers_list_view(client, django_user_model):
    username = "test_user"
    password = "pass123"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/manager/trainers')
    assert response.status_code == 200


def test_manager_groups_list_view(client, django_user_model):
    username = "test_user"
    password = "pass123"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/manager/groups')
    assert response.status_code == 200


def test_create_student_form_view(client, django_user_model):
    username = "test_user"
    password = "pass123"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.post(
        '/manager/student-add',
        dict(username='example@tst.com', phone_number='123456789')
    )
    assert response.status_code == 302
    assert response.url == '/manager/'
