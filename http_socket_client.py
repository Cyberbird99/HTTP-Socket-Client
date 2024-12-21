import socket

print('creating socket...')
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
print('connecting to server')

# Modified variable names
server_address = "www.example.com"  # Host you want to connect to
server_port = 80  # Port for HTTP service

# Establish connection
socket_object.connect((server_address, server_port))
print('connection established')

# Create HTTP request
http_request = "GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % server_address  # Correct format
socket_object.send(http_request.encode())  # Send the request

# Receive response
response_data = socket_object.recv(4096)
print("Data:", response_data.decode())  # Decode the bytes to string
print("Length:", len(response_data))

# Closing the socket
print("closing socket")
socket_object.close()
