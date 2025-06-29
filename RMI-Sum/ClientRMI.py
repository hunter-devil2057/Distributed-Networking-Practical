import Pyro4

# Start the client and invoke methods on the remote Adder object.
def start_client():
    ns = Pyro4.locateNS()
    uri = ns.lookup("example.adder")
    adder = Pyro4.Proxy(uri)
    print("Testing remote adder method:")
    print(f"Add: 5 + 3 = {adder.add(5, 3)}")

if __name__ == "__main__":
    start_client()