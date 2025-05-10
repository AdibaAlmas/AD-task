import os

from validate_csv import FileProcessorFactory
from validate_csv import FileProcessorFactory, log_invalid_file, store_valid_file


def show_menu():
    print("\nSelect an option:")
    print("1. Start File Validation")
    print("2. View Invalid Files Log")
    print("3. Exit")

def start_validation(directory_path):
    print("\nStarting file validation...")
    # Here we loop over the files and validate them
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
        else:
            print(f"Skipping non-CSV file: {file_name}")

def view_invalid_log():
    print("\nInvalid Files Log:")
    try:
        with open("invalid_files_log.txt", "r") as file:
            logs = file.readlines()
            if logs:
                for log in logs:
                    print(log.strip())
            else:
                print("No invalid files logged.")
    except FileNotFoundError:
        print("No invalid files log found.")

def main():
    # Path to the directory containing CSV files
    directory_path = "C:/Users/miraq/OneDrive/Desktop/AD task 1/ftp_data/"

    while True:
        show_menu()
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            start_validation(directory_path)
        elif user_choice == "2":
            view_invalid_log()
        elif user_choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
