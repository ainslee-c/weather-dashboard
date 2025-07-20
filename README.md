# Swift Weather Dashboard 🌦️✨

A Taylor Swift-themed weather dashboard app built with Flask and containerized with Docker. This project demonstrates basic DevOps concepts including containerization, environment variables, and API integration.

![Weather Dashboard Preview](https://via.placeholder.com/600x400?text=Swift+Weather+Dashboard)

## Features

- ☁️ Real-time weather data from OpenWeatherMap API
- 🌡️ Current temperature, wind speed, and humidity
- 🎨 Taylor Swift-inspired design elements
- 🔄 Auto-refreshes every 5 minutes
- 📱 Responsive design that works on desktop and mobile
- 🎵 Weather messages with Taylor Swift-inspired themes

## Technologies Used

- **Flask**: Python web framework
- **Docker**: Containerization
- **HTML/CSS**: Frontend design
- **OpenWeatherMap API**: Weather data
- **Environment Variables**: Secure API key storage

## Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional, for containerization)
- OpenWeatherMap API key (free tier)

### Installation

1. Clone this repository: git clone https://github.com/ainslee-c/weather-dashboard.git
cd weather-dashboard
2. Create a virtual enviornment and install dependencies:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask requests python-dotenv
3. Create a '.env' file in the project root with your API key: 
WEATHER_API_KEY=your_api_key_here
WEATHER_CITY=Your_City_Name

### Running the Application

### Without Docker: 
python app.py

Visit `http://localhost:5002` in your browser.

#### With Docker:
Build the Docker Image: docker build -t weather-dashboard
Run the container: docker run -p 5002:5002--env-file .env weather-dashboard
Visit `http://localhost:5002` in your browser.

## Project Structure

weather-dashboard/
├── app.py                 # Flask application
├── Dockerfile             # Docker configuration
├── .env                   # Environment variables (not in repo)
├── .gitignore             # Git ignore file
├── templates/             # HTML templates
│   └── index.html         # Main dashboard template
└── README.md              # This file
## Learning Outcomes

This project demonstrates several DevOps and software development concepts:

- Using environment variables for configuration
- API integration
- Containerization with Docker
- Web application development
- Version control with Git

## Future Enhancements

- Add 5-day forecast
- Implement more dynamic Taylor Swift era theming based on weather
- Add unit tests
- Set up CI/CD pipeline
- Add geolocation to automatically detect user's location

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenWeatherMap for the weather data API
- Flask for the web framework
- Taylor Swift for the inspiration

---

Created with 💖 as a learning project for DevOps concepts. 
