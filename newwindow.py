import pygame

# Initialize pygame
pygame.init()

# to create a pygame window
screen = pygame.display.set_mode((480,240))

# get the sie
x, y = screen.get_size()

# quit pygame when done
pygame.display.quit()

print(x, y)