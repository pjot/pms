#!/usr/bin/env python
import requests
import json
import traceback
from flask import Flask

class MicroService(Flask):
    registry_url = 'http://localhost:1337/api/service'
    name = ''
    port = ''
    registered = False

    def __init__(self, name, port):
        self.name = name
        self.port = str(port)
        Flask.__init__(self, name)
        self.route('/api/ping', endpoint=self.ping)

    def start(self, **kwargs):
        self.register()
        Flask.run(self, **kwargs)

    def ping():
        return 'pong'

    def call(self, service, method, data = None):
        params = data or {}
        url = requests.get(self.registry_url + '/' + service).text
        print self.registry_url + '/' + service
        print url + method
        return requests.get(url + method, params=params).json()

    def register(self):
        if self.registered:
            print 'already registered'
            return

        data = {
            'name' : self.name,
            'url' : 'http://localhost:' + self.port + '/api/'
        }
        headers = {
            'Content-Type' : 'application/json'
        }
        print('registering')
        response = requests.post(self.registry_url, json.dumps(data), headers=headers) 
        if response.text == 'OK':
            print 'registered'
            self.registered = True
        else:
            print 'failed to register'
            self.registered = False
