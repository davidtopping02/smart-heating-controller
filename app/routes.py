from flask import request, jsonify
from app import create_app
from app.servo_control import move_servo, get_servo_position

app = create_app()


@app.route('/api/heat/position', methods=['POST'])
def set_position():
    data = request.get_json()
    position = data.get('position')
    if position not in [1, 2, 3, 4, 5]:
        return jsonify({"status": "error", "message": "Invalid position"}), 400

    move_servo(position)
    return jsonify({"status": "success", "message": f"Moved to position {position}"}), 200


@app.route('/api/heat/position', methods=['GET'])
def get_position():
    position = get_servo_position()
    return jsonify({"current_position": position}), 200
