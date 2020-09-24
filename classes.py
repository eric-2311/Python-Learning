
#Sample class in Python
class AngryBird():
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_vertical(self, delta):
        self.y += delta


bird = AngryBird()
print(bird.x, bird.y)
bird.move_vertical(3)
print(bird.x, bird.y)