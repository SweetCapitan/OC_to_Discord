from flask import Flask
import requests
import os
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
url = os.environ.get('URL')


class Webhook(Resource):
    def get(self):
        pass

    def post(self, text):
        data = dict()
        data['username'] = 'Minecraft-to-Discord'
        data['content'] = text
        req = requests.post(url, data=data)
        return 201

    def put(self):
        pass

    def delete(self):
        pass



api.add_resource(Webhook, "/webhook", "/webhook/", "/webhook/<text>")
if __name__ == '__main__':
    app.run(debug=True)
