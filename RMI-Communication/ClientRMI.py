import Pyro4
# Start the client and communicate with the remote GreetService object.
def start_client():
    ns = Pyro4.locateNS()
    uri = ns.lookup("example.greet")
    greet_service = Pyro4.Proxy(uri)
      
    message = "hello"
    print(f"Client sending: {message}")
    response = greet_service.greet(message)
    print(f"Server response: {response}")  
    # Test with a different message
    message = "hi"
    print(f"Client sending: {message}")
    response = greet_service.greet(message)
    print(f"Server response: {response}")

if __name__ == "__main__":
    start_client()