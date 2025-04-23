import json
from geopy.distance import geodesic
from geopy import Point
import math

def flight_coordinates(start_coord, end_coord, interval_km=100):
    from geographiclib.geodesic import Geodesic

    geod = Geodesic.WGS84
    line = geod.InverseLine(start_coord[0], start_coord[1], end_coord[0], end_coord[1])
    
    num_points = int(line.s13 // (interval_km * 1000))
    coords = []

    for i in range(num_points + 1):
        s = i * interval_km * 1000
        pos = line.Position(s)
        coords.append((pos['lat2'], pos['lon2']))

    if coords[-1] != end_coord:
        coords.append(end_coord)

    return coords

start = (40.6413, -73.7781)  # JFK Airport
end = (51.4700, -0.4543)     # Heathrow Airport

path_coords = flight_coordinates(start, end)

# Output
with open('path_coords.json', 'w') as f:
    json.dump(path_coords, f, indent=4)
