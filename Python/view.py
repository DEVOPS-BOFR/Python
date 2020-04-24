from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Results(Resource):
    def post(self):
        result = request.data
        print(type(result))
        return render_template('result.html', result = result)

api.add_resource(Results, '/')

if __name__ == '__main__':
    app.run(debug = True)
else:
    app.run(port = 6000)