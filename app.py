from flask import Flask, request
from datetime import datetime
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class personalCapital(Resource):
    def get(self):
        return {'about':'Personal Capital data'}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku testing a commit</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

api.add_resource(personalCapital, '/test')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

