import os
from slackclient import SlackClient

from app.components.ConfigurationComponent import ConfigurationComponent


class ConsoleClient:

    def api_call(self, method, timeout=None, **kwargs):
        print("\n")
        print("method: {}, channel: {}, text: {}".format(method, kwargs["channel"], kwargs["text"]))
        print("\n")
        result = dict()
        result["ok"] = True
        return result


class SlackGateway:
    def __init__(self, configuration: ConfigurationComponent):

        self.configuration = configuration
        client_proxies = dict()
        if configuration.get_falcon_http_proxy():
            client_proxies["http"] = self.configuration.get_falcon_http_proxy()
        if self.configuration.get_falcon_https_proxy():
            client_proxies["https"] = self.configuration.get_falcon_https_proxy()

        if self.configuration.get_slack_key() and self.configuration.get_slack_key() != "console":
            self.sc = SlackClient(self.configuration.get_slack_key(), proxies=client_proxies)
        else:
            self.sc = ConsoleClient()

    def send_message(self, target, message):
        result = self.sc.api_call("chat.postMessage", channel=target, text=message)
        if not result["ok"]:
            raise ValueError(result)
        else:
            print(" \n send message to {}".format(target))
        return result

