import csv

def process_csv(file_path):
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Read each row in the CSV file
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path = "data/data.csv"
    
    # Process the CSV file
    process_csv(csv_file_path)
