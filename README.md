 ## Bakery API 
 This is a Django REST API for the bakery.

### Features:

- User can place order, view order details and generate bill for the order.
- Admin can add ingredients, add bakery items and view bakery item details and manage inventory.
- Unauthorized users can view the list of available bakery products, but cannot place order.
- Unauthorized users can register as a customer and obtain a JWT token for authentication.
- Customer can filter the product search .



### Clone the Repo
```
git clone https://github.com/nidhi-2619/bakery-api.git
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Setup Database
Setup database settings inside `bakery/settings.py` file
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3308',
    }
}
```
### Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

To create a superuser account, use this command:

```
python manage.py createsuperuser
```

### Start the development Server

```
python manage.py runserver
```
Server will be available at` http://127.0.0.1:8000 `in your browser

### API Endpoints
##### Admin Endpoints
```
POST /api/ingredients/:Create a new ingredient.
POST /api/bakeryitems/: Create a new bakery item with ingredients.
GET /api/bakeryitems/{id}/: Get details of a specific bakery item.
```

##### Customer Endpoints

```
GET /api/products/: Get a list of available bakery products.
POST /api/customers/register/: Register a new customer.
POST /api/token/: Obtain a JWT token for authentication.
GET /api/orders/: Get a list of orders.
POST /api/orders/: Place a new order.
GET /api/orders/{id}/: Get details of a specific order.
GET /api/orders/{id}/bill/: Generate the bill for a specific order.
```

### Authentication
The API uses `JSON Web Tokens (JWT)` for authentication. To obtain a token, make a `POST` request to the` /api/token/` endpoint with the` username` and `password`. 
Include the token in the Authorization header of subsequent requests with the format `Bearer <token>`.
