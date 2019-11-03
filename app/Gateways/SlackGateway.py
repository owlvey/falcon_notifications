import os
from slackclient import SlackClient

from app.components.ConfigurationComponent import ConfigurationComponent


class SlackGateway:
    def __init__(self, configuration: ConfigurationComponent):

        self.configuration = configuration
        client_proxies = dict()
        if configuration.get_falcon_http_proxy():
            client_proxies["http"] = self.configuration.get_falcon_http_proxy()
        if self.configuration.get_falcon_https_proxy():
            client_proxies["https"] = self.configuration.get_falcon_https_proxy()
        self.sc = SlackClient(self.configuration.get_slack_key(), proxies=client_proxies)

    def send_message(self, target, message):
        result = self.sc.api_call("chat.postMessage", channel=target, text=message)
        if not result["ok"]:
            raise ValueError(result)
        return result

