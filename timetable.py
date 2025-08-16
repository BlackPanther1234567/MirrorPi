import json, os

def get_timetable():
    path = os.path.join(os.path.dirname(__file__), '../timetable.json')
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return {"error": "Timetable not found"}
