import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

print("Calling remote 'add' method...")
result = proxy.add(5, 3)
print("Result of add(5, 3):", result)

print("Calling remote 'subtract' method...")
result = proxy.subtract(10, 4)
print("Result of subtract(10, 4):", result)
