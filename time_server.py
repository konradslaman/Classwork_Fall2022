from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/time", methods=["GET"])
def current_time():
    currentTime = datetime.now()
    strTime = datetime.strftime(currentTime, "%H:%M:%S")
    return strTime


@app.route("/date", methods=["GET"])
def current_date():
    currentDate = datetime.now()
    strDate = datetime.strftime(currentDate, "%m-%d-%y")
    return strDate


@app.route("/age", methods=["POST"])
def get_age():
    """
        incoming_json =  {"date": "10/21/2022",
                          "units": "years"}
    """
    in_data = request.get_json()
    date = in_data["date"].split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    givenDate = datetime(year, month, day)
    currentDate = datetime.now()
    difference = currentDate-givenDate
    return jsonify(float(difference.days)/365)


@app.route("/breakfast", methods=["GET"])
def till_breakfast():
    currentTime = datetime.now()
    currentHours = currentTime.hour + currentTime.minute/60
    currentHours += currentTime.second/3600
    breakfastTime = 8.0
    difference = breakfastTime - currentHours
    return jsonify(difference)


@app.route("/lunch", methods=["GET"])
def till_lunch():
    currentTime = datetime.now()
    currentHours = currentTime.hour + currentTime.minute/60
    currentHours += currentTime.second/3600
    lunchTime = 13.25
    difference = lunchTime - currentHours
    return jsonify(difference)


@app.route("/dinner", methods=["GET"])
def till_dinner():
    currentTime = datetime.now()
    currentHours = currentTime.hour + currentTime.minute/60
    currentHours += currentTime.second/3600
    dinnerTime = 20.5
    difference = dinnerTime - currentHours
    return jsonify(difference)


if __name__ == '__main__':
    app.run()
