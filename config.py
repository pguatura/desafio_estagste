import json
import urllib2
import hmac
import hashlib
import os

class Configuration(object):
    config_dict = {}

    def __init__(self):
        self.init_config()

    def init_config(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        self.config_dict = json.loads(open(directory + '/config').read())
        if 'user_token' in self.config_dict:
            self.config_dict['access_token'] = self.config_dict['user_token']
        else:
            self.getFacebookAppToken()


    def getFacebookAppToken(self):
        url = ("https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials" % (self.config_dict['client_id'], self.config_dict['client_secret']))
        response = urllib2.urlopen(url)
        self.config_dict['access_token'] = response.read().split('=')[1]


config = Configuration()
