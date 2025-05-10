import csv

# Function to generate a good CSV file
def generate_good_csv(file_name):
    headers = ["trial_id", "patient_id", "drug_name", "dose", "start_date", "end_date"]
    rows = [
        ["T001", "P001", "Aspirin", "500mg", "2023-05-01", "2023-05-05"],
        ["T002", "P002", "Paracetamol", "300mg", "2023-06-10", "2023-06-15"]
    ]

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Good CSV file '{file_name}' created.")

# Function to generate a bad CSV file
def generate_bad_csv(file_name):
    headers = ["trial_id", "patient_id", "drug_name", "dose"]
    rows = [
        ["T001", "P001", "Aspirin", "500mg"],
        ["T002", "P002", "Paracetamol", "300mg"]
    ]

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Bad CSV file '{file_name}' created.")

# Generate the files
generate_good_csv("good_sample.csv")
generate_bad_csv("bad_sample.csv")
