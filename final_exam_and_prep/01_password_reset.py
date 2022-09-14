data = input()

while True:
    command = input().split(" ")
    if command[0] == "Done":
        print(f"Your password is: {data}")
        break
    elif command[0] == "TakeOdd":
        data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
        print(data)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        left_side = data[:index]
        right_side = data[(index+length):]
        sliced_pass = left_side + right_side
        data = sliced_pass
        print(data)
    elif command[0] == "Substitute":
        substring = command[1]
        substitude = command[2]
        if substring in data:
            data = data.replace(substring, substitude)
            print(data)
        else:
            print("Nothing to replace!")
