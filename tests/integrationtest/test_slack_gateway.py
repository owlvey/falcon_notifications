import unittest
import os
from app.Gateways.SlackGateway import SlackGateway
from app.components.ConfigurationComponent import ConfigurationComponent


class TestSlackGateway(unittest.TestCase):
    def setUp(self):
        self.slack = SlackGateway(ConfigurationComponent())

    def test_send_message(self):
        self.slack.send_message("UFR3ZBD6Y", "test")
        self.slack.send_message("UFR3ZBD6Y", ":cry:")


if __name__ == '__main__':
    unittest.main()