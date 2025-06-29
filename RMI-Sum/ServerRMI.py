import Pyro4
from Adder import Adder

# Start the Pyro4 server and register the Adder object.
def start_server():
    adder = Adder()
    daemon = Pyro4.Daemon()
    uri = daemon.register(adder)
    ns = Pyro4.locateNS()
    ns.register("example.adder", uri)
    print(f"Server is running with URI: {uri}")
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()