import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server on localhost and port 12345
client_socket.connect(('localhost', 12345))

# Send a message
message = "Hello Server, this is Client."
client_socket.send(message.encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close the connection
client_socket.close()
