# data_module.py
import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file_path: str) -> pd.DataFrame:
    """Load CSV into a DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {file_path} with {len(df)} rows and {len(df.columns)} columns.")
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return pd.DataFrame()

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Simple cleaning: drop empty rows, fix column names"""
    if df.empty:
        print("No data loaded.")
        return df
    df = df.dropna(how="all")  # drop empty rows
    df.columns = [c.strip().replace(" ", "_").lower() for c in df.columns]
    print("Dataset cleaned. Empty rows removed, column names simplified.")
    return df

def preview_dataset(df: pd.DataFrame, n: int = 5):
    """Show first rows of dataset"""
    if df.empty:
        print("No data to preview.")
        return
    print("\n--- Preview ---")
    print(df.head(n))

def plot_graph(df: pd.DataFrame):
    """Plot a simple graph:
       - If 'year' exists, line plot year vs first numeric column.
       - Otherwise, scatter plot two numeric columns."""
    if df.empty:
        print("No data to plot.")
        return

    # Try line plot if year column exists
    year_col = None
    for col in df.columns:
        if "year" in col:
            year_col = col
            break

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if year_col and numeric_cols:
        plt.plot(df[year_col], df[numeric_cols[0]])
        plt.xlabel(year_col)
        plt.ylabel(numeric_cols[0])
        plt.title(f"{numeric_cols[0]} over {year_col}")
    elif len(numeric_cols) >= 2:
        plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
        plt.xlabel(numeric_cols[0])
        plt.ylabel(numeric_cols[1])
        plt.title(f"{numeric_cols[1]} vs {numeric_cols[0]}")
    else:
        print("Not enough numeric data to plot.")
        return

    plt.tight_layout()
    plt.show()
