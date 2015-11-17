import pprint
import requests
import json

class json_wrapper:

    json_res = ""
    json_body = ""
    json_url = ""

    def post_get(self):

        response = requests.post(
        'http://172.20.2.20:5000/v2.0/tokens',
        data=json.dumps({'auth':{'tenantName': 'admin','passwordCredentials':{'username':'admin','password':'admin'}}}),
        headers={'Content-Type': 'application/json'})

        data = json.load(response.json())

        pprint.pprint(data['access'])