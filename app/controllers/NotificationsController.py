from flask import Blueprint, make_response, request

from app.components.ConfigurationComponent import ConfigurationComponent
from app.components.ShellComponent import ShellComponent

component = ShellComponent()

api = Blueprint('notifications_api', __name__)

url_prefix = "/notifications"


@api.route(url_prefix, methods=["POST"])
def post_notification():
    data = request.get_json()
    result = component.notify(data)
    return make_response(result, 200)


@api.route(url_prefix, methods=["GET"])
def get_notifications():
    configuration = ConfigurationComponent()
    result = configuration.diagnostics()
    return make_response(result, 200)


