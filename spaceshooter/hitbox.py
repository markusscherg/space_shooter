import arcade


class Hitbox:
    def __init__(self,x, y, r):
        self.center_x = x
        self.center_y = y
        self.radius = r

    def set_position(self, x,y):
        self.center_x = x
        self.center_y = y

    def collides_with(self, other):
        # Calculate the distance between the centers of the two hitboxes
        distance = ((self.center_x - other.center_x) ** 2 + (self.center_y - other.center_y) ** 2) ** 0.5
        # Check if the distance is less than or equal to the sum of the radii
        return distance <= (self.radius + other.radius)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.BLUE)
