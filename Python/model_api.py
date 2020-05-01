from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Config(Resource):
    def __init__(self):
        pass

    # Load config file
    def get(self):
        self.fil = request.args
        path = self.fil['file']        
        
        with open(path) as f:
            var = f.read()
        print('File read: ' + path)

        return var

    # Save config file
    def post(self):
        self.fil = request.args
        path = self.fil['file']
        data = request.data
        dec_data = data.decode()
        
        with open(path, 'w') as g:
            for element in dec_data:
                g.write(element)

api.add_resource(Config, '/conf')

if __name__ == '__main__':
    app.run(debug=True)