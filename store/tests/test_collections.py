from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection




@pytest.mark.django_db
class TestCreateCollection:
    #@pytest.mark.skip(reason="Not implemented yet")
    def test_if_user_is_anonymous_returns_401(self, api_client):
        #AAA (Arrange, Act, Assert)
        #Arrange 
        api_client.logout() #ensures the client is logged out

        #Act
        #client = APIClient() #creates an instance of the APIClient
        response = api_client.post('/store/collections/', {'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED #asserts that the response status code is 401 (unauthorized)

    def test_if_user_is_not_admin_returns_403(self, api_client):
        #AAA (Arrange, Act, Assert)
        #Arrange 

        #Act
        #client = APIClient() #creates an instance of the APIClient
        api_client.force_authenticate(user = {}) #authenticates the client as a non-admin user
        response = api_client.post('/store/collections/', {'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN #asserts that the response status code is 403 (forbidden)

    def test_if_data_is_invalid_returns_400(self, api_client):
        #AAA (Arrange, Act, Assert)
        #Arrange 

        #Act
        #client = APIClient() #creates an instance of the APIClient
        user = User(is_staff = True) #creates a user instance and sets is_staff to true
        api_client.force_authenticate(user = user) #authenticates the client as a non-admin
        response = api_client.post('/store/collections/', {'title': ''}) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST #asserts that the response status code is 400 (bad request)
        assert response.data['title'] is not None #asserts that the response data contains an error message for the title field

    def test_if_data_is_valid_returns_201(self, api_client):
        #AAA (Arrange, Act, Assert)
        #Arrange 

        #Act
        #client = APIClient() #creates an instance of the APIClient
        user = User(is_staff = True) #creates a user instance and sets is_staff to true
        api_client.force_authenticate(user = user) #authenticates the client as a non-admin
        response = api_client.post('/store/collections/', {'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_201_CREATED #asserts that the response status code is 201 (created)
        assert response.data['id'] > 0 #asserts that the response data contains a valid id for the created collection

# Note: Ensure that the 'api_client' fixture is defined in conftest.py or the same test file.
# The fixture should return an instance of APIClient.

#the second repetition is api_client.post('/store/collections/', {'title': 'a'})