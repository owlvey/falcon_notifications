from app.components.MessagingComponent import MessagingComponent
from app.core.NotificationEntity import NotificationEntity


class ShellComponent:
    def __init__(self):
        self.messaging_component = MessagingComponent()
        pass

    def notify(self, data: dict):
        result = dict()
        notification = NotificationEntity()
        notification.load(data)
        self.messaging_component.notify(notification)
        return result
