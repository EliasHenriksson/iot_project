# IoT project
This a simple solution written in Python using the Flask and SQLAlchemy framework combined with an in memory SQLite database.
The observations can be stored with a POST request to `/api/Observation` of the following form
```
{
  "thingId": string,
  "name": string,
  "timestamp": int,
  "data": {}
}
```

# Run the app
If we want to use a virtual environment we can create one with

`virtualenv -p python3 env`

and activate it with

`source env/bin/activate`

Install the required packages with

`pip install -r requirements.txt`

and start the app with

`python run.py`

There are a few unit tests. We can be run them with

`python test_app.py`
