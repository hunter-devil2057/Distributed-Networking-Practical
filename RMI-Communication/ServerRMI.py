import Pyro4
from GreetService import GreetService

# Start the Pyro4 server and register the GreetService object.
def start_server():
    greet_service = GreetService()
    daemon = Pyro4.Daemon()
    uri = daemon.register(greet_service)
    ns = Pyro4.locateNS()
    ns.register("example.greet", uri)
    print(f"Server is running with URI: {uri}")
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()