def check_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False

cards = input().split()
command = input()

number_of_rounds = 0
while not command == "end" and cards:
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)

    number_of_rounds += 1

    if check_index_is_valid(index_1, len(cards)) and check_index_is_valid(index_2, len(cards)) and not index_1 == index_2:
        el_1 = cards[index_1]
        el_2 = cards[index_2]
        if el_1 == el_2:
            cards.remove(el_1)
            cards.remove(el_2)
            print(f"Congrats! You have found matching elements - {el_1}!")
        else:
            print("Try again!")
    else:
        element_to_add = f"-{number_of_rounds}a"
        middle = len(cards) // 2
        cards.insert(middle, element_to_add) #заради средата се вкарва отляво и отдясно
        cards.insert(middle, element_to_add) #заради средата се вкарва отляво и отдясно
        print("Invalid input! Adding additional elements to the board")

    command = input()

if not cards:
    print(f"You have won in {number_of_rounds} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(cards))
