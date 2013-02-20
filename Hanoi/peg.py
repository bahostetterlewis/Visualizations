class Peg():
    def __init__(self, color, position, name):
        self.left, self.top, self.width, self.height = position
        self.discs = []
        self.name  = name
        self.color = color

    def position(self):
        return (self.left, self.top, self.width, self.height)

    def clear(self):
        del self.discs
