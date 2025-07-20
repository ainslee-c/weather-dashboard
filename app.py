from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Register template filter correctly
@app.template_filter('timestamp_to_time')
def timestamp_to_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def weather_dashboard():
    api_key = os.environ.get('WEATHER_API_KEY')
    if not api_key:
        return "Error: WEATHER_API_KEY not found in environment variables"
    
    # Default to New York if no city specified
    city = os.environ.get('WEATHER_CITY', 'New York')
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        weather_data = response.json()
        return render_template('index.html', weather=weather_data)
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)