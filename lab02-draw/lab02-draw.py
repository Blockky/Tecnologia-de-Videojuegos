#importamos la librería de Arcade
import arcade

#Creamos una ventana arcade llamada "DIBUJO PIOLA"
arcade.open_window(1000,650, "DIBUJO PIOLA")

#Definimos que el fondo de la ventana sea de color azul claro (light cyan)
arcade.set_background_color(arcade.color.LIGHT_PASTEL_PURPLE)

# <-------------------------------- Empieza a dibujar --------------------------------------->
arcade.start_render()

#SANS CUERPO
arcade.draw_ellipse_filled(300,200,120,250,arcade.color.BLUE)

#SANS CABEZA
arcade.draw_ellipse_filled(300,350,100,80,arcade.color.WHITE)
arcade.draw_ellipse_filled(300,320,100,60,arcade.color.WHITE)

#SANS OJOS
arcade.draw_ellipse_filled(280,350,30,25,arcade.color.BLACK)
arcade.draw_ellipse_filled(320,350,30,25,arcade.color.BLACK)

arcade.draw_ellipse_filled(284,350,6,8,arcade.color.WHITE)
arcade.draw_ellipse_filled(316,350,6,8,arcade.color.WHITE)

#SANS BOCA
arcade.draw_arc_outline(300, 320, 70,30, arcade.color.BLACK,
                       210, 330, 10)
arcade.draw_arc_outline(300, 324, 70,30, arcade.color.BLACK,
                       210, 330, 10)
arcade.draw_arc_outline(300, 328, 70,30, arcade.color.BLACK,
                       210, 330, 10)
arcade.draw_arc_outline(300, 330, 70,30, arcade.color.BLACK,
                       210, 330, 10)

#SANS NARIZ
arcade.draw_triangle_filled(292,330,308,330,300,340,arcade.color.BLACK)

#SUELO
arcade.draw_lrtb_rectangle_filled(0,1000,150,0,arcade.color.PURPLE_HEART)
arcade.draw_lrtb_rectangle_filled(0,1000,156,150,arcade.color.BLACK)

#TIENDA DE SANS
arcade.draw_polygon_filled([[120, 400],
                            [200, 520],
                            [380, 520],
                            [460, 400]],
                            arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(130,160,400,133,arcade.color.BROWN_NOSE)
arcade.draw_lrtb_rectangle_filled(420,450,400,133,arcade.color.BROWN_NOSE)
arcade.draw_lrtb_rectangle_filled(120,460,190,140,arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(120,460,250,200,arcade.color.DARK_BROWN)

#COFRE DE MINECRAFT
arcade.draw_lrtb_rectangle_filled(600,775,300,125,arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(610,765,290,135,arcade.color.MEAT_BROWN)
arcade.draw_lrtb_rectangle_filled(600,775,230,220,arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(670,705,250,200,arcade.color.DARK_BROWN)

arcade.draw_lrtb_rectangle_filled(680,695,365,350,arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(680,695,410,370,arcade.color.BLACK)

# <-------------------------------- Termina de dibujar --------------------------------------->
arcade.finish_render()
arcade.run()



