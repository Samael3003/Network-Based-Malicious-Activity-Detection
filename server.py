import socket
import csv
import subprocess

# Function to read the list of malicious URLs and programs from the CSV file
def read_malicious_list():
    malicious_list = []
    with open('malicious.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            malicious_list.append(row[0])
    return malicious_list

# Function to check if a URL or program is malicious
def is_malicious(input_str, malicious_list):
    for malicious_item in malicious_list:
        if malicious_item in input_str:
            return True
    return False

# Function to terminate a program (platform-independent)
def terminate_program(program_name):
    try:
        if platform.system() == 'Windows':
            subprocess.Popen(['taskkill', '/F', '/IM', program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.Popen(['pkill', program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(f"Error terminating program: {e}")

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Replace with your server's IP address
port = 12345  # Choose a suitable port number

server_socket.bind((host, port))
server_socket.listen(5)

malicious_urls_and_programs = read_malicious_list()

print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    data = client_socket.recv(1024).decode()
    print(f"Received data from client: {data}")
    
    if is_malicious(data, malicious_urls_and_programs):
        print("Malicious activity detected!")
        # For demonstration purposes, we'll just print a message.
        # You can replace this with code to terminate a program or block a website.
        print("Taking action...")

    client_socket.close()
