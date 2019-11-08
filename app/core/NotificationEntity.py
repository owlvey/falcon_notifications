from app.core.MemberEntity import MemberEntity
from datetime import datetime

class NotificationEntity:
    def __init__(self):
        self.references = list()
        self.what = list()
        self.where = list()
        self.when = list()
        self.why = list()
        self.emotion = 3
        self.action = "alert"
        self.whom = list()  # type list[MemberEntity]

    def get_action_icon(self):
        if self.action == "alert":
            return ":fire:"
        if self.action == "award":
            return ":gem:"
        return ":fire:"

    def get_emotion_icon(self):
        if self.emotion == 1:
            return ":disappointed_relieved:"
        if self.emotion == 2:
            return ":disappointed:"
        if self.emotion == 3:
            return ":relieved:"
        if self.emotion == 4:
            return ":smiley:"
        return ":sunglasses:"

    def get_message(self, member: MemberEntity):

        greetings = "Good " + ("morning <@" if datetime.now().hour < 12 else "afternoon <@") + \
                    member.slack_member + "> \n"

        if self.why:
            temporal = " {} \n {} \n *When*: {} \n *Where* {} , {}. \n *Why*: \n {} \n {} ".format(greetings,
                                                                                                 self.get_action_icon(),
                                                                               "\n".join(self.when), ",".join(self.where),
                                                                               ",".join(self.what), "\n".join(self.why),
                                                                               self.get_emotion_icon())
        else:
            temporal = " {} \n {} {}, In {} , {}. \n {} ".format(greetings, self.get_action_icon(),
                                                                 "\n".join(self.when), ",".join(self.where),
                                                                 ",".join(self.what),
                                                                 self.get_emotion_icon())

        if self.references:
            temporal += " \n Please check :male-detective:  {}".format(",".join(self.references))

        return temporal

    def load(self, data: dict):
        members = data["whom"]
        for item in members:
            temp = MemberEntity()
            temp.load(item)
            self.whom.append(temp)
        self.what = data.get("what")
        self.when = data.get("when")
        self.where = data.get("where")
        self.why = data.get("why")
        self.references = data.get("references")
        self.emotion = data.get("emotion") or 3
        self.action = data.get("action") or "alert"

