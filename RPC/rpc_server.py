from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

server = SimpleXMLRPCServer(("localhost", 9000))
print("RPC Server listening on port 9000...")

server.register_function(add, "add")
server.register_function(subtract, "subtract")

server.serve_forever()