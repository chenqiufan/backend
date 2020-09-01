# coding = utf-8
from flask import Blueprint

from ..models import User
api_bp = Blueprint('user_api_v1',__name__)


@api_bp.route('/')
def login():
    return "successed"
