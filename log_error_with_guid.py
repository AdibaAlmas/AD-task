import requests

# Function to fetch a GUID from the API
def get_guid():
    url = "https://www.uuidtools.com/api/generate/v1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip('"')  # Extract the GUID from the response
    else:
        return None

# Function to log invalid file entries with a GUID
def log_invalid_file_with_guid(file_path, reason):
    guid = get_guid()
    if guid:
        print(f"Error logged: {guid} - Invalid file: {file_path}, Reason: {reason}")
    else:
        print(f"Failed to generate GUID for file: {file_path}")

# Example usage
log_invalid_file_with_guid("path/to/your_file.csv", "Missing required column")
