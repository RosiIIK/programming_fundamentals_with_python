import re

number = int(input())

pattern = r"^(.+)>(?P<group_1>[0-9]{3})\|(?P<group_2>[a-z]{3})\|(?P<group_3>[A-Z]{3})\|(?P<group_4>[^<>]{3})<\1$"

for num in range(number):
    password = input()
    match_password = re.finditer(pattern, password)
    valid_matches = re.findall(pattern, password)
    encrypted_password = ""
    if valid_matches:
        for match in match_password:
            current_dict = match.groupdict()
            encrypted_password += current_dict['group_1'] + current_dict['group_2'] + current_dict['group_3'] + \
                                  current_dict['group_4']
            print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
