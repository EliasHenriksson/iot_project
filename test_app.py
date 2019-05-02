import unittest
from run import create_app
import json

ENDPOINT = '/api/Observation'


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.app = self.app.test_client()
        self.app.testing = True

    def test_empty_db(self):
        response = self.app.get(ENDPOINT)

        assert len(json.loads(response.data)["data"]) == 0

    def create_json(self, nbr):
        data = {"thingId": str(nbr), "name": "thermostat", "timestamp": int(nbr), "data": {"heat": str(nbr)}}

        return json.dumps(data, sort_keys=True)

    def test_store_one_observation(self):
        data = self.create_json(1)
        self.app.post(ENDPOINT, data=data)
        response = self.app.get(ENDPOINT)

        assert data == json.dumps(json.loads(response.data)["data"][0], sort_keys=True)

    def test_store_multiple_observations(self):
        NBR_OF_OBSERVATIONS = 100

        for i in range(0, NBR_OF_OBSERVATIONS):
            self.app.post(ENDPOINT, data=self.create_json(i))

        response = self.app.get(ENDPOINT)

        assert len(json.loads(response.data)["data"]) == NBR_OF_OBSERVATIONS

    def test_store_json_without_thing_od(self):
        data = json.dumps({"name": "thermostat", "timestamp": 1, "data": {"heat": "3"}})
        response = self.app.post(ENDPOINT, data=data)

        if "422" not in response.status:
            assert True

    def test_store_json_with_extra_field(self):
        data = json.dumps({"name": "thermostat", "timestamp": 1, "data": {"heat": "3"}, "extraField": "2"})
        response = self.app.post(ENDPOINT, data=data)

        if "422" not in response.status:
            assert True


if __name__ == '__main__':
    unittest.main()
