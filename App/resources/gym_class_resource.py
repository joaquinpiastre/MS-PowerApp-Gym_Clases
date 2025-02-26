from flask import jsonify, Blueprint, request
from app.services.gym_class_service import GymClassService
from app.mapping.gym_class_schema import GymClassSchema


gym_class = Blueprint('gym_class', __name__)
gym_class_schema = GymClassSchema()

# find all
@gym_class.route('/find_all_classes', methods=['GET'])
def get_classes():
    service = GymClassService()
    class_data = gym_class_schema.load(request.json)
    classes = service.find_all(class_data)
    return jsonify({"Classes": classes}), 200

#create
@gym_class.route('/add_class', methods=['POST'])
def create_class():
    service = GymClassService()
    class_data = request.get_json()
    new_class = service.create(class_data)
    return {"message": "Clase creada", "class": GymClassSchema().dump(new_class)}, 201

#update
@gym_class.route('/update_class/<int:id>', methods=['PUT'])
def update_class(id):
    service = GymClassService()
    class_data = request.json
    updated_class = service.update(class_data, id)
    return {"message": "Clase actualizada", "class": GymClassSchema().dump(updated_class)}, 200

#delete
@gym_class.route('/delete_class/<int:id>', methods=['DELETE'])
def delete_class(id):
    service = GymClassService()
    service.delete(id)
    return {"message": "Clase eliminada"}, 200
