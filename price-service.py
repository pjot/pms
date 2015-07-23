#!/usr/bin/env python

from flask import Flask, request, abort, Response
import json
import PMS

port = 1339
app = PMS.MicroService('PriceService', port)

prices = [
    { 
        'price' : 1000,
        'id' : 1
    },
    {
        'price' : 2000,
        'id' : 2
    }
]

@app.route('/api/price/<int:id>', methods=['GET'])
def get(id):
    for price in prices:
        if price['id'] == id:
            return Response(json.dumps(price))
    return 'not able to find id', id

app.start(debug=False, port=port)
