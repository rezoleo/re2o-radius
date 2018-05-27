# encoding=utf8

import socket

import requests

from config import Config

CONFIG = Config()

username = CONFIG['Default']['USERNAME']
password = CONFIG['Default']['PASSWORD']


class Re2o:
    def __init__(self):
        self.session = requests.session()
        self.errors = []
        self.csrftoken = None

    def get_csrf_token(self, url):
        self.session.get(url)
        self.csrftoken = self.session.cookies['csrftoken']

    def init_connection(self):
        try:
            login_url = CONFIG.get_url('login')
            self.get_csrf_token(login_url)
            self.login_data = {'username': username, 'password': password, 'csrfmiddlewaretoken': self.csrftoken}
            self.resp_co = self.session.post(login_url, data=self.login_data, headers=dict(referer=login_url))
        except Exception as err:
            self.errors.append(err)
            print(self.errors)  # TODO Handle errors
        return

    def check_mac(self, mac_search):
        try:
            mac_search = mac_search.lower()
            mac_ip_dns = self.session.post(CONFIG.get_rest_url('mac-ip-dns'))
            mac_ip_dns.raise_for_status()
            mac_list = mac_ip_dns.json()  # type: list
            return len(list(filter(lambda mac: mac['mac_address'].lower() == mac_search, mac_list))) >= 1
        except Exception as err:
            print(err)  # TODO
