# coding = utf-8
from flask import Blueprint,request,session
import json
from ..models import User
from apps import db
api_bp = Blueprint('user_api_v1',__name__)

@api_bp.route('/demo')
def demo():
    return "Demo"

@api_bp.route('/user_api_v1/register',methods=['post'])
def regieter():
    """
    注册
    :return:
    """
    user_info = json.loads(request.data)
    username = user_info.get("username",None)
    password = user_info.get("password",None)
    password2 = user_info.get("password2",None)
    phone = user_info.get("phone",None)
    if not username or not password or not password2 or not phone:
        return {"data":None,"response":"failed",'msg':'Lack of parameter'},200

    user_list = User.query.filter_by(phonenumber=phone).all()
    if user_list:
        return {"data":"The phone has been registered","response":"failed",'msg':'Lack of parameter'},200
    else:
        user = User(username=username,phonenumber=phone,password=password)
        print(user)
        db.session.add(user)
        db.session.commit()
        return {"data":{"username":username,"password":password,"phone":phone},"response":"successful",'msg':'0'},201

@api_bp.route('/user_api_v1/login',methods=['post'])
def login():
    user_info = json.loads(request.data)
    username = user_info.get("username", None)
    password = user_info.get("password", None)
    if not username or not password:
        return {"data": None, "response": "failed", 'msg': 'Lack of parameter'}, 200

    user_list = User.query.filter_by(username=username).all()

    if not user_list:
        return {"data":"This user does not exist","response":"failed","msg":"0"},200

    return {"data":None,"response":"successful","msg":"0"},200
