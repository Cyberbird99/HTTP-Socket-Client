# HTTP-Socket-Client

This Python script performs the following actions:

1. **Creates a socket**: Establishes a socket using the IPv4 address family and TCP protocol.
2. **Connects to a remote server**: Connects to `www.example.com` on port 80 (the standard HTTP port).
3. **Sends an HTTP GET request**: Sends a simple HTTP GET request to the server asking for the root (`/`) page.
4. **Receives server response**: Receives the server's response (up to 4096 bytes).
5. **Displays data**: Prints the received response data (HTML content of the page) and its length.
6. **Closes the connection**: Closes the socket connection after receiving the response.

In short, the code establishes a connection to a web server, sends an HTTP GET request, retrieves the response, and displays it.
