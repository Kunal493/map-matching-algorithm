# Map-Matching Algorithm for Highway and Service Road Classification
This is demo version only.

## Project Overview
This project aims to develop a map-matching algorithm using AI-ML techniques to distinguish vehicular movement on highways and service roads. 
The algorithm is designed to handle intermittent GNSS position data and large biases in GNSS coordinates, making it suitable for applications such as GNSS-based tolling systems. 
The solution uses Flask for the backend, a simple HTML/JavaScript frontend for visualization, and Python for map-matching and classification.

## Features
Real-time vehicle tracking: Continuously tracks and displays the vehicle's position on a map.
Road classification: Uses map-matching techniques to classify whether the vehicle is on a highway or a service road.
Data visualization: Visualizes the vehicle's movement on an embedded Google Map.
AI-ML enhancement: Designed for future integration with AI-ML techniques to improve map-matching performance.

## Project Structure

├── app.py                  # Flask server for backend

├── classify_road.py        # Python module for road classification

├── templates

│   └── map.html            # Frontend HTML for displaying map and coordinates

├── road_segments.csv       # Demo CSV file containing road segments data

├── SystemArchitecture.jpeg # SystemArchitecture image

├── FlowChart.jpg           # FlowChart

└── README.md               # Project documentation

# Getting Started
## Prerequisites
Python 3.x
Flask
Basic knowledge of HTML, JavaScript, and Python

## Installation
# Clone the repository:
git clone https://github.com/Kunal493/map-matching-algorithm.git

## Install required Python packages:
pip install flask
Ensure you have the CSV file with road segments data:

A sample CSV file named road_segments.csv is provided with the project.
Running the Application
Start the Flask server:
python app.py
Access the application:

Open a web browser and navigate to http://localhost:8000 to view the map and start tracking.
Example CSV File
The CSV file road_segments.csv contains sample road segments data used for classification.

How It Works
Frontend (HTML/JavaScript):

Uses the Geolocation API to continuously fetch the user's current GPS coordinates.
Displays the vehicle's movement on a Google Map embedded in the page.
Sends GPS coordinates to the backend server every few seconds.
Backend (Flask):

Receives GPS coordinates from the frontend.
Uses a map-matching algorithm to classify whether the vehicle is on a highway or a service road.
Classification Module:

Loads road segment data from the CSV file.
Computes the closest road segment to the received GPS coordinates using geometric calculations.
Classifies the vehicle's position as either on a highway or a service road based on proximity to road segments.
Future Enhancements
Integration with machine learning models to improve accuracy in challenging conditions.
Expanding the road segments data to cover more regions.
Enhancing the frontend with more interactive and responsive map features.
Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.


