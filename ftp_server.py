
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    authorizer = DummyAuthorizer()
    # Creates a user with username "user", password "12345", with full permissions
    authorizer.add_user("user", "12345", "./ftp_data", perm="elradfmwMT")
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define the address and port
    server = FTPServer(("127.0.0.1", 2121), handler)
    print("FTP Server running at ftp://127.0.0.1:2121")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
