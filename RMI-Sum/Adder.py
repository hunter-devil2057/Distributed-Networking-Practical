import Pyro4

@Pyro4.expose
class Adder(object):
      # Add two numbers and return the result.
      def add(self, x, y):
          return x + y