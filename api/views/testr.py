from flask_restplus import Resource
from main import api

@api.route('/study')
class testR(Resource):
	def get(self):
		return 'workings'