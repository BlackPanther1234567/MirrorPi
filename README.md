# MirroPi | IoT-Based Smart Mirror using Raspberry Pi

An IoT-based Smart Mirror that displays:
- Real-time weather
- Class timetables
- Exam schedules
- Important college events

## Features
- Raspberry Pi configured as a local web server
- Python (Flask) backend
- JavaScript frontend with dynamic updates
- Weather API integration
- Customizable for different institutions

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/BlackPanther1234567/MirrorPi.git
   cd MirroPi
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python backend/app.py
   ```
4. Open `http://<raspberry-pi-ip>:5000` in Chromium (in kiosk mode for mirror display).

## Author
Rakesh Kannan
