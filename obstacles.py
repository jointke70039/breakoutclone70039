#deklaracja przeszkody - 
import random

class Obstacle:
    total_obstacles = 0  # Class variable to track the total number of obstacles

    def __init__(self, x, y, width, height, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color if color is not None else (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        Obstacle.total_obstacles += 1  # Increment the total number of obstacles
        

obstacles = [
    Obstacle(20, 0, 50, 20),
    Obstacle(20, 30, 50, 20),
    Obstacle(20, 60, 50, 20),
    Obstacle(20, 90, 50, 20),

    Obstacle(80, 0, 50, 20),
    Obstacle(80, 30, 50, 20),
    Obstacle(80, 60, 50, 20),
    Obstacle(80, 90, 50, 20),

    Obstacle(140, 0, 50, 20),
    Obstacle(140, 30, 50, 20),
    Obstacle(140, 60, 50, 20),
    Obstacle(140, 90, 50, 20),

    Obstacle(200, 0, 50, 20),
    Obstacle(200, 30, 50, 20),
    Obstacle(200, 60, 50, 20),
    Obstacle(200, 90, 50, 20),

    Obstacle(260, 0, 50, 20),
    Obstacle(260, 30, 50, 20),
    Obstacle(260, 60, 50, 20),
    Obstacle(260, 90, 50, 20),

    Obstacle(320, 0, 50, 20),
    Obstacle(320, 30, 50, 20),
    Obstacle(320, 60, 50, 20),
    Obstacle(320, 90, 50, 20),

    Obstacle(380, 0, 50, 20),
    Obstacle(380, 30, 50, 20),
    Obstacle(380, 60, 50, 20),
    Obstacle(380, 90, 50, 20),

    Obstacle(440, 0, 50, 20),
    Obstacle(440, 30, 50, 20),
    Obstacle(440, 60, 50, 20),
    Obstacle(440, 90, 50, 20),

    Obstacle(500, 0, 50, 20),
    Obstacle(500, 30, 50, 20),
    Obstacle(500, 60, 50, 20),
    Obstacle(500, 90, 50, 20),

]