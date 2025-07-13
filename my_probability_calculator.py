import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        # for color, count in kwargs.items():
        #     self.contents.extend([color] * count )
        self.contents.extend(color for color, value in kwargs.items() for _ in range(value))

    def draw(self, no_of_balls_drawn):
        if no_of_balls_drawn >= len(self.contents):
            all_balls = self.contents.copy()
            self.contents.clear()
            return all_balls
        
        balls_drawn = random.sample(self.contents, no_of_balls_drawn)
        for color in balls_drawn:
            self.contents.remove(color)
        return balls_drawn

def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):
    expected_outcome = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        if all(drawn.count(color) >= count for color, count in expected_balls.items()):
                expected_outcome += 1
    probability = float(expected_outcome / num_experiments)
    return probability
    
hat1 = Hat(blue=3, red=5, green=2)
probability = experiment(
        hat=hat1,
        expected_balls={'red':3,'green':2},
        num_balls_drawn=5,
        num_experiments=2000)
print(probability)