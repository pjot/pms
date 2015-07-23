#!/usr/bin/env python

from flask import Flask, request, abort, Response
import json
import PMS

port = 1340
app = PMS.MicroService('Lister', port)

products = app.call('ProductService', 'products')

for product in products:
    price = app.call('PriceService', 'price/' + str(product['id']))
    print product
    print price
