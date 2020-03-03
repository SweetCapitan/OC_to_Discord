from flask import Flask
import requests
import os
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
url = os.environ.get('URL')
message = {}


class Webhook(Resource):

    def get(self):
        if message is None:
            return 204
        else:
            return message[0]

    def post(self):
        data = dict()
        parser = reqparse.RequestParser()
        parser.add_argument('author')
        parser.add_argument('text')
        params = parser.parse_args()
        data['username'] = params['author']
        data['content'] = params['text']
        req = requests.post(url, data=data)
        return 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message')
        params = parser.parse_args()
        message[0] = params['message']
        return 201

    def delete(self):
        pass


api.add_resource(Webhook, "/webhook")
if __name__ == '__main__':
    app.run(debug=True)
