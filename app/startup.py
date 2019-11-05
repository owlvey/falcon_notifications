import json
import os

from app.components.ConfigurationComponent import ConfigurationComponent
from app.controllers.NotificationsController import api as notification_api
from app.controllers.AvailabilityController import api as availability_api

from flask import Flask

from app.core.NotificationEntity import NotificationEntity

app = Flask(__name__)
app.register_blueprint(notification_api)
app.register_blueprint(availability_api)


@app.route('/')
def home():
    notification = NotificationEntity()
    result = dict()
    result["diagnostic"] = (ConfigurationComponent()).diagnostics()
    result["sample"] = notification.__dict__
    return result


if __name__ == "__main__":
    app.run(debug=True)


