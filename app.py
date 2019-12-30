from flask import Flask, render_template
from datetime import datetime
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/', methods=['GET'])
def index():
  response = requests.get(
      'https://api.darksky.net/forecast/439f4d9d27bbb7f513361d2e54644e83/53.20139,5.80859'
  ).json()
  if "currently" in response:
    response['currently']['time'] = datetime.utcfromtimestamp(
        response['currently']['time'])
  if "alerts" in response:
    for alert in response['alerts']:
      alert['time'] = datetime.utcfromtimestamp(alert['time'])
      alert['expires'] = datetime.utcfromtimestamp(alert['expires'])

  return render_template('index.html', data=response)


if __name__ == '__main__':
  app.run()