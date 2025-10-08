import pytest 

@pytest.fixture
def api_client():
    """Fixture to provide an instance of APIClient for tests."""
    from rest_framework.test import APIClient
    return APIClient()
