import Pyro4

@Pyro4.expose
class GreetService(object):
    # Respond to a client message with a greeting.
     def greet(self, message):
        if message.lower() == "hello":
            return "Hello! Server received your message. How can I assist you today?"
        return "Sorry, I only respond to 'hello'."