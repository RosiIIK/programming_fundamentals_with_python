input_info = input()
guests = {}

dislike_counter = 0
while not input_info == "Stop":
    guest_info = input_info.split("-")
    command = guest_info[0]
    name = guest_info[1]
    meal = guest_info[2]
    if command == "Like":
        if name not in guests:
            guests[name] = {'meal': [meal]}
        elif meal not in guests[name]['meal']:
            guests[name]['meal'].append(meal)
    elif command == "Dislike":
        if name not in guests:
            print(f"{name} is not at the party.")
        elif meal in guests[name]['meal']:
            dislike_counter += 1
            guests[name]['meal'].remove(meal)
            print(f"{name} doesn't like the {meal}.")
        else:
            print(f"{name} doesn't have the {meal} in his/her collection.")


    input_info = input()

for guest_name, meals in guests.items():
    print(f"{guest_name}: {', '.join(meals['meal'])}")

print(f"Unliked meals: {dislike_counter}")
