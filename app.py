# Imports
from flask import Flask, request, jsonify, abort, make_response
import json
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from functions.user_list import UserList


# Initialisation
app = Flask(__name__)
geolocator = Nominatim(user_agent="MyApp")

"""
Returns users matching the city, and those that fall within the distance parameter
Eg: api/London/50
"""
# Routes
@app.route('/api/<string:city>/<int:distance>/', methods=['GET'])
def get_users(city, distance):
    if request.method == "GET":
        # Prepare response_data
        response_data = []

        # Collect all with matching city and append
        try:
            response = requests.get(f" https://bpdts-test-app.herokuapp.com/city/{city}/users")
            city_model = UserList(response)
            city_list = city_model.return_list()
            for user in city_list:
                response_data.append(user)
        except requests.exceptions.HTTPError as error:
            abort(error.response.status_code)

        # Collect all within distance parameter of city
        try:
            response = requests.get("https://bpdts-test-app.herokuapp.com/users")
            distance_model = UserList(response)
            distance_list = distance_model.return_list()
        except requests.exceptions.HTTPError as error:
            abort(error.response.status_code)

        # Find longitude and latitude of city parameter
        city_location = geolocator.geocode(city)
        city_long_lat = (city_location.latitude, city_location.longitude)

        # Check if user is within distance parameter and not already in response data
        for user in distance_list:
            user_lat_long = (user["latitude"], user["longitude"])
            distance_from_city = geodesic(city_long_lat, user_lat_long).miles
            if distance_from_city < distance and user["id"] not in response_data:
                response_data.append(user)

        if len(response_data) == 0:
            return make_response(jsonify({"success": True, "cache": False, "data": "No results returned"}, 204))
        return make_response(jsonify({"success": True, "cache": False, "data": response_data}), 200)
    else:
        abort(405)


# Error Handling
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"success": False, "cache": False, "data": "Bad Request"}), 400)


@app.errorhandler(401)
def unauthorised(error):
    return make_response(jsonify({"success": False, "cache": False, "data": "Unauthorised"}), 401)


@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({"success": False, "cache": False, "data": "Forbidden"}), 403)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"success": False, "cache": False, "data": "Not found"}), 404)


@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({"success": False, "cache": False, "data": "Method not allowed"}), 405)


@app.errorhandler(410)
def resource_gone(error):
    return make_response(jsonify({"success": False, "cache": False, "data": "Gone"}), 410)


if __name__ == '__main__':
    app.run()
