cart = []

#infinte loop until the user enter checkout
while True:
    print("-----\Cart details-----")
    print("1. Add item")
    print("2. View item")
    print("3. Remove item")
    print("4. Checkout")

    choice = int(input("Enter the choice(1-4):"))
    if choice == 1:
        print("\nAdd your item")
        items = input("Enter your item:")
        cart.append(items)
        print("Your items are added")

    elif choice == 2:
        print("your items")
        if len(cart) == 0:
            print("no item present in it")
        else:
            for i, item in enumerate(cart, 1):
                print(f"{i}:{item}")

    elif choice == 3:
        name = input("Enter the item to remove:")
        cart.remove(name)
        print("Item removed successfully!")

    elif choice == 4:
        print(f"you purchased {len(cart)} items")
        print("your items are",cart)
        exit()
    else:
        print("Invalid input")