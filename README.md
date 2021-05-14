Test question:
https://www.notion.so/Patricia-s-Senior-Python-Developer-s-Test-29c7b6fed4474ac5ba7466c07642515d



## To run
Assuming there is python >= 3.8, pip, virtualenv, sqlite3 and Make installed on the machine where code will be run.

### pull project 

`git clone git@github.com:horlahlekhon/transaction-microservice.git`

`cd transaction-microservice`

`git checkout master`

#### Create virtual env and activate it
`virtualenv --python python3 .`

`source bin/activate`

#### Install dependencies
 `pip install -r requirements.txt`

#### Run migration
`make migrate`

### run test 
`make test`

### Seed db with client data
I provided a json file on the root of the folder `clients.json` clients should be registered there and a valid webhook url that 
accepts post request of the shape 

```json
{
  "transaction_reference": "ref",
  "status": "successful"
}
```
and return success response. requests will fail if the webhook url does not respond well. although transactions will be saved as further 
instructions were not given on what to do if webhook fails. after correct client data has been put in the file we hen run:
`make seed` to create database entry for the data.

### Run server

`make run`

#### make request
Request in the shape 

```json
{
    "transaction_reference": "ref",
    "price": 234.10,
    "status": "successful"
}
```
will be responded to and if it succeeded its response will be cached with the `hash(request body)`  as cache key,
using django's LRU caching system so that we can filter out duplicate requests before getting to the controllers.
on the other hand, if the request failed, we don't cache it.

the cache uses the standard HTTP cache-control policy to disable the cache so passing  `Cache-Control: No-Cache`, will make each request avoid the cache, but we wont still have duplicate transactions.

request are secured using client's api-key. check the database for an api key and add to header `x-api-key`
an example request will be.

```
curl --location --request POST '0.0.0.0:8000/microservice/' \
--header 'x-api-key: 18f22b543b3b9c8a1c9b8b23f4d71d637c18e59080e89b2f' \
--header 'Content-Type: application/json' \
--data-raw '{
    "transaction_reference": "ref",
    "price": 234.10,
    "status": "successful"
}'
```

The database is sqlite and data can be viewed by running sqlite command from cli or gui.
