total_price_without_taxes = 0
total_price_with_taxes = 0
total_amount_of_taxes = 0
command = input()
while command != "special":
    if command == "regular":
        break
    price = float(command)
    total_price_without_taxes += price
    if price < 0:
        print("Invalid price!")
        total_price_without_taxes -= price
    command = input()
total_price_with_taxes = total_price_without_taxes * 1.2
total_amount_of_taxes = total_price_with_taxes - total_price_without_taxes

if command == "special":
    total_price_with_taxes = total_price_with_taxes * 0.9

if total_price_without_taxes != 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
else:
    print("Invalid order!")
