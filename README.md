[![Build Status](https://travis-ci.org/mulondo/Fast-Food-Fast.svg?branch=ft-challenge-two)](https://travis-ci.org/mulondo/Fast-Food-Fast) [![Coverage Status](https://coveralls.io/repos/github/mulondo/Fast-Food-Fast/badge.svg?branch=api)](https://coveralls.io/github/mulondo/Fast-Food-Fast?branch=api) [![Maintainability](https://api.codeclimate.com/v1/badges/ed9209343cc8dbd0879d/maintainability)](https://codeclimate.com/github/mulondo/Fast-Food-Fast/maintainability)

# Fast-Food-Fast
FAST-FOOD-FAST is an e-commerce platfrom dealing in food delivery.

**Installation and setup**

Clone the repository from github:<br/>

```git clone https://github.com/mulondo/Fast-Food-Fast.git```

Create virtualenv and activate it:

Install pip

pip install virtualenv

virtualenv venv

activate the virtualenv<br/>

On windows:

```mypthon\Scripts\activate ```<br/>
On linux/os:

```source/venv/acticate```

**API End points**
 
|Resource URL|Methods   |Description|
|----------------|------------|-------------|
|`/api/v1/orders` |`GET,POST` |`Get all orders,Add an order` |
|`/api/v1/orders/<int:order_id>` |`GET,PUT`|`Get a specific order, Update the status of a specific order` |
