from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Menu Editor")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")

def add_item_to_menu():
    name = input("Enter the item's name: ")
    price = int(input("Enter the item's price: "))
    item = MenuItem(name, price)
    if item.save():
        print("Item was added successfully.")
    else:
        print("Error while adding item.")

def remove_item_from_menu():
    name = input("Enter the name of the item you want to remove: ")
    item = MenuItem(name, 0)
    if item.delete():
        print("Item was deleted successfully.")
    else:
        print("Error while deleting item.")

def update_item_from_menu():
    name = input("Enter the name of the item you want to update: ")
    price = int(input("Enter the new price: "))
    new_name = input("Enter the new name (or leave empty to keep the same): ")
    item = MenuItem(name, 0)
    if item.update(new_name or name, price):
        print("Item was updated successfully.")
    else:
        print("Error while updating item.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("Restaurant Menu:")
        for item in items:
            print(f"{item[1]} - ${item[2]}")
    else:
        print("The menu is empty.")

if __name__ == "__main__":
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "V":
            name = input("Enter the name of the item you want to view: ")
            item = MenuManager.get_by_name(name)
            if item:
                try:
                    print(f"Name: {item[0][1]}, Price: ${item[0][2]}")
                except IndexError as e:
                    print("Error: Item list structure is not as expected:", item)
            else:
                print("Item not found.")

        elif choice == "A":
            add_item_to_menu()

        elif choice == "D":
            remove_item_from_menu()

        elif choice == "U":
            update_item_from_menu()

        elif choice == "S":
            show_restaurant_menu()

        elif choice == "E":
            show_restaurant_menu()
            break

        else:
            print("Invalid choice. Please try again.")
