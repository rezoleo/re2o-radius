#!/usr/bin/env python3
# encoding=utf8

"""Wrapper around configparser to manage config."""

import configparser


class Config(configparser.ConfigParser):
    """Manage project configuration."""

    _CONFIG_FILES = [
        # '/usr/local/etc/re2o/config.ini',
        '/etc/re2o/config.ini',
        '/etc/raddb/scripts/re2o-radius/config.ini',
    ]

    def __init__(self):
        super().__init__()
        self.parsed_files = self.read(self._CONFIG_FILES)

    def get_url(self, url):
        return self['Default']['URL'] + url + '/'

    def get_rest_url(self, url):
        return self['Default']['URL'] + 'machines/rest/' + url + '/'
