number_of_cars = int(input())
my_cars = {}

for _ in range(number_of_cars):
    car_info = input().split("|")
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    my_cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        needed_fuel = int(command[3])
        if my_cars[car]['fuel'] < needed_fuel:
            print(f"Not enough fuel to make that ride")
        elif my_cars[car]['fuel'] >= needed_fuel:
            my_cars[car]['mileage'] += distance
            my_cars[car]['fuel'] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if my_cars[car]['mileage'] >= 100000:
                del my_cars[car]
                print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car = command[1]
        refill = int(command[2])
        if my_cars[car]['fuel'] + refill >= 75:
            refill_diff = 75 - my_cars[car]['fuel']
            my_cars[car]['fuel'] += 75 - my_cars[car]['fuel']
            print(f"{car} refueled with {refill_diff} liters")
        else:
            my_cars[car]['fuel'] += refill
            print(f"{car} refueled with {refill} liters")
    elif command[0] == "Revert":
        car = command[1]
        revert_distance = int(command[2])
        my_cars[car]['mileage'] = my_cars[car]['mileage'] - revert_distance
        if my_cars[car]['mileage'] < 10000:
            my_cars[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {revert_distance} kilometers")

    command = input()

for car, qualities in my_cars.items():
        print(f"{car} -> Mileage: {my_cars[car]['mileage']} kms, Fuel in the tank: {my_cars[car]['fuel']} lt.")
