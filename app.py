from flask import Flask, jsonify, render_template
from utils.weather_api import get_weather
from utils.timetable import get_timetable
from utils.exams import get_exam_schedule

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/weather')
def weather():
    return jsonify(get_weather())

@app.route('/api/timetable')
def timetable():
    return jsonify(get_timetable())

@app.route('/api/exams')
def exams():
    return jsonify(get_exam_schedule())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
