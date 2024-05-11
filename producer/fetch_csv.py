import shutil

def fetch_csv(local_path, save_path):
    # Copy the local CSV file to the specified save path
    shutil.copy(local_path, save_path)
    print(f"CSV file copied to {save_path}")

if __name__ == "__main__":
    # Local path to the CSV file
    local_csv_path = "data/data.csv"
    
    # Path to save the CSV file
    save_path = "data/data.csv"
    
    # Fetch the CSV file
    fetch_csv(local_csv_path, save_path)
