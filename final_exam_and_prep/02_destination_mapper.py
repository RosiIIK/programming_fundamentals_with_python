import re

places_string = input()
pattern = r'(=|/)(?P<place>[A-Z][a-zA-Z]+)\1'
places_match = re.finditer(pattern, places_string)

travel_points = 0
destinations = []

for place in places_match:
    object_dict = place.groupdict()
    destinations.append(object_dict['place'])
    travel_points += len(object_dict['place'])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
