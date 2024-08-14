import arcade
import arcade.color
import math

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Primitivas de arcade"


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.vertices = [(100, 100), (100, 200), (200, 200), (200, 100)]
        
    def on_update(self, delta_time: float):
        print(delta_time)
        # self.vertices = self.rotate(self.vertices, 10 * delta_time, 200, 200)
        # self.vertices = self.translate(self.vertices, 10 * delta_time, 10 * delta_time)
        
    def on_draw(self):
        arcade.start_render()
        self.draw_shape(self.vertices)
        new = self.scale(self.vertices, 2)
        self.draw_shape(new)
        # new = self.rotate(self.vertices, 30, 100, 100)
        # self.draw_shape(new)
        # for i in range(11):
        #     new = self.rotate(new, 30, 100, 100)
        #     self.draw_shape(new)

    def translate(self, vertices, dx, dy):
        return [(x + dx, y + dy) for x, y in vertices]

    def rotate(self, vertices, angle, px=0, py=0):
        new_vertices = []
        angle_radians = math.radians(angle)
        for x, y in vertices:
            new_vertices.append(
                ((x - px) * math.cos(angle_radians) - (y - py) * math.sin(angle_radians) + px,
                 (x - px) * math.sin(angle_radians) + (y - py) * math.cos(angle_radians) + py)
            )

        return new_vertices
    
    def scale(self, vertices, s):
        return [(s * x, s * y) for x, y in vertices]

    def draw_shape(self, vertices):
        for x, y in vertices:
            arcade.draw_point(x, y, arcade.color.RED, 4)

        arcade.draw_line_strip(vertices+[vertices[0]], arcade.color.RED)


    
if __name__ == "__main__":
    app = MyWindow()
    arcade.run()