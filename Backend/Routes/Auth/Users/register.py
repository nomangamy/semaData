from models.DomainOwner import DomainOwner
from models.users import Users 
from  extensions import db 
from flask import request,jsonify,url_for,Blueprint,session
from werkzeug.security import generate_password_hash
from flask_login import login_user,login_required,current_user
from datetime import datetime
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()



register_bp =Blueprint("register_bp",__name__) 

@register_bp.route('/register',methods=['POST'])

def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message":"Invalid JSON data"}),400
        
        email = data.getZ("email")
        first_name = data.get("firstName")
        second_name = data.get("secondName")
        password = data.get("password")

        if not all([email,first_name,second_name,password]):
            return jsonify({"message":"All fields are required"}),400
        
        if Users.query.filter_by(email =email).first() or \
            DomainOwner.query.filter_by(owner_email=email).first():
            return jsonify({"message":"Email already registered."}),400
        
        password =bcrypt.generate_password_hash(password).decode('utf-8')

        new_user =Users(
            email = email,
            first_name = first_name,
            second_name = second_name,
            password = password 
        )
        if new_user:
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message":"Registration successful!"}),201
        else:
            return jsonify({"message":"Error during registration."}),500
    except Exception as e:
        db.session.rollback()
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message":f"Error occurred: {str(e)}","debug_info":str(e)}),500
    






















