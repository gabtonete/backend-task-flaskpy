from flask import Blueprint

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login', method=["POST"])
def login():
    pass