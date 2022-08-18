def add_command(f_pieces_collection, f_command):
    f_piece = f_command[1]
    f_composer = f_command[2]
    f_key = f_command[3]
    if f_piece in f_pieces_collection:
        print(f"{f_piece} is already in the collection!")
    else:
        f_pieces_collection[f_piece] = {f_composer: f_key}
        print(f"{f_piece} by {f_composer} in {f_key} added to the collection!")
    return f_pieces_collection


def remove_command(f_pieces_collection, f_command):
    f_piece = f_command[1]
    if f_piece in f_pieces_collection:
        del f_pieces_collection[f_piece]
        print(f"Successfully removed {f_piece}!")
    else:
        print(f"Invalid operation! {f_piece} does not exist in the collection.")
    return f_pieces_collection


def change_key_command(f_pieces_collection, f_command):
    f_piece = f_command[1]
    f_new_key = f_command[2]
    if f_piece in f_pieces_collection:
        old_composer_key = f_pieces_collection.get(f_piece)
        old_composer = old_composer_key.keys()
        key_for_change = "".join(old_composer)
        f_pieces_collection[f_piece][key_for_change] = f_new_key
        print(f"Changed the key of {f_piece} to {f_new_key}!")
    else:
        print(f"Invalid operation! {f_piece} does not exist in the collection.")
    return f_pieces_collection


number = int(input())

pieces_collection = {}

for num in range(number):
    initial_command = input().split("|")
    piece = initial_command[0]
    composer = initial_command[1]
    piece_id = initial_command[2]
    pieces_collection[piece] = {composer: piece_id}

command = input()

while not command == "Stop":
    command = command.split("|")
    if command[0] == "Add":
        pieces_collection = add_command(pieces_collection, command)
    elif command[0] == "Remove":
        pieces_collection = remove_command(pieces_collection, command)
    elif command[0] == "ChangeKey":
        pieces_collection = change_key_command(pieces_collection, command)
    command = input()

for piece_id, composers in pieces_collection.items():
    for composer_id, keys in composers.items():
        print(f"{piece_id} -> Composer: {composer_id}, Key: {keys}")
