from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.contrib.auth.models import User
from store.models import Collection, Product
from model_bakery import baker

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection





@pytest.mark.django_db
class TestCreateCollection:
    #@pytest.mark.skip(reason="Not implemented yet")
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        #AAA (Arrange, Act, Assert)
        #Arrange
        response = create_collection({'title': 'a'})  # makes a post request to the collections endpoint with title as data. Title is the colection title
        # api_client.logout() #ensures the client is logged out

        #Act
        #client = APIClient() #creates an instance of the APIClient
        #response = api_client.post('/store/collections/', ) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED #asserts that the response status code is 401 (unauthorized)

    def test_if_user_is_not_admin_returns_403(self, authenticate, api_client, create_collection):
        #AAA (Arrange, Act, Assert)
        #Arrange 
        authenticate() #authenticates the client as a non-admin user

        #Act
        response = create_collection({'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title
        #client = APIClient() #creates an instance of the APIClient
        #api_client.force_authenticate(user = {}) #authenticates the client as a non-admin user
        # #response = api_client.post('/store/collections/', {'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title
        
        #Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN #asserts that the response status code is 403 (forbidden)

    def test_if_data_is_invalid_returns_400(self, api_client, create_collection):
        #AAA (Arrange, Act, Assert)
        #Arrange 

        #Act
        #client = APIClient() #creates an instance of the APIClient
        user = User(is_staff = True) #creates a user instance and sets is_staff to true
        api_client.force_authenticate(user = user) #authenticates the client as a non-admin
        #response = api_client.post('/store/collections/', {'title': ''}) #makes a post request to the collections endpoint with title as data. Title is the colection title
        response = create_collection({'title': ''}) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST #asserts that the response status code is 400 (bad request)
        assert response.data['title'] is not None #asserts that the response data contains an error message for the title field

    def test_if_data_is_valid_returns_201(self, api_client, create_collection):
        #AAA (Arrange, Act, Assert)
        #Arrange 

        #Act
        #client = APIClient() #creates an instance of the APIClient
        user = User(is_staff = True) #creates a user instance and sets is_staff to true
        api_client.force_authenticate(user = user) #authenticates the client as a non-admin
        #response = api_client.post('/store/collections/', {'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title
        response = create_collection({'title': 'a'}) #makes a post request to the collections endpoint with title as data. Title is the colection title

        #Assert
        assert response.status_code == status.HTTP_201_CREATED #asserts that the response status code is 201 (created)
        assert response.data['id'] > 0 #asserts that the response data contains a valid id for the created collection


# Note: Ensure that the 'api_client' fixture is defined in conftest.py or the same test file.
# The fixture should return an instance of APIClient.

#the second repetition is api_client.post('/store/collections/', {'title': 'a'})

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client, create_user):
        # Arrange
        collection = baker.make(Collection) #creates a collection instance using model bakery and takes care of relationships for us 
        #baker.make(Product, _quantity=5, collection=collection) #creates 5 product instances and associates them with the collection instance created above
        #Act
        response = api_client.get(f'/store/collections/{collection.id}/') #makes a get request to the collections endpoint with the id of the collection created above

        assert response.status_code == status.HTTP_200_OK #asserts that the response status code is 200 (ok)
        assert response.data == { #asserts that the response data contains the correct id and title of the collection
            'id': collection.id,
            'title': collection.title,
            'products_count': 0 #asserts that the response data contains the correct products_count of the collection
        }


    def test_if_collection_does_not_exist_returns_404(self, api_client):
        # Arrange
        collection = baker.make(Collection) #creates a collection instance using model bakery and takes care of relationships for us
        non_existent_id = collection.id + 1 #creates a non-existent id by adding 1 to the id of the collection created above

        #Act
        response = api_client.get(f'/store/collections/{non_existent_id}/') #makes a get request to the collections endpoint with an id that does not exist

        assert response.status_code == status.HTTP_404_NOT_FOUND #asserts that the response status code is 404 (not found)
        assert response.data == {
            'detail': 'No Collection matches the given query.'
        }
        #asserts that the response data contains the correct error message

    def test_if_collection_exists_with_products_returns_200(self, api_client):
        # Arrange
        collection = baker.make(Collection) #creates a collection instance using model bakery and takes care of relationships for us 
        baker.make(Product, _quantity=5, collections=collection) #creates 5 product instances and associates them with the collection instance created above
        #Act
        response = api_client.get(f'/store/collections/{collection.id}/') #makes a get request to the collections endpoint with the id of the collection created above

        assert response.status_code == status.HTTP_200_OK #asserts that the response status code is 200 (ok)
        assert response.data == { #asserts that the response data contains the correct id and title of the collection
            'id': collection.id,
            'title': collection.title,
            'products_count': 5 #asserts that the response data contains the correct products_count of the collection
        }

    def test_if_collection_exists_with_no_products_returns_200(self, api_client):
        # Arrange
        collection = baker.make(Collection) #creates a collection instance using model bakery and takes care of relationships for us 
        #Act
        response = api_client.get(f'/store/collections/{collection.id}/') #makes a get request to the collections endpoint with the id of the collection created above

        assert response.status_code == status.HTTP_200_OK #asserts that the response status code is 200 (ok)
        assert response.data == { #asserts that the response data contains the correct id and title of the collection
            'id': collection.id,
            'title': collection.title,
            'products_count': 0 #asserts that the response data contains the correct products_count of the collection
        }


@pytest.mark.django_db
class TestListCollections:
    def test_returns_200(self, api_client):
        # Arrange
        baker.make(Collection, _quantity=3) #creates 3 collection instances using model bakery

        #Act
        response = api_client.get('/store/collections/') #makes a get request to the collections endpoint

        assert response.status_code == status.HTTP_200_OK #asserts that the response status code is 200 (ok)
        assert len(response.data) == 3 #asserts that the response data contains 3 collections

    def test_returns_collections_in_alphabetical_order(self, api_client):
        # Arrange
        baker.make(Collection, title='C') #creates a collection instance with title 'C' using model bakery
        baker.make(Collection, title='A') #creates a collection instance with title 'A' using model bakery
        baker.make(Collection, title='B') #creates a collection instance with title 'B' using model bakery

        #Act
        response = api_client.get('/store/collections/') #makes a get request to the collections endpoint

        assert response.status_code == status.HTTP_200_OK #asserts that the response status code is 200 (ok)
        assert response.data[0]['title'] == 'C' #asserts that the first collection in the response data has title 'A'
        assert response.data[1]['title'] == 'A' #asserts that the second collection in the response data has title 'B'
        assert response.data[2]['title'] == 'B' #asserts that the third collection in the response data has title 'C'

    def test_returns_empty_list_if_no_collections(self, api_client):
        # Arrange
        #no collections are created


        #Act
        response = api_client.get('/store/collections/') #makes a get request to the collections endpoint


        assert response.status_code == status.HTTP_200_OK #asserts that the response status code is 200 (ok)
        assert response.data == [] #asserts that the response data is an empty list
        

