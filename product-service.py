#!/usr/bin/env python

from flask import Flask, request, abort, Response
import json
import PMS

port = 1338
app = PMS.MicroService('ProductService', port)

products = [
    { 
        'name' : 'Grundpakke',
        'id' : 1
    },
    {
        'name' : 'Silverpakke',
        'id' : 2
    }
]

@app.route('/api/products', methods=['GET'])
def get():
    return Response(json.dumps(products))

app.start(debug=False, port=port)
