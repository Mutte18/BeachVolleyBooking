from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "secret"
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if username != 'userX' or password != 'password':
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/protected', methods=['GET'])
@jwt_required()
def getInfo():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

    # current_user = request.jwt_identity
    # return jsonify(logged_in_as=current_user), 200


if __name__ == '__main__':
    app.run(debug=True)
