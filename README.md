[![Build Status](https://travis-ci.org/mulondo/Fast-Food-Fast.svg?branch=ft-challenge-three)](https://travis-ci.org/mulondo/Fast-Food-Fast) [![Coverage Status](https://coveralls.io/repos/github/mulondo/Fast-Food-Fast/badge.svg?branch=heroku_host)](https://coveralls.io/github/mulondo/Fast-Food-Fast?branch=heroku_host) [![Maintainability](https://api.codeclimate.com/v1/badges/ed9209343cc8dbd0879d/maintainability)](https://codeclimate.com/github/mulondo/Fast-Food-Fast/maintainability)
# Fast-Food-Fast
FAST-FOOD-FAST is an e-commerce platfrom dealing in food delivery.

##Installation and setup

Clone the repository from github:<br/>

```
git clone https://github.com/mulondo/Fast-Food-Fast.git

```
Create virtualenv and activate it:

- Install pip

- pip install virtualenv

- virtualenv venv

- activate the virtualenv<br/>

On windows:

```
mypthon\Scripts\activate 

```
On linux/os:

```
source/venv/acticate

```

Run the application

```
python run.py
```
Test the application by running

```

pytest or python -m unittest

```

**API End points**
 
|Resource URL|Methods   |Description|User type|Authentication|
|----------------|------------|-------------|-------------|-------------|
|`/api/v2/auth/signup`|`POST`|`Allows a user to register`|`customer`|`jwt`|
|`/api/v2/auth/login`|`POST`|`Allows the user to login`|`customer`|`jwt`|
|`/api/v2/users/orders`|`POST`|`creates an order`|`customer`|`jwt`|
|`/api/v2//users/orders `|`GET`|`gets the history of user orders`|`customer`|`jwt`|
|`/api/v2/orders`|`GET`|`gets all orders made by all customers`|`admin`|`jwt`|
|`/api/v2/orders/<orderId>`|`GET`|`gets a specific order`|`admin`|`jwt`|
|`/api/v2/​orders/<orderId>`|` PUT`|`update order status`|`admin`|`jwt`|
|`/api/v2/menu`|`GET`|`get a list of menu items`|`customer`|`jwt`|
|`/api/v2/menu`|`POST`|`add menu items`|`admin`|`jwt`|
|`/api/v2/make_admin/<int:user_id>`|`PUT`|`assign admin role`|`admin`|`jwt`|
