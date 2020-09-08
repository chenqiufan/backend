# coding = utf-8
from flask import Blueprint,request,session

from ..models import User
api_bp = Blueprint('user_api_v1',__name__)

@api_bp.route('/login',methods=['post'])
def login():
    try:
        data = request.data.decode('utf-8')
        print(data)
    except Exception as e:
        print(e)
    return "successed"

@api_bp.route('/demo')
def demo():
    return "Demo"