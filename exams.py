import json, os

def get_exam_schedule():
    path = os.path.join(os.path.dirname(__file__), '../exam_schedule.json')
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return {"error": "Exam schedule not found"}
