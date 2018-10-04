
# Fast-Food-Fast
FAST-FOOD-FAST is an e-commerce platfrom dealing in food delivery.

**Installation and setup**

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
|`/api/v1/auth/signup`|`POST`|`Allows a user to register`|`customer`|`jwt`|
|`/api/v1/auth/login`|`POST`|`Allows the user to login`|`customer`|`jwt`|
|`/api/v1/users/orders`|`POST`|`creates an order`|`customer`|`jwt`|
|`/api/v1//users/orders `|`GET`|`gets the history of user orders`|`customer`|`jwt`|
|`/api/v1/orders`|`GET`|`gets all orders made by all customers`|`admin`|`jwt`|
|`/api/v1/orders/<orderId>`|`GET`|`gets a specific order`|`admin`|`jwt`|
|`/api/v1/​orders/<orderId>`|` PUT`|`update order status`|`admin`|`jwt`|
|`/api/v1/menu`|`GET`|`get a list of menu items`|`customer`|`jwt`|
|`/api/v1/menu`|`POST`|`add menu items`|`admin`|`jwt`|
