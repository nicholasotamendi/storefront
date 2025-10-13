import pytest

from core.models import User 

@pytest.fixture
def api_client():
    """Fixture to provide an instance of APIClient for tests."""
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        user = User(is_staff=is_staff)
        return api_client.force_authenticate(user=user)
    return do_authenticate


@pytest.fixture
def create_user():
    def do_create_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return do_create_user


