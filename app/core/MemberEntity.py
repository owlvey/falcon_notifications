class MemberEntity:
    def __init__(self):
        self.email = None
        self.slack_member = None
        self.notified = False
        self.name = None

    def load(self, data: dict):
        self.email = data.get("email")
        self.slack_member = data.get("slack_member")
        self.name = data.get("name")
