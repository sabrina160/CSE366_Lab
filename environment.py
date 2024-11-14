class Environment:
    #Class Initialization and Definition
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wrap_position(self, position):
        x, y = position 
        x = x % self.width
        y = y % self.height
        return [x, y]
