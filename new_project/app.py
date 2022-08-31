from flask import Flask
import datetime
from flask_restx import fields, Api, Resource

app = Flask(__name__)
api = Api(app)

model1 = api.model ('Model',{
    'timestamp':fields.String(Required=True),
    'temperature': fields.Integer,
    'note':fields.String
    
})

@api.route('/my-resource/<timestamp>,<temperature>,<note>', endpoint='my-resource')
@api.doc(params={'timestamp': 'an_timestamp','temperature':'temp','note':'desc'})
class MyResource(Resource):

    @api.doc(model=model1)
    def post(self, timestamp,temperature,note):
        return {
            'timestamp':timestamp,
            'temperature':temperature,
            'note':note
        }
        



if __name__ == '__main__':
    app.run(debug=True)