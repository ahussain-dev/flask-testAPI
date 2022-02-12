# Interview Practical Test - API

## Description
This is a small API with a single route, capable of meeting the singular requirement of returning users from London within a 50 mile radius. I've used parameters in order to make the request dynamic. Flask has been utilised to make this API; future implementations would include a class for a response model and further exception handling.

## Installation
https://flask.palletsprojects.com/en/2.0.x/installation/
Setup your Flask environment and run the requirements.txt document.

## Project Use
- Scheme Type: HTTP
- Operation: GET
- Route: /api/<string:city>/<int:distance>
- Parameters: 
City - String
Distance - Integer (maximum acceptable distance from city)
- Response Type: JSON
- Response: Success (Bool), Cache (Bool), HTTP Status, Data

### Example Response
| Keys  | Values |
| ------------- | ------------- |
| Success  | True  |
| Code  | 200  |
| Cache  | False |
| Data  | {"id": 1, "first_name": "Joe", "last_name": "Bloggs", ... etc}  |

## Tests
A small set of assertion tests were carried out on the route, to ensure appropriate response codes were delivered, type was JSON and that the JSON was modelled appropriately. Further tests could be created for a response model class, if included. They have been included in this repo in the /tests folder.

## Credits
This is the sole work of myself.
