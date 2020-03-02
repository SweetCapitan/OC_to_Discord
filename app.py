from flask import Flask
import requests
import os
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
url = os.environ.get('URL')


class Webhook(Resource):
    def get(self):
        pass

    def post(self):
        data = dict()
        parser = reqparse.RequestParser()
        parser.add_argument('author')
        parser.add_argument('text')
        params = parser.parse_args()
        data['username'] = params['author']
        data['content'] = params['author']
        req = requests.post(url, data=data)
        return 201

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(Webhook, "/webhook")
if __name__ == '__main__':
    app.run(debug=True)
