import os
import pandas as pd

def save_to_excel(data, folder="dataset", resource_name="wpsup", start_date="2020-01-01", end_date="2025-01-01"):
    if not data:
        print("No data to save.")
        return

    os.makedirs(folder, exist_ok=True)
    file_name = f"{folder}/{resource_name}_{start_date}_to_{end_date}.xlsx"

    df = pd.DataFrame(data["response"]["data"])
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name}")

if __name__ == "__main__":
    from retrieve_data import retrieve_data

    try:
        data = retrieve_data()
        save_to_excel(data, start_date="2020-01-01", end_date="2025-01-01")
    except Exception as e:
        print(f"An error occurred: {e}")
