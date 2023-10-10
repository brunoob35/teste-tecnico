Back-End application using Python and Flask

To run the application simply run the main.py

Ir provides the following routes:
POST http://localhost:5000/devices
POST http://localhost:5000/points
GET http://localhost:5000/devices
GET http://localhost:5000/device/{id}
GET http://localhost:5000/points/{serial}
PUT http://localhost:5000/devices/{serial}
PUT http://localhost:5000/points/{serial}
DELETE http://localhost:5000/devices/{serial}
DELETE http://localhost:5000/points/{serial}