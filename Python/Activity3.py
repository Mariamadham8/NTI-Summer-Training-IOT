prod = {
    "cheese": 10,
    "Eggs": 5,
    "tomato": 10,
    "chiken": 40,
}

print("Welcome to Store :)")
print("======================")
print("Products Available:")

for key, value in prod.items():
    print(f"{key} : {value} EGP")
Cart = []
Quantity = []
while True:

    print("\nChoose Product:")
    name = input()

    if name not in prod:
        print("Product not available. Please choose again.")
        continue

    Cart.append(name)

    print("Choose Product Quantity:")
    num = int(input())
    Quantity.append(num)

    print("Do you want to quit? (yes/no)")
    ans = input()

    if ans.lower() == 'yes':
        TotalSum = 0
        print("\nYour Cart:")
        print("==========")
        for i in range(len(Cart)):
            product_name = Cart[i]
            qty = Quantity[i]
            price = prod[product_name]
            cost = qty * price
            print(f"{product_name} x {qty} = {cost} EGP")
            TotalSum += cost

        print(f"\nTotal Cost = {TotalSum} EGP")
        break
