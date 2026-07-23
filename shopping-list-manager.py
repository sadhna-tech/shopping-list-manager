import os

FILE_NAME = "shopping_list.txt"


def load_items():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_items(items):
    with open(FILE_NAME, "w") as file:
        for item in items:
            file.write(item + "\n")


shopping_list = load_items()


while True:
    print("\n===== Shopping List Manager =====")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear List")
    print("5. Save List")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        if shopping_list:
            print("\nShopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("\nShopping list is empty.")

    elif choice == "2":
        item = input("Enter item: ").strip()

        if item:
            shopping_list.append(item)
            print("Item added successfully!")
        else:
            print("Item cannot be empty.")

    elif choice == "3":
        if shopping_list:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

            try:
                item_number = int(input("Enter item number to remove: "))

                if 1 <= item_number <= len(shopping_list):
                    removed = shopping_list.pop(item_number - 1)
                    print(f"{removed} removed successfully!")
                else:
                    print("Invalid item number.")

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Shopping list is empty.")

    elif choice == "4":
        shopping_list.clear()
        print("Shopping list cleared.")

    elif choice == "5":
        save_items(shopping_list)
        print("Shopping list saved successfully!")

    elif choice == "6":
        save_items(shopping_list)
        print("Shopping list saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")