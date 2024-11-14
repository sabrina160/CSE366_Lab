class Agent:
    #Class Initialization and Definition
    def __init__(self, environment, x=0, y=0, speed=5): 
        self.environment = environment
        self.position = [x, y]
        self.speed = speed

    def move(self, direction):
        if direction == "up":
            self.position[1] -= self.speed
        elif direction == "down":
            self.position[1] += self.speed
        elif direction == "left":
            self.position[0] -= self.speed
        elif direction == "right":
            self.position[0] += self.speed

       
        self.position = self.environment.wrap_position(self.position)
    def get_position(self):
        return self.position
