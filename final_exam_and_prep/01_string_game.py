def change_command(f_input_line, f_command):
    char = f_command[1]
    replacement = f_command[2]
    f_input_line = f_input_line.replace(char, replacement)
    print(f_input_line)
    return f_input_line


def includes_command(f_input_line, f_command):
    substring = f_command[1]
    if substring in f_input_line:
        print("True")
    else:
        print("False")
    return f_input_line


def end_command(f_input_line, f_command):
    substring = f_command[1]
    if f_input_line.endswith(substring):
        print("True")
    else:
        print("False")
    return f_input_line


def uppercase_command(f_input_line):
    f_input_line = f_input_line.upper()
    print(f_input_line)
    return f_input_line


def find_index_command(f_input_line, f_command):
    char = f_command[1]
    if char in f_input_line:
        index = f_input_line.index(char)
        print(index)
    return f_input_line


def cut_command(f_input_line, f_command):
    start_index = int(f_command[1])
    count = int(f_command[2])
    end_index = start_index + count
    f_input_line = f_input_line[start_index:end_index]
    print(f_input_line)
    return f_input_line


input_line = input()
command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "Change":
        input_line = change_command(input_line, command)
    elif command[0] == "Includes":
        input_line = includes_command(input_line, command)
    elif command[0] == "End":
        input_line = end_command(input_line, command)
    elif command[0] == "Uppercase":
        input_line = uppercase_command(input_line)
    elif command[0] == "FindIndex":
        input_line = find_index_command(input_line, command)
    elif command[0] == "Cut":
        input_line = cut_command(input_line, command)
    command = input()
