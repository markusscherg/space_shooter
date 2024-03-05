import random
import arcade

from spaceshooter.asteroids import BigAsteroid
from spaceshooter.spaceship import SpaceShip


class Game(arcade.Window):
    def __init__(self, screen_width: int, screen_height: int, screen_title="Spaceshooter!"):
        super().__init__(screen_width, screen_height, screen_title)

        # Attributes of the Game class
        self.spaceship = None
        self.asteroids = []
        self.bullets = []
        self.powerups = []

        # some additional attributes
        self.min_asteroids = 3  # minimal number of asteroids to be in the game

        # Dictionary to keep track of key states
        self.key_states = {}

        # Debugging
        self.debug = False

    def setup(self):
        """
            This method is called once before the game starts.
            It can be seen as an addition to the __init__ method.
            Call this method manually to restart the game.
        """
        # Initialize spaceship
        self.spaceship = SpaceShip(":resources:images/space_shooter/playerShip1_orange.png", 1, 200, 200)
        self.spaceship.set_position(self.width / 2, self.spaceship.height)



    def update(self, delta_time: float):
        """Check for user inputs."""

        # Move spaceship if LEFT or RIGHT is pressed
        if self.is_key_pressed(arcade.key.RIGHT):
            self.spaceship.move(delta_time, 0)
        elif self.is_key_pressed(arcade.key.LEFT):
            self.spaceship.move(-delta_time, 0)

        # Move Asteroids
        for asteroid in self.asteroids:
            asteroid.move(0, -delta_time)

            # Handle Collisions
            self.handle_collisions()

        # Remove Asteroids that are out of screen
        new_asteroids = [asteroid for asteroid in self.asteroids if asteroid.center_y > 0]
        self.asteroids = new_asteroids

        # spawn new asteroid if there are less than 3
        if len(self.asteroids) < self.min_asteroids:
            self.spawn_asteroid()



    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw spaceship, asteroids and bullets
        self.spaceship.draw()
        for asteroid in self.asteroids:
            asteroid.draw()

        # Draw Hitboxes if in debug mode
        if self.debug:
            self.spaceship.hitbox.draw()

            for a in self.asteroids:
                a.hitbox.draw()

    def on_key_press(self, key, modifiers):
        self.key_states[key] = True

        if key == arcade.key.LCTRL or key == arcade.key.RCTRL:
            self.spaceship.shoot()

    def on_key_release(self, key, modifiers):
        self.key_states[key] = False

    def is_key_pressed(self, key):
        return self.key_states.get(key, False)

    def spawn_asteroid(self):
        x = random.randint(0, self.width)
        y = random.randint(self.height, self.height + 350)
        t = random.randint(1, 2)

        if t == 1:
            # Spawn big asteroid
            hp = random.randint(20, 200)
            speed = random.randint(40,180)
            asteroid = BigAsteroid(":resources:images/space_shooter/meteorGrey_big2.png", 1, speed, 30, hp)
            asteroid.set_position(x,y)
            self.asteroids.append(asteroid)

    def handle_collisions(self):
        # Handle collisions between spaceship and asteroids
        colliding_asteroids = []
        for asteroid in self.asteroids:
            if asteroid.hitbox.collides_with(self.spaceship.hitbox):
                colliding_asteroids.append(asteroid)
        self.asteroids = [asteroid for asteroid in self.asteroids if asteroid not in colliding_asteroids]