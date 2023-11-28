import math

import arcade


class SpaceShip(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

        # Movement speed of the spaceship
        self.speed = 200

        print(self.width, self.height)

    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y

    def move(self, x, y):
        self.center_x += self.speed * x
        self.center_y += self.speed * y
