"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=None):
        self.start = self.new_start = start

    def generate(self):
        """ Generate serial sequentially """
        self.start += 1
        return self.start -1

    def reset(self):
        """ Reset number back to initial start """
        self.start = self.new_start
  