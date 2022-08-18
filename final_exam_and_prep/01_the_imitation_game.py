encrypted_message = input()
instructions = input()

while not instructions == "Decode":
    instructions = instructions.split("|")
    if instructions[0] == "Move":
        move_letters = int(instructions[1])
        first_part = encrypted_message[:move_letters]
        last_part = encrypted_message[move_letters:]
        encrypted_message = last_part + first_part
    elif instructions[0] == "Insert":
        index = int(instructions[1])
        value = instructions[2]
        first_part = encrypted_message[:index]
        last_part = encrypted_message[index:]
        encrypted_message = first_part + value + last_part
    elif instructions[0] == "ChangeAll":
        substring = instructions[1]
        replacement_value = instructions[2]
        encrypted_message = encrypted_message.replace(substring, replacement_value)
    instructions = input()

print(f"The decrypted message is: {encrypted_message}")
