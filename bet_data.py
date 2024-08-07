import os
import random
import pandas as pd
import urllib.parse
from time import sleep
from flask import Flask, jsonify, request, make_response
import mercadopago
import requests
from datetime import datetime
sdk = mercadopago.SDK("TEST-5028275400963991-072115-e9d62c74c3f2a777a6cd57d7470171ee-1905753922")
app = Flask(__name__)
webhook_url = 'https://backend.botconversa.com.br/api/v1/webhooks-automation/catch/8476/24JR7uiXjkVY/'

@app.route("/create_link_payment", methods=['POST'])
def create_link_payment():
    payment =create_payment(request.json)
    result	= sdk.payment().create(payment)
    response = result["response"]
    #link = response["ticket_url"]
    return response

@app.route("/get_info_preferences", methods=['GET'])
def get_info_preferences():
    preference_response = sdk.preference().get("1905753922-666d43a0-3487-468d-9c12-7ab5dc9623a7")
    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
	    'x-idempotency-key': '1234'
    }
    response = preference_response["response"]
    return response


@app.route("/successfull_result", methods=['GET'])
def successful_result():
    return {"Result","Good, i buy your product",200}
@app.route("/failure_result", methods=['GET'])
def failure_result():
    return {"Result","Sorry, i don't buy your product",400}



6
def create_payment(data):
    
    payment_data = {
    "payment_method_id": "pix",
    "transaction_amount": data["valor"],
	"installments": 1,
    "payer": {     
        "first_name":  data["nome"],
		"email": "matheus15sdl@gmail.com",
		"identification": {
			"type": "CPF",
			"number": data["cpf"]
	    },
  		"phone": {
				"area_code": "55",
				"number": data["numero"]
			}
    },
    "description": "Pix de " + data["nome"],
    "notification_url": "https://backend.botconversa.com.br/api/v1/webhooks-automation/catch/8476/24JR7uiXjkVY/"
    }
    return payment_data
@app.route("/")    
def hello():
    return "Hello World!"
app.run(port=5001, host='192.168.1.169', debug=False,ssl_context=("certificates/cert.pem", "certificates/key.pem"))




