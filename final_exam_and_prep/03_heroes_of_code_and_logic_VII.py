heroes_number = int(input())
heroes = {}

for i in range(heroes_number):
    hero_info = input().split(" ")
    name = hero_info[0]
    hit_points = int(hero_info[1])
    mana_points = int(hero_info[2])
    heroes[name] = {"HP": hit_points, "MP": mana_points}

command = input()

while not command == "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        name = command[1]
        mana_points_needed = int(command[2])
        spell_name = command[3]
        if heroes[name]["MP"] >= mana_points_needed:
            heroes[name]["MP"] -= mana_points_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[name]["HP"] -= damage
        if heroes[name]["HP"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        name = command[1]
        recharge_amount = int(command[2])
        if heroes[name]["MP"] + recharge_amount >= 200:
            refill_amount = 200 - heroes[name]["MP"]
            heroes[name]["MP"] = 200
        else:
            heroes[name]["MP"] += recharge_amount
            refill_amount = recharge_amount
        print(f"{name} recharged for {abs(refill_amount)} MP!")
    elif command[0] == "Heal":
        name = command[1]
        heal_amount = int(command[2])
        if heroes[name]["HP"] + heal_amount >= 100:
            amount_recovery = 100 - heroes[name]["HP"]
            heroes[name]["HP"] = 100
        else:
            heroes[name]["HP"] += heal_amount
            amount_recovery = heal_amount
        print(f"{name} healed for {amount_recovery} HP!")
    command = input()

for hero, skills in heroes.items():
    print(f"{hero}")
    print(f'  HP: {heroes[hero]["HP"]}')
    print(f'  MP: {heroes[hero]["MP"]}')
