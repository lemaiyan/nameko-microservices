# Nameko Star Trek App

This app comprises of three services
* Crew Service
* Ship Service 
* Gateway Service

The purpose is to demonstrate how Nameko microservices work, the services are part of one code base but 
they have been separated at the `docker-compose` level where each service is isolated from 
the other service only sharing the `rabbitmq` instance.


## Getting Started

To tun the application 
* Run `docker-compose up` 
* Import this [Postman Collection](https://www.getpostman.com/collections/9df78f3df56de02db6cc) to postman
and interact with the service.


## Tests

To run tests run the command `docker-compose run star_trek_service pytest tests`




