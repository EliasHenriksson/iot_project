import unittest
from run import create_app
import json

POST_END_POINT = '/api/Observation'
GET_END_POINT = '/api/Observation'

class TestApp(unittest.TestCase):
	def setUp(self):
		self.app = create_app('config')
		self.app = self.app.test_client()
		self.app.testing = True

	def testEmptyDb(self):
	    response = self.app.get(GET_END_POINT)

	    assert len(json.loads(response.data)["data"]) == 0  

	def testStoreOneObservation(self):
		data = json.dumps({"thingId": "001", "name": "thermostat", 
			"timestamp": 1, "data": {"heat": "5"}}, sort_keys=True)	
		response = self.app.post(POST_END_POINT, data = data, content_type='application/json')
		response = self.app.get(GET_END_POINT)

		assert data == json.dumps(json.loads(response.data)["data"][0], sort_keys=True)

	def testStoreManyObservations(self):
		NBR_OF_OBSERVATIONS_TO_STORE = 100

		for i in range(0, NBR_OF_OBSERVATIONS_TO_STORE):
			 	data = json.dumps({"thingId": str(i), "name": "thermostat", 
			 		"timestamp": i, "data": {"heat": str(i)}}, sort_keys=True)
			 	self.app.post(POST_END_POINT, data = data, content_type='application/json')

		response = self.app.get(GET_END_POINT)

		assert len(json.loads(response.data)["data"]) == NBR_OF_OBSERVATIONS_TO_STORE		

	def testStoreJsonWithoutThingId(self):
		data = json.dumps({"name": "thermostat", "timestamp": 1, "data": {"heat": "3"}})
		response = self.app.post(POST_END_POINT, data = data, content_type='application/json')
		
		if "422" not in response.status:
			assert True

	def testStoreJsonWithExtraField(self):
		data = json.dumps({"name": "thermostat", "timestamp": 1, "data": {"heat": "3"}, "extraField": "2"})
		response = self.app.post(POST_END_POINT, data = data, content_type='application/json')

		if "422" not in response.status:
			assert True

if __name__ == '__main__':
    unittest.main()
