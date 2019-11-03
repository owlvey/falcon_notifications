import unittest
from app.core.NotificationEntity import NotificationEntity


class TestNotificationEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_notification_load_what(self):
        notification = NotificationEntity()
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
                "tags": {
                    "slack": "UFR3ZBD6Y"
                }
            }]
        }
        notification.load(data)
        self.assertEqual(1, len(notification.what))
        self.assertEqual(1, len(notification.whom))

    def test_notification_load_whom(self):
        notification = NotificationEntity()
        data = {
            "what": [],
            "whom": [{
                "name": "gvalderrama",
                "slack_member": "UFR3ZBD6Y"
            }]
        }
        notification.load(data)
        self.assertEqual(1, len(notification.whom))
        self.assertTrue(notification.whom[0].slack_member)
        self.assertTrue(notification.whom[0].name)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
