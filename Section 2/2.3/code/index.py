from flask import Flask
from flask import render_template
import os
import json
import time
import urllib2

app = Flask(__name__)

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=London&cnt=10&mode=json&units=metric"
    response = urllib2.urlopen(url).read()
    return response

@app.route("/")
def index():
    data = json.loads(get_weather())
    forecast_list = []
    for d in data.get("list"):
        day = time.strftime('%d %B', time.localtime(d.get('dt')))
        mini = d.get("temp").get("min")
        maxi = d.get("temp").get("max")
        description = d.get("weather")[0].get("description")
        forecast_list.append((day,mini,maxi,description))
    return render_template("index.html", forecast_list=forecast_list)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)