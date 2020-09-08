# coding = utf-8
from flask import Blueprint,request,session

from ..models import User
api_bp = Blueprint('user_api_v1',__name__)


@api_bp.route('/login',methods=['POST'])
def login():
    session["name"] = ""
    data = request.data
    print(data)
    return "successed"
