from ftplib import FTP

# Connect to the FTP server
ftp = FTP()
ftp.connect("127.0.0.1", 2121)  # Connect to your FTP server
ftp.login("user", "12345")     # Login credentials

# Set file paths
remote_file = "/MED_DATA_20230603140104.csv"  # Replace with your actual file name
local_file = "./ftp_data/MED_DATA_20230603140104.csv"  # Save location

# Download the file
with open(local_file, "wb") as f:
    ftp.retrbinary(f"RETR {remote_file}", f.write)

print(f"Downloaded file to {local_file}")

# Close the FTP connection
ftp.quit()
