import pygame
from pygame.locals import *
import numpy as np
from pygame import gfxdraw
g = 1


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm


class Planet:
    def __init__(self, x, y, vx, vy, mass):
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.mass = mass

    def draw(self):
        pygame.gfxdraw.aacircle(screen, int(self.pos[0]), int(self.pos[1]), 1 + int(np.sqrt(self.mass)), (0, 0, 0))

    def compute(self, planets):
        total_force = 0
        for planet in planets:
            if planet != self:
                distance = np.sqrt((planet.pos[0] - self.pos[0]) ** 2 + (planet.pos[1] - self.pos[1]) ** 2)
                force = g * ((self.mass * planet.mass) / distance ** 2)
                force_direction = normalize(planet.pos - self.pos)
                final_force = force * force_direction
                total_force += final_force

        acceleration = total_force / self.mass
        self.vel += acceleration * 0.1
        self.pos += self.vel * 0.1

        # pygame.draw.line(screen, (0, 0, 0), self.pos/2, self.pos/2 + final_force * 50)


star1 = Planet(250., 250., 0., 0., 1000.)
# star2 = Planet(300., 250., 0., -1.5, 1000.)
planet1 = Planet(250., 70., 2., 0., 20.)
planet1_moon = Planet(250., 80., 3.5, 0., 1.)
planet2 = Planet(250., 150., 4., 0., 0.1)
planets = [star1, planet1, planet1_moon, planet2]
screen = pygame.display.set_mode((500, 500))
done = False
screen.fill((255, 255, 255))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    for planet in planets:
        planet.compute(planets)
        planet.draw()

    pygame.display.flip()

