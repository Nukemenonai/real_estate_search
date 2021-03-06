# Real Estate Search 

## Description 
This is a simple project created for external users to consult available estate for sale. With this service users should be able to see available and sold estate

Additionally the tool allows that users can "like" estate in order to have an internal ranking for the most attractive estate

## Technologies used
* Python:  
* MySQL: 

## How the project is to be aproached 
* Test driven development: Tests are made to ensure the code satisfies incremental test cases

The code attempts to follow domain driven design guidelines 

## How to use locally: 
Clone the repository 
Set the environment variables (maybe use export $(cat .env | grep -v ^# | xargs) along with env example file)
run python server.py
## Endpoints 
### GET: /status
Retrieves the status of the microservice, including the app name and version 
### POST: /estate
Main endpoint of the microservice. retrieves all available estate according to search criteria 

#### Params: 
* year: year of construction of the estate
* city: city where estate is located
* status: 3, 4, 5 if the estate is on pre-sale, sale or sold respectively

#### request body 
```
{
    "year": 2000
    "city": "bogota"
    "statuses": [3, 4, 5]
}
```
#### response body 

```
[
    {
        "Address": "calle 23 #45-67",
        "City": "bogota",
        "Price": 120000000,
        "Description": "Hermoso apartamento en el centro de la ciudad",
        "Status": "pre_venta"
    },
    ...
]
```

## Likes service

The repository extends on the current model using a new table "likes" like so: 

* ![](./entity_relationship.png)

This table allows to get the register when an user gives a like to a property and also to get the historical of likes for each user and to what estate were they given. 
