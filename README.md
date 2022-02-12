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
| Data  | {"id": 1, "name": "Joe Bloggs"}  |

## Tests
Testing information here.

## Credits
This is the sole work of myself.
