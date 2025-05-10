import os
import logging
import csv
import random
import uuid
import shutil
import datetime
from datetime import timedelta
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

# Set up logging for invalid files
logging.basicConfig(
    filename='invalid_files.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Function to generate random dates
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Function to create CSV with sample data
def create_csv(file_path):
    # Define column names
    fieldnames = ["trial_id", "patient_id", "drug_name", "dose", "start_date", "end_date"]
    
    # Sample data (you can expand this)
    drug_names = ["DrugA", "DrugB", "DrugC"]
    doses = ["50mg", "25mg", "100mg"]
    
    # Define the date range for the trial start and end dates
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)
    
    # Create a CSV file with the specified path
    with open(file_path, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Generate 10 rows of data
        for trial_id in range(1, 11):
            patient_id = random.randint(100, 999)
            drug_name = random.choice(drug_names)
            dose = random.choice(doses)
            trial_start_date = generate_random_date(start_date, end_date).strftime('%Y-%m-%d')
            trial_end_date = generate_random_date(datetime.datetime.strptime(trial_start_date, '%Y-%m-%d'), end_date).strftime('%Y-%m-%d')
            
            row = {
                "trial_id": trial_id,
                "patient_id": patient_id,
                "drug_name": drug_name,
                "dose": dose,
                "start_date": trial_start_date,
                "end_date": trial_end_date
            }
            
            writer.writerow(row)
    
    print(f"CSV file '{file_path}' created successfully!")

# Function to validate the CSV file
def validate_csv(file_path):
    print(f"Validating file: {file_path}")
    required_columns = ["trial_id", "patient_id", "drug_name", "dose", "start_date", "end_date"]
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != required_columns:
                return False
            for row in reader:
                if not all(row[col] for col in required_columns):
                    return False
        return True
    except Exception as e:
        print(f"Error during validation: {e}")
        return False

# Function to log invalid files
def log_invalid_file(file_path, reason):
    unique_id = str(uuid.uuid4())
    log_file = "invalid_files_log.txt"
    with open(log_file, "a") as f:
        f.write(f"{unique_id} - Invalid file: {file_path}, Reason: {reason}\n")
    print(f"Logged invalid file with ID {unique_id}")

# Function to store valid files
def store_valid_file(original_path, filename):
    now = datetime.datetime.now()
    folder_path = now.strftime("valid_data/%Y/%m/%d/%H%M%S")
    os.makedirs(folder_path, exist_ok=True)
    dest_path = os.path.join(folder_path, filename)
    shutil.copy2(original_path, dest_path)
    print(f"Valid file stored at: {dest_path}")

# Abstract FileProcessor class
class FileProcessor(ABC):
    @abstractmethod
    def validate_file(self, file_path):
        pass

    @abstractmethod
    def process_file(self, file_path):
        pass

# CSVFileProcessor implementation
class CSVFileProcessor(FileProcessor):
    def validate_file(self, file_path):
        print(f"Validating CSV file: {file_path}")
        
        required_columns = ["trial_id", "patient_id", "drug_name", "dose", "start_date", "end_date"]
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                if reader.fieldnames != required_columns:
                    return False
                for row in reader:
                    if not all(row[col] for col in required_columns):
                        return False
            return True
        except Exception as e:
            print(f"Error validating CSV file: {e}")
            return False

    def process_file(self, file_path):
        print(f"Processing CSV file: {file_path}")
        store_valid_file(file_path, os.path.basename(file_path))
        return True

# XMLFileProcessor implementation
class XMLFileProcessor(FileProcessor):
    def validate_file(self, file_path):
        print(f"Validating XML file: {file_path}")
        
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            required_elements = ["trial_id", "patient_id", "drug_name", "dose", "start_date", "end_date"]
            for elem in required_elements:
                if root.find(elem) is None:
                    return False
            return True
        except Exception as e:
            print(f"Error validating XML file: {e}")
            return False

    def process_file(self, file_path):
        print(f"Processing XML file: {file_path}")
        return True

# Factory for creating file processors
class FileProcessorFactory:
    @staticmethod
    def get_file_processor(file_type: str) -> FileProcessor:
        if file_type == "csv":
            return CSVFileProcessor()
        elif file_type == "xml":
            return XMLFileProcessor()
        else:
            raise ValueError(f"Unknown file type: {file_type}")

# Main logic to validate, log, and store files in a directory
directory_path = "C:/Users/miraq/OneDrive/Desktop/AD task 1/ftp_data/"
for file_name in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file_name)
    if file_name.endswith('.csv'):  # Assuming you're validating CSV files
        processor = FileProcessorFactory.get_file_processor("csv")
        if processor.validate_file(file_path):
            print(f"CSV file '{file_name}' is valid ✅")
            processor.process_file(file_path)
        else:
            print(f"CSV file '{file_name}' is invalid ❌")
            reason = "Invalid format or missing required fields"
            log_invalid_file(file_path, reason)
