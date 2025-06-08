# shopping_list_manager.py

def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")

        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print(f"{item} not found in the list.")

        elif choice == "3":
            print("Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
