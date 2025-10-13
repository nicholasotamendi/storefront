
from locust import HttpUser, task, between
from random import choice, randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5) # Simulate a user waiting between 1 to 5 seconds between tasks
    # Define tasks for the user to perform, such as:
    # viewing products
    # viewing product details
    # adding a product to the cart
    # viewing the cart

    @task (2)
    def view_products(self):
        collection_id = randint(1, 6)  # Assuming collection IDs range from 2 to 6
        self.client.get(f'/store/products/?collection_id={collection_id}', name="/store/products/") # View products in a collection

    @task (4)
    def view_product(self):
        product_id = randint(1, 6)  # Assuming product IDs range from 1 to 6
        self.client.get(f'/store/products/{product_id}/', 
                        name="/store/products/[id]/") # View product details
    @task (1)
    def add_to_cart(self):
        product_id = randint(1, 4)  # Assuming product IDs range from 1 to 4
        self.client.post(f'/store/carts/{self.cart_id}/items/',
                         name="/store/carts/items/",
                         json={"product_id": product_id, "quantity": 1}) # Add product to cart

    @task (1)
    def say_hello(self):
        self.client.get('/playground/hello/')

    def on_start(self):
        res = self.client.post('/store/carts/') # Create a new cart when the user starts
        if res.status_code == 201:
            result = res.json()
            self.cart_id = result['id']
        else:
            print(f"ERROR: Failed to create cart on start. Status: {res.status_code}")


