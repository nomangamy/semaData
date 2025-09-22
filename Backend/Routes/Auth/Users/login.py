import Flask 
import jwt 
from flask import request, jsonify 
from flask_login import login_user,login_required,current_user
from datetime import datetime, timedelta
from models.users import Users
from  extensions import db
from flask import Blueprint
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

login_bp = Blueprint("login_bp",__name__)
@login_bp.route('/login',methods=['POST'])


def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message":"Invalid JSON data"}),400
        
        email = data.get("email")
        password = data.get("password")

        if not all([email,password]):
            return jsonify({"message":"Email and password are required"}),400
        
        user = Users.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user)
            token_payload = {
                'user_id': user.id,
                'exp': datetime.utcnow() + timedelta(hours=1)
            }
            token = jwt.encode(token_payload, 'your_secret_key', algorithm='HS256')
            return jsonify({
                "message":"Login successful!",
                "token":token,
                "user":{
                    "id":user.id,
                    "email":user.email,
                    "first_name":user.first_name,
                    "second_name":user.second_name}
            }),200
        else:
            return jsonify({"message":"Invalid email or password"}),401
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message":f"Error occurred: {str(e)}","debug_info":str(e)}),500

