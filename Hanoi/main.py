import pygame
from pygame import locals as pylocals

from peg import Peg


def PegBuilder(surface):
    mainpeg = Peg((255, 0, 0), (100, 50, 10, 100), 'Main Peg')
    auxpeg = Peg((0, 255, 0), (250, 50, 10, 100), 'Aux Peg')
    destpeg = Peg((0, 0, 255), (400, 50, 10, 100), 'Dest Peg')
    pegs = [mainpeg, auxpeg, destpeg]
    return pegs

def DiscBuilder(surface, pegs, discCount):
    for i in reversed(range(discCount)):
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
        print(l)
        curDisc = pygame.draw.rect(surface, (i*30, i*30, i*30), (x, y, l, h))
        pegs[0].discs.append(curDisc)

def SwapPegs(pegs, first, second):
    pegs[first], pegs[second] = pegs[second], pegs[first]
    for i, peg in enumerate(pegs):
        peg.left = 100 + i * 150

def DrawPegs(pegs, surface):
    surface.fill((250, 250, 250))
    for peg in pegs:
        pygame.draw.rect(surface, peg.color, peg.position())

def update(screen, background):
    screen.blit(background, (0,0))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500)) #  sets the screen size
    pygame.display.set_caption('Towers Of Hanoi Visualization') #  window title
    # create a background and convert it ty type of parent?
    background = pygame.Surface(screen.get_size()).convert()
    pegs = PegBuilder(background)
    DrawPegs(pegs, background)
    update(screen, background)
    clock = pygame.time.Clock()

    s = (['biggest', 'bigger', 'big', 'medium', 'little'], '1')
    a = ([], '2')
    d = ([], '3')
    pygame.time.wait(1000)
    hanoi(len(s[0]),s,a,d, pegs, screen, background)
    print('done')

    while(1): #  main loop
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pylocals.QUIT:
                    return


def hanoi(n, s, a, d, pegs, screen, background):
    if n > 0:
        pygame.time.wait(90)
        SwapPegs(pegs, 1, 2)
        DrawPegs(pegs, background)
        update(screen, background)
        hanoi(n - 1, s, d, a, pegs, screen, background)
        pygame.time.wait(90)
        SwapPegs(pegs, 1, 2)
        DrawPegs(pegs, background)
        update(screen, background)

        if s[0]:
            d[0].append(s[0].pop())

        pygame.time.wait(90)
        SwapPegs(pegs, 0, 1)
        DrawPegs(pegs, background)
        update(screen, background)
        # move tower of size n-1 from a to d
        hanoi(n - 1, a, s, d, pegs, screen, background)
        pygame.time.wait(90)
        DrawPegs(pegs, background)
        update(screen, background)
        SwapPegs(pegs, 0, 1)

if __name__ == '__main__':
    main()
