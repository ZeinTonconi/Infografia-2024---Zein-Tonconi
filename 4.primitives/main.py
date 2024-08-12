import arcade
from bresenham import get_line, get_circle

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Circulos con bresenham"


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 10
        # circulo
        self.xc = 30
        self.yc = 40
        self.r = 15
        # linea
        self.x0, self.y0, self.x1, self.y1 = 20, 20, 150, 70
        self.circle_color = arcade.color.RED_DEVIL

        # self.speed = 25
        # self.velocity = [25, 20]

    def on_update(self, delta_time: float):
        pass
        # self.xc += delta_time * self.velocity[0]
        # self.yc += delta_time * self.velocity[1]

        # # Logica del rebote en X
        # if (self.xc + self.r > SCREEN_WIDTH // self.pixel_size 
        #     or self.xc - self.r < 0):
        #     self.velocity[0] = -1 * self.velocity[0]

        # # Logica del rebote en Y
        # if (self.yc + self.r > SCREEN_HEIGHT // self.pixel_size 
        #     or self.yc - self.r < 0):
        #     self.velocity[1] = -1 * self.velocity[1]

    def on_draw(self):
        arcade.start_render()
        points = get_circle(
            self.xc,
            self.yc,
            self.r
        )
        line_points = get_line(
            self.x0, self.y0,
            self.x1, self.y1
        )
        self.draw_grid()
        self.draw_circle_points(points, arcade.color.DARK_YELLOW)
        self.draw_scaled_circle(
            self.xc,
            self.yc,
            self.r
        )
        self.draw_line_points(line_points, arcade.color.ALICE_BLUE)
        self.draw_pentagon(0, 0, 5)

    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [50, 50, 50]
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [50, 50, 50]
            )

    def draw_circle_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_circle(self, xc, yc, r):
        arcade.draw_circle_outline(
            xc * self.pixel_size, 
            yc * self.pixel_size, 
            r * self.pixel_size, 
            [100, 255, 40, 150], 
            5
        )

    def draw_line_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            [100, 255, 40, 150],
            5
        )

    # ejemplo base de implementacion
    def draw_pentagon(self, xc, yc, r, color):
        # obtener vertices
        # obtener bordes entre vertices
        points = get_line(0,0,0,0)
        # dibujar figura
        self.draw_line_points(points, color)

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()