from app.core.MemberEntity import MemberEntity


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
        return ":eyes:"

    def get_emotion_icon(self):
        if self.emotion == 1:
            return ":disappointed_relieved:"
        if self.emotion == 2:
            return ""
        if self.emotion == 3:
            return ""
        if self.emotion == 4:
            return ""
        return ""

    def get_message(self):
        temporal = "{} At {} , in {} , {} because {}. {} ".format(self.get_action_icon(),
                                                                  ",".join(self.when), ",".join(self.where),
                                                                  ",".join(self.what), ",".join(self.why),
                                                                  self.get_emotion_icon())
        if self.references:
            temporal += " Please review :male-detective:  {}".format(",".join(self.references))

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

