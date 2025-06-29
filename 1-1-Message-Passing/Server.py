import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost on port 12345
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening on port 12345...")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive a message
data = conn.recv(1024).decode()
print(f"Received from client: {data}")

# Send response back
response = "Message received: " + data
conn.send(response.encode())

# Close the connection
conn.close()
