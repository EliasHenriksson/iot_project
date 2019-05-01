from flask import request
from flask_restful import Resource
from Model import db, Observation, ObservationSchema
import json

observations_schema = ObservationSchema(many=True)
observation_schema = ObservationSchema()

class ObservationResource(Resource):
    def get(self):
        observations = Observation.query.all()
        observations = observations_schema.dump(observations).data
        for observation in observations:
            observation['data'] = json.loads(observation['data'])
        
        return {'status': 'success', 'data': observations}, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = observation_schema.load(json_data)
        if errors:
            return errors, 422
        observation = Observation(
            thingId = json_data['thingId'], 
            name = json_data['name'],
            timestamp = json_data['timestamp'],
            data = json.dumps(json_data['data'])
            )
        

        db.session.add(observation)
        db.session.commit()

        result = observation_schema.dump(observation).data

        return { "status": 'success', 'data': result }, 201