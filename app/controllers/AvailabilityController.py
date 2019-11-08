from flask import Blueprint, make_response, request

from app.components.ConfigurationComponent import ConfigurationComponent
from app.components.ShellComponent import ShellComponent
from app.core.AvailabilityProductToNotificationTranslator import AvailabilityProductToNotificationTranslator
from app.core.AvailabilityServiceToNotificationTranslator import AvailabilityServiceToNotificationTranslator
from app.core.AvailabilitySquadToNotificationTranslator import AvailabilitySquadToNotificationTranslator

component = ShellComponent()

api = Blueprint('availability_api', __name__)

url_prefix = "/availability"


@api.route(url_prefix + "/services", methods=["POST"])
def post_notification():
    data = request.get_json()
    notification = AvailabilityServiceToNotificationTranslator.translate(data)
    result = component.notify(notification)
    return make_response(result, 200)


@api.route(url_prefix + "/products", methods=["POST"])
def post_products_notification():
    data = request.get_json()
    notification = AvailabilityProductToNotificationTranslator.translate(data)
    result = component.notify(notification)
    return make_response(result, 200)


@api.route(url_prefix + "/squads", methods=["POST"])
def post_squads_notification():
    data = request.get_json()
    notification = AvailabilitySquadToNotificationTranslator.translate(data)
    if notification:
        result = component.notify(notification)
        return make_response(result, 200)
    else:
        return make_response({}, 200)

