import unittest
import os
from app.Gateways.SlackGateway import SlackGateway
from app.components.MessagingComponent import MessagingComponent
from app.components.ShellComponent import ShellComponent


class TestMessagingComponent(unittest.TestCase):

    def setUp(self):
        self.component = ShellComponent()

    def test_notifications(self):
        data = {
            "references": [
                "http://www.google.com"
            ],
            "why": [
                "login has 0.95 availability"
            ],
            "when": [
                "2019-01-01 to 2019-02-02"
            ],
            "where": [
                "personal loan"
            ],
            "what": [
                "SLO with 0.99 is broken with 0.95 availability"
            ],
            "whom": [{
                "name": "gvalderrama",
                "email": "test@email.com",
                "slack_member": "UFR3ZBD6Y"
            }]
        }
        self.component.notify(data)
        # self.slack.send_message("UFR3ZBD6Y", ":cry:")


if __name__ == '__main__':
    unittest.main()