def is_index_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False

text = input()
command = input()

while not command == "End":
    split_command = command.split()
    if split_command[0] == "Translate":
        char = split_command[1]
        replacement_char = split_command[2]
        text = text.replace(char, replacement_char)
        print(text)
    elif split_command[0] == "Includes":
        substring = split_command[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif split_command[0] == "Start":
        substring = split_command[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")
    elif split_command[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif split_command[0] == "FindIndex":
        char = split_command[1]
        if char in text:
            index = text.rfind(char)
            print(index)
    elif split_command[0] == "Remove":
        start_index = int(split_command[1])
        count = int(split_command[2])
        if is_index_valid(start_index, text):
            first_part = text[:start_index]
            last_part = text[count+start_index:]
            text = first_part + last_part
            print(text)

    command = input()
