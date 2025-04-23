import json
from geopy.distance import geodesic

with open("path_coords.json", "r") as f:
    waypoints = [tuple(coord) for coord in json.load(f)]


with open("pireps.json", "r") as f:
    raw_pireps = json.load(f)

# store PIREPS in array
arp_reports = []
for report in raw_pireps:
    if "lat" in report and "lon" in report:
        report["coordinates"] = (report["lat"], report["lon"])
        arp_reports.append(report)

# PIREPs in 50 mile radius
MAX_NM = 50
nearby_arp = []
for report in arp_reports:
    for wp in waypoints:
        if geodesic(wp, report["coordinates"]).nautical <= MAX_NM:
            nearby_arp.append(report)
            break

# Output to json
with open("nearby_pireps.json", "w") as out_file:
    json.dump(nearby_arp, out_file, indent=2)

print(f"✅ Saved {len(nearby_arp)} PIREP reports within {MAX_NM} NM to 'nearby_pireps.json'")
