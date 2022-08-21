def index_is_valid(index, text):
    if 0 <= index < len(text):
        return True
    return False

tour_stops = input()

while True:
    command = input().split(":")
    if command[0].startswith("Travel"):
        print(f"Ready for world tour! Planned stops: {tour_stops}")
        break
    elif command[0].startswith("Add"):
        index = int(command[1])
        string = command[2]
        if index_is_valid(index, tour_stops):
            left_side = tour_stops[:index]
            right_side = tour_stops[index:]
            tour_stops = left_side + string + right_side
            print(tour_stops)
        else:
            print(tour_stops)
    elif command[0].startswith("Remove"):
        start_index = int(command[1])
        end_index = int(command[2])
        if index_is_valid(start_index, tour_stops) and index_is_valid(end_index, tour_stops):
            tour_stops = tour_stops[:start_index] + tour_stops[end_index+1:]
            print(tour_stops)
        else:
            print(tour_stops)
    elif command[0].startswith("Switch"):
        old_string = command[1]
        new_string = command[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)
            print(tour_stops)
        else:
            print(tour_stops)
