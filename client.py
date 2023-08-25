import socket
import time
import pygetwindow as gw
import pyperclip

# Function to get the active browser window's title
def get_active_browser_title():
    active_window = gw.getActiveWindow()
    if active_window:
        return active_window.title
    return None

# Function to get the URL from the clipboard
def get_clipboard_url():
    clipboard_text = pyperclip.paste()
    if clipboard_text.startswith("http://") or clipboard_text.startswith("https://"):
        return clipboard_text
    return None

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'  # Replace with the server's IP address
server_port = 12345  # Use the same port as the server

try:
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    while True:
        active_title = get_active_browser_title()
        clipboard_url = get_clipboard_url()

        if active_title:
            print(f"Active Window Title: {active_title}")
            client_socket.send(active_title.encode())

        if clipboard_url:
            print(f"Clipboard URL: {clipboard_url}")
            client_socket.send(clipboard_url.encode())

        time.sleep(5)  # Adjust the sleep time as needed
except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
