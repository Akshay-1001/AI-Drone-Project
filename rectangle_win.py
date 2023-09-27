import pygame

pygame.init()

# creating the surface
surface = pygame.display.set_mode((400, 250))

# red
color = (255, 0, 0)

# drawing a rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 30))

pygame.display.flip()