import arcade

# Set constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tutorial"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Clear screen and start render process
arcade.start_render()

# --- Drawing Commands Will Go Here ---

arcade.draw_line(0,0,400,300, arcade.color.BLACK)

arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()