import unittest
from run import create_app
import json

class TestApp(unittest.TestCase):
	def setUp(self):
		self.app = create_app('config')
		self.app = self.app.test_client()
		self.app.testing = True

	def testEmptyDb(self):
	    response = self.app.get('/api/Observation')

	    assert len(json.loads(response.data)["data"]) == 0  

	def testStoreOneObservation(self):
		data = json.dumps({"thingId": "001", "name": "thermostat", "timestamp": "1", "data": {"heat": "5"}},sort_keys=True)		
		response = self.app.post('/api/Observation', data = data, content_type='application/json')
		response = self.app.get('/api/Observation')

		assert data == json.dumps(json.loads(response.data)["data"][0], sort_keys=True)

if __name__ == '__main__':
    unittest.main()
