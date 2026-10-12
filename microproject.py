inventory_list = []
print("=============================================")
print("        Product Stock Inventory Register     ")
print("=============================================")
while True:
    print("\n--- MAIN MENU ---")
    print("1. Add Product Item")
    print("2. Display Inventory Report")
    print("3. Clear All Records")
    print("4. Exit Program")
    choice = input("\nEnter your choice (1-4): ").strip()
    if choice == "1":
        print("\n--- Add New Item ---")
        item_name = input("Enter Product Name: ").strip()
        quantity_str = input("Enter Stock Quantity: ").strip()
        if not item_name or not quantity_str:
            print("Error: Both fields are mandatory.")
            continue
        try:
            quantity_val = int(quantity_str)
            if quantity_val < 0:
                print("Error: Quantity cannot be negative.")
                continue
        except ValueError:
            print("Error: Quantity must be a whole number.")
            continue
        if quantity_val < 10:
            status = "REORDER"
        else:
            status = "SUFFICIENT"
        product_record = [item_name, quantity_val, status]
        inventory_list.append(product_record)
        print(f"Success: Item '{item_name}' saved.") 
    elif choice == "2":
        print("\n=============================================")
        print(f"{'Product Name':<15} | {'Quantity':<12} | {'Stock Status':<12}")
        print("---------------------------------------------")
        if len(inventory_list) == 0:
            print("        No items found in memory.            ")
        else:
            for item in inventory_list:
                print(f"{item[0]:<15} | {item[1]:<12} | {item[2]:<12}")
        print("=============================================")
    elif choice == "3":
        inventory_list.clear()
        print("Memory reset successful. All records removed.")
    elif choice == "4":
        print("\nExiting program. Execution terminated.")
        break
    else:
        print("Invalid choice. Enter a number between 1 and 4.")
