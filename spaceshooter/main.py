"""
Platformer Game
"""
import math

import arcade

from spaceshooter.spaceship import SpaceShip

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Spaceshooter!"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Dictionary to keep track of key states
        self.key_states = {}

        # Our Spaceship goes here
        self.spaceship = None

        # This sets the background color. For a space shooter black seems fitting
        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.spaceship = SpaceShip(":resources:images/space_shooter/playerShip1_orange.png", 1)
        self.spaceship.set_position(SCREEN_WIDTH / 2, self.spaceship.height)

    def update(self, delta_time: float):
        if self.is_key_pressed(arcade.key.RIGHT):
            self.spaceship.move(delta_time, 0)
        elif self.is_key_pressed(arcade.key.LEFT):
            self.spaceship.move(-delta_time, 0)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.spaceship.draw()

    def on_key_press(self, key, modifiers):
        self.key_states[key] = True

    def on_key_release(self, key, modifiers):
        self.key_states[key] = False

    def is_key_pressed(self, key):
        return self.key_states.get(key, False)

    def normalize_vector(self, x, y):
        magnitude = math.sqrt(x ** 2 + y ** 2)

        # Avoid division by zero
        if magnitude == 0:
            return 0, 0

        return x / magnitude, y / magnitude


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
