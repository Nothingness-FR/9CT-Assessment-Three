# main.py
from data_module import (
    load_dataset,
    clean_dataset,
    preview_dataset,
    plot_graph
)

def main():
    print("=== Data Science Project ===")
    print("1. Load global_temps.csv")
    print("2. Load disaster-events new.csv")
    choice = input("Choose dataset (1 or 2): ").strip()

    if choice == "1":
        dataset_name = "global_temps.csv"
    else:
        dataset_name = "disaster-events new.csv"

    df = load_dataset(dataset_name)

    while True:
        print("\n--- Menu ---")
        print("1. Preview dataset")
        print("2. Clean dataset")
        print("3. Create graph")
        print("4. Exit")
        option = input("Select (1-4): ").strip()

        if option == "1":
            preview_dataset(df)
        elif option == "2":
            df = clean_dataset(df)
        elif option == "3":
            plot_graph(df)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
