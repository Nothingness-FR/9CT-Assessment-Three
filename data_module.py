import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")   # fixes macOS plot window issues




# ========= LOAD & CLEAN =========
def load_and_clean(disaster_file="disaster-events new.csv", climate_file="global_temps.csv"):
    global merged_df

    # Load datasets
    disasters_df = pd.read_csv(disaster_file)
    climate_df = pd.read_csv(climate_file)

    # Clean column names
    disasters_df.columns = disasters_df.columns.str.strip().str.title()
    climate_df.columns = climate_df.columns.str.strip().str.title()

    # Ensure Year column exists
    if "Year" not in disasters_df.columns or "Year" not in climate_df.columns:
        raise ValueError("Both datasets must contain a 'Year' column.")

    # Group by year and disaster type
    disasters_df = disasters_df.groupby(["Year", "Disaster_Type"], as_index=False).sum(numeric_only=True)

    # Group climate by year
    climate_df = climate_df.groupby("Year", as_index=False).mean(numeric_only=True)

    # Merge
    merged_df = pd.merge(disasters_df, climate_df, on="Year", how="inner")


# ========= PREVIEW =========
def display_dataset_preview():
    if merged_df is None:
        print("Data not loaded yet.")
        return
    print("\n=== Dataset Preview ===")
    print(merged_df.head(10))


# ========= VISUALISATION =========
def display_visualisation():
    if merged_df is None:
        print("Data not loaded yet.")
        return

    disaster_types = merged_df["Disaster_Type"].unique()
    print("\nAvailable disaster types:", ", ".join(disaster_types))
    choice = input("Enter a disaster type to plot (or 'all' for everything): ").strip().title()

    if choice != "All" and choice not in disaster_types:
        print("Invalid choice.")
        return

    climate_col = "Temperature" if "Temperature" in merged_df.columns else merged_df.columns[-1]

    if choice == "All":
        df = merged_df.groupby("Year", as_index=False).sum(numeric_only=True)
        disaster_col = "Count" if "Count" in df.columns else df.columns[1]
    else:
        df = merged_df[merged_df["Disaster_Type"] == choice]
        disaster_col = "Count" if "Count" in df.columns else df.columns[2]

    _, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df["Year"], df[climate_col], color="red", label="Global Temperature")
    ax1.set_ylabel("Temperature (°C)", color="red")
    ax1.tick_params(axis="y", labelcolor="red")

    ax2 = ax1.twinx()
    ax2.plot(df["Year"], df[disaster_col], color="blue", label=f"{choice} Disasters")
    ax2.set_ylabel("Number of Disasters", color="blue")
    ax2.tick_params(axis="y", labelcolor="blue")

    plt.title(f"Climate Change vs {choice} Disasters Over Time")
    plt.show()


# ========= COMPARE TWO DISASTERS =========
def compare_disasters():
    if merged_df is None:
        print("Data not loaded yet.")
        return

    disaster_types = merged_df["Disaster_Type"].unique()
    print("\nAvailable disaster types:", ", ".join(disaster_types))

    d1 = input("Enter the first disaster type: ").strip().title()
    d2 = input("Enter the second disaster type: ").strip().title()

    if d1 not in disaster_types or d2 not in disaster_types:
        print("Invalid disaster types entered.")
        return

    df1 = merged_df[merged_df["Disaster_Type"] == d1].set_index("Year")
    df2 = merged_df[merged_df["Disaster_Type"] == d2].set_index("Year")

    # Pick count column
    col1 = "Count" if "Count" in df1.columns else df1.columns[1]
    col2 = "Count" if "Count" in df2.columns else df2.columns[1]

    _, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df1.index, df1[col1], label=d1, color="blue")
    ax.plot(df2.index, df2[col2], label=d2, color="green")

    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Disasters")
    plt.title(f"Comparison of {d1} vs {d2} Disasters")
    plt.legend()
    plt.show()


# ========= SEARCH =========
def search_data():
    if merged_df is None:
        print("Data not loaded yet.")
        return

    year = input("Enter a year to filter by (or press Enter to skip): ").strip()
    disaster = input("Enter a disaster type to filter by (or press Enter to skip): ").strip().title()

    df = merged_df.copy()
    if year.isdigit():
        df = df[df["Year"] == int(year)]
    if disaster and disaster in df["Disaster_Type"].unique():
        df = df[df["Disaster_Type"] == disaster]

    print("\n=== Filtered Data ===")
    print(df if not df.empty else "No data found.")


# ========= SAVE =========
def save_changes():
    if merged_df is not None:
        merged_df.to_csv("cleaned_dataset.csv", index=False)
        print("Dataset saved as cleaned_dataset.csv")


# ========= MENU =========
def main_menu():
    load_and_clean()  # Load datasets at the start

    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View dataset")
        print("2. View visualisation (line graphs)")
        print("3. Compare two disaster types")
        print("4. Search or filter data")
        print("5. Save changes")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            display_dataset_preview()
        elif choice == '2':
            display_visualisation()
        elif choice == '3':
            compare_disasters()
        elif choice == '4':
            search_data()
        elif choice == '5':
            save_changes()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    merged_df = None
    main_menu()








