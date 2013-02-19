from pygame.draw import rect


class Peg():
    def __init__(self, surface, colorTuple, positionTuple, name):
        self.rectangle = rect(surface, colorTuple, positionTuple)
        self.discs = []
        self.name  = name

    def clear(self):
        del self.discs
