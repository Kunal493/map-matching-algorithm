# app.py
from flask import Flask, request, jsonify, render_template
from classify_road import classify_road, load_road_segments

app = Flask(__name__)

# Load road segments data
road_segments = load_road_segments('road_segments.csv')

@app.route("/")
def home():
    return render_template('map.html')

@app.route("/submit_coordinates", methods=['POST'])
def submit_coordinates():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Classify the road type based on GPS coordinates
    road_type = classify_road((latitude, longitude), road_segments)
    print(f"Vehicle is on a {road_type}")
    
    return jsonify({'status': 'success', 'road_type': road_type})

if __name__ == "__main__":
    app.run(debug=True, port=8000)