choice = 0
while choice != 5:
    print(f"-- IMS🐍🐍🐍🐍💩  🍫 --")
    print(f"")
    print(f"1. Add a new item")
    print(f"2. Remove an item")
    print(f"3. Update an item")
    print(f"4. View all items")
    print(f"5. Exit")
    choice = int(input(f"Enter your choice: "))
    if choice == 1:
        print(f"Add a new item")
    elif choice == 2:
        print(f"Remove an item")
    elif choice == 3:
        print(f"Update an item")
    elif choice == 4:
        print(f"View all items")
    elif choice == 5:
        print(f"Exit")
    else:
        print(f"Invalid choice")
