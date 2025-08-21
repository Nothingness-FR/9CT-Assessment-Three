# main.py
from data_module import (
    load_dataset,
    display_dataset_preview,
    display_visualisation,
    search_data,
    update_data_entry,
    save_changes,
)

def main_menu():
    # Load one dataset at the beginning (keeps it simple)
    load_dataset()

    while True:
        print("\n=== Data Viewer Interface (Simple) ===")
        print("1. View dataset (preview)")
        print("2. View visualisation")
        print("3. Search data (text contains)")
        print("4. Update a data entry (edit one cell)")
        print("5. Save changes to CSV")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            display_dataset_preview()
        elif choice == '2':
            display_visualisation()
        elif choice == '3':
            search_data()
        elif choice == '4':
            update_data_entry()
        elif choice == '5':
            save_changes()
            print("Changes saved.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
