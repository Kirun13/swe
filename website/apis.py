from .models import *
from datetime import datetime, timedelta
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

@api.route('/api/the_admin/register', methods=['POST'])
def register_admin():
    data = request.get_json()

    # Assuming 'user_id' is part of the incoming data
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({'error': 'user_id is required'}), 400

    # Hash the password (assuming you have 'the_password' in the incoming data)
    hashed_password = generate_password_hash(data.get('the_password'))

    # Create User record with the specified user_id
    admin_user = The_User(
        user_id=user_id,
        email=data.get('email'),
        givenname=data.get('givenname'),
        surname=data.get('surname'),
        middle_name=data.get('middle_name'),
        phone=data.get('phone'),
        address=data.get('address'),
        the_password=hashed_password,
        username=data.get('username'),
        salt=data.get('salt'),
        government_id=data.get('government_id'),
        user_role='ADMIN',
    )

    # Create Admin record and associate it with the User
    admin = The_Admin(admin_id=user_id)  # Use 'user_id' from the incoming data

    db.session.add(admin_user)
    db.session.add(admin)
    db.session.commit()

    return jsonify({'user_id': admin_user.user_id, 'message': 'Admin registered successfully'}), 201


@api.route("/api/the_admin/login", methods=["POST"])
def login_admin():
    data = request.get_json()

    admin_user = The_User.query.filter_by(email=data.get("email")).first()

    if admin_user and check_password_hash(admin_user.the_password, data.get("the_password")):
        access_token = create_access_token(
            identity={
                "user_id": admin_user.user_id,
                "user_role": admin_user.user_role,
                "email": admin_user.email,
            },
            expires_delta=timedelta(days=1),
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401


@api.route("/api/the_admin/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
