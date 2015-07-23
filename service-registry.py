#!/usr/bin/env python
import logging
import json
from flask import Flask, request, abort, Response

logging.basicConfig(level=logging.DEBUG)

app = Flask('ServiceRegistry')
services = []

class Service:
    name = ''
    url = ''

    def __init__(self, data):
        self.name = data['name']
        self.url = data['url']

@app.route('/api/services', methods=['GET'])
def list():
    result = []
    for service in services:
        result.append({'name': service.name, 'url': service.url})

    return Response(json.dumps(result))

@app.route('/api/service', methods=['POST'])
def add():
    service = Service(request.get_json())
    services.append(service)
    print "adding", service.name
    print services
    return 'OK'

@app.route('/api/service/<string:name>', methods=['GET'])
def get(name):
    for service in services:
        if service.name == name:
            return service.url
    abort(404)

app.run(debug=False, port=1337)
