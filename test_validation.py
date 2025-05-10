import unittest
import csv
import os

# Define the function to validate CSV
def is_valid_csv(file_path):
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

# Define the test case class
class TestCSVValidation(unittest.TestCase):
    def test_valid_csv(self):
        # Create a sample valid CSV file in memory or temporary location for testing
        test_file = 'test_valid_file.csv'
        with open(test_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["trial_id", "patient_id", "drug_name", "dose", "start_date", "end_date"])
            writer.writeheader()
            writer.writerow({
                "trial_id": "1", 
                "patient_id": "A123", 
                "drug_name": "DrugA", 
                "dose": "100mg", 
                "start_date": "2023-01-01", 
                "end_date": "2023-01-10"
            })
        
        # Assert that the file is valid
        self.assertTrue(is_valid_csv(test_file))
        
        # Cleanup
        os.remove(test_file)

    def test_invalid_csv(self):
        # Create a sample invalid CSV file for testing
        test_file = 'test_invalid_file.csv'
        with open(test_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["trial_id", "patient_id", "drug_name", "dose", "start_date"])
            writer.writeheader()  # Missing 'end_date' column
            writer.writerow({
                "trial_id": "1", 
                "patient_id": "A123", 
                "drug_name": "DrugA", 
                "dose": "100mg", 
                "start_date": "2023-01-01"
            })
        
        # Assert that the file is invalid
        self.assertFalse(is_valid_csv(test_file))
        
        # Cleanup
        os.remove(test_file)

# Run the tests
if __name__ == "__main__":
    unittest.main()
