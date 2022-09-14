message = input()
command = input()

while not command == "Reveal":
    command_split = command.split(":|:")
    if command_split[0] == "InsertSpace":
        index = int(command_split[1])
        first_part = message[:index]
        last_part = message[index:]
        message = first_part + " " + last_part
        print(message)
    elif command_split[0] == "Reverse":
        substring = command_split[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print("error")
    elif command_split[0] == "ChangeAll":
        substring = command_split[1]
        replacement = command_split[2]
        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")
