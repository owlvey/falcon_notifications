from app.Gateways.SlackGateway import SlackGateway
from app.components.ConfigurationComponent import ConfigurationComponent
from app.core.NotificationEntity import NotificationEntity


class MessagingComponent:
    def __init__(self):
        self.slack_gateway = SlackGateway(ConfigurationComponent())

    def notify(self, notification: NotificationEntity):

        slack_members = filter(lambda c: c.slack_member and c.notified is False,
                               notification.whom)

        for item in slack_members:
            self.slack_gateway.send_message(item.slack_member, notification.get_message())
            item.notified = True
