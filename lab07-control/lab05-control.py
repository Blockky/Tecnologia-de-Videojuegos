import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
MOVEMENT_SPEED = 3

class Sans:
    def __init__(self, x, y, change_x, change_y):

        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        # CUERPO        self.radius = radius
        arcade.draw_ellipse_filled(300 + self.x, 200, 120, 250, arcade.color.BLUE)
        # CABEZA
        arcade.draw_ellipse_filled(300 + self.x , 350, 100, 80, arcade.color.WHITE)
        arcade.draw_ellipse_filled(300 + self.x , 320, 100, 60, arcade.color.WHITE)
        # OJOS
        arcade.draw_ellipse_filled(280 + self.x , 350, 30, 25, arcade.color.BLACK)
        arcade.draw_ellipse_filled(320 + self.x , 350, 30, 25, arcade.color.BLACK)
        arcade.draw_ellipse_filled(284 + self.x , 350, 6, 8, arcade.color.WHITE)
        arcade.draw_ellipse_filled(316 + self.x , 350, 6, 8, arcade.color.WHITE)
        # SANS BOCA
        arcade.draw_arc_outline(300 + self.x , 320, 70, 30, arcade.color.BLACK,
                                210, 330, 10)
        arcade.draw_arc_outline(300 + self.x , 324, 70, 30, arcade.color.BLACK,
                                210, 330, 10)
        arcade.draw_arc_outline(300 + self.x , 328, 70, 30, arcade.color.BLACK,
                                210, 330, 10)
        arcade.draw_arc_outline(300 + self.x , 330, 70, 30, arcade.color.BLACK,
                                210, 330, 10)
        # NARIZ
        arcade.draw_triangle_filled(292 + self.x , 330, 308 + self.x , 330, 300 + self.x , 340, arcade.color.BLACK)

    def on_update(self):
        self.y += self.change_y
        self.x += self.change_x

        if self.x > SCREEN_WIDTH - 360:
            self.x = SCREEN_WIDTH - 360

        if self.x < -240:
            self.x = -240

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.LIGHT_PASTEL_PURPLE)

        self.sans = Sans(0,0, 0, 0)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        self.clear()
        self.sans.draw()

        arcade.draw_lrtb_rectangle_filled(0, 1000, 150, 0, arcade.color.PURPLE_HEART)
        arcade.draw_lrtb_rectangle_filled(0, 1000, 156, 150, arcade.color.BLACK)

    def on_update(self, delta_time):
        self.sans.on_update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.sans.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.sans.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.sans.change_x = 0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "SANS MOVIENDOSE")
    arcade.run()

main()