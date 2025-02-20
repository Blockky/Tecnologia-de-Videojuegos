import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650



def draw_sans(x):
    #CUERPO
    arcade.draw_ellipse_filled(300 + x,200,120,250,arcade.color.BLUE)
    #CABEZA
    arcade.draw_ellipse_filled(300 + x,350,100,80,arcade.color.WHITE)
    arcade.draw_ellipse_filled(300 + x,320,100,60,arcade.color.WHITE)
    #OJOS
    arcade.draw_ellipse_filled(280+x,350,30,25,arcade.color.BLACK)
    arcade.draw_ellipse_filled(320+x,350,30,25,arcade.color.BLACK)
    arcade.draw_ellipse_filled(284+x,350,6,8,arcade.color.WHITE)
    arcade.draw_ellipse_filled(316+x,350,6,8,arcade.color.WHITE)
    #SANS BOCA
    arcade.draw_arc_outline(300+x, 320, 70,30, arcade.color.BLACK,
                           210, 330, 10)
    arcade.draw_arc_outline(300+x, 324, 70,30, arcade.color.BLACK,
                           210, 330, 10)
    arcade.draw_arc_outline(300+x, 328, 70,30, arcade.color.BLACK,
                           210, 330, 10)
    arcade.draw_arc_outline(300+x, 330, 70,30, arcade.color.BLACK,
                           210, 330, 10)
    #NARIZ
    arcade.draw_triangle_filled(292+x,330,308+x,330,300+x,340,arcade.color.BLACK)

def draw_floor():
    arcade.draw_lrtb_rectangle_filled(0,1000,150,0,arcade.color.PURPLE_HEART)
    arcade.draw_lrtb_rectangle_filled(0,1000,156,150,arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()

    draw_sans(on_draw.x_sans)
    on_draw.x_sans += 1
    draw_floor()

on_draw.x_sans = 0


def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT, "DIBUJO PIOLA")
    arcade.set_background_color(arcade.color.LIGHT_PASTEL_PURPLE)

    arcade.schedule(on_draw, 1/60)

    arcade.run()

main()