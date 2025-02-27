from flask import Blueprint, request, jsonify, abort
from .validators import validate_animal_data

animal_blueprint = Blueprint('animals', __name__)

animals = {
    "lion": {"name": "Lion", "species": "Panthera leo", "habitat": "Savannah"},
    "elephant": {"name": "Elephant", "species": "Loxodonta africana", "habitat": "Savannah"}
}


@animal_blueprint.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(list(animals.values()))


@animal_blueprint.route('/animals/<string:animal_name>', methods=['GET'])
def get_animal(animal_name):
    animal = animals.get(animal_name.lower())
    if not animal:
        abort(404, description="Animal not found")
    return jsonify(animal)


@animal_blueprint.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()

    error = validate_animal_data(data)
    if error:
        abort(400, description=error)

    name = data['name'].lower()
    if name in animals:
        abort(400, description="Animal already exists")

    animals[name] = data
    return jsonify(data), 201
