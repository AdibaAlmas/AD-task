import ftplib

# Function to connect to FTP server
def connect_ftp(server, username, password, directory=None):
    try:
        ftp = ftplib.FTP(server)
        ftp.login(username, password)
        print(f"Connected to FTP server: {server}")

        if directory:
            ftp.cwd(directory)
            print(f"Changed to directory: {directory}")

        return ftp
    except Exception as e:
        print("FTP connection failed:", e)
        return None

# Function to search for CSV files on FTP server
def search_csv_files(ftp):
    try:
        file_list = ftp.nlst()  # List all files in the current directory
        csv_files = [f for f in file_list if f.endswith('.csv')]  # Filter CSV files
        return csv_files
    except Exception as e:
        print("Error retrieving file list:", e)
        return []

# Main logic
if __name__ == "__main__":
    server = "127.0.0.1"  # FTP server IP (localhost if it's local)
    username = "user"  # FTP username
    password = "12345"  # FTP password
    directory = "AD Task 1/Data.csv"  # Directory inside FTP server

    # Connect to FTP server
    ftp = connect_ftp(server, username, password, directory)

    if ftp:
        # Get list of CSV files
        files = search_csv_files(ftp)
        print("CSV Files:")
        for f in files:
            print(f" - {f}")
        ftp.quit()  # Close the FTP connection



