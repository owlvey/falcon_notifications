import os


class ConfigurationComponent:

    def __init__(self):
        pass

    def get_falcon_http_proxy(self):
        return os.environ.get("falcon_http_proxy")

    def get_falcon_https_proxy(self):
        return os.environ.get("falcon_https_proxy")

    def get_slack_key(self):
        return os.environ.get("owlvey_slack_key")

    def diagnostics(self):
        result = dict()
        result["owlvey_slack_key"] = True if self.get_slack_key() else False
        return result