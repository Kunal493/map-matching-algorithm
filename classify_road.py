import math
import csv

def deg2rad(deg):
    return deg * (math.pi / 180)

def point_to_line_distance(x0, y0, x1, y1, x2, y2):
    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    if denominator == 0:  # To avoid division by zero
        return float('inf')
    return numerator / denominator

def find_closest_road(gps_coords, road_segments):
    min_distance = float('inf')
    closest_road = None
    
    for road in road_segments:
        start_point = (road['start_lat'], road['start_lon'])
        end_point = (road['end_lat'], road['end_lon'])
        distance = point_to_line_distance(gps_coords[0], gps_coords[1], 
                                          start_point[0], start_point[1], 
                                          end_point[0], end_point[1])
        
        if distance < min_distance:
            min_distance = distance
            closest_road = road
    
    return closest_road

def classify_road(gps_coords, road_segments):
    closest_road = find_closest_road(gps_coords, road_segments)
    
    if closest_road:
        return closest_road['type']
    return "Unknown"

def load_road_segments(csv_file):
    road_segments = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            road_segment = {
                'type': row['type'],
                'start_lat': float(row['start_lat']),
                'start_lon': float(row['start_lon']),
                'end_lat': float(row['end_lat']),
                'end_lon': float(row['end_lon'])
            }
            road_segments.append(road_segment)
    return road_segments
