import pygame
from pygame import locals as pylocals

from peg import Peg


def PegBuilder(surface):
    mainpeg = Peg(surface, (255, 0, 0), (100, 50, 10, 100), 'Main Peg')
    auxpeg = Peg(surface, (0, 255, 0), (250, 50, 10, 100), 'Aux Peg')
    destpeg = Peg(surface, (0, 0, 255), (400, 50, 10, 100), 'Dest Peg')
    pegs = [mainpeg, auxpeg, destpeg]
    return pegs

def DiscBuilder(surface, pegs, discCount):
    for i in range(0, discCount):
        #  constant length of 20 and the peg size increase
        l = 20 + (20 * i)
        h = 10
        #  constant 150 due to peg length + its y coord is 150
        #  add the peg delta offset to constant to get the y coord
        y = (150 - discCount * 10) + (10 * i)
        #  Constant is middle of the mainpeg its x + 1/2 its width
        #  subtract half of the length of the current peg so that it is
        #  centered on the center of the given peg
        x = 105 - l // 2
        curDisc = pygame.draw.rect(surface, (i*30, i*30, i*30), (x, y, l, h))
        pegs[0].discs.append(curDisc)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500)) #  sets the screen size
    pygame.display.set_caption('Towers Of Hanoi Visualization') #  window title
    background = pygame.Surface(screen.get_size()).convert() # create a background and convert it ty type of parent?
    background.fill((250, 250, 250))
    pegs = PegBuilder(background)
    DiscBuilder(background, [], 6)
    screen.blit(background, (0,0))
    clock = pygame.time.Clock()


    pygame.display.flip()  # update screen
    while(1): #  main loop
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pylocals.QUIT:
                    return

if __name__ == '__main__':
    main()