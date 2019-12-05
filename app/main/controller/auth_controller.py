from flask import request
from flask_restplus import Resource, cors

from app.main.model.auth_dto import AuthDto
from app.main.service.auth_helper import Auth

api = AuthDto.api
user_auth = AuthDto.user_auth


@cors.crossdomain(origin="*")
@api.route("/login")
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc("user_login")
    @api.expect(user_auth, validate=True)
    def post(self):
        """Login the user"""
        post_data = request.json
        return Auth.login_user(data=post_data)


@cors.crossdomain(origin="*")
@api.route("/logout")
class LogoutAPI(Resource):
    """
    Logout Resource
    """

    @api.doc("user_logout")
    def post(self):
        """Logout the user"""
        auth_header = request.headers.get("Authorization")
        return Auth.logout_user(data=auth_header)
