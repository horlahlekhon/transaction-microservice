## To run

### pull project 

`git clone git@github.com:horlahlekhon/transaction-microservice.git`

`cd transaction-microservice`

#### Create virtual env and activate it
`virtualenv --python python3`

`source bin/activate`

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


The database is sqlite and data can be viewed by running sqlite command from cli or gui.
