import arcade
import math
import pymunk
from game_object import Box

WIDTH = 800
HEIGHT = 800
TITLE = "boxes"

class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        # crear espacio
        self.space = pymunk.Space()
        self.space.gravity = (0, -9)

        # sprites
        self.sprites = arcade.SpriteList()
        self.lines = []
        self.add_boxes()
        self.add_static()

    def add_boxes(self):
        for i in range(3):
            self.sprites.append(
                Box(i * 70 + 70, 135, self.space)
            )
        for i in range(2):
            for j in range(2):
                self.sprites.append(
                    Box(i*70 + 500, j * 70 + 400, self.space)
                )

    def add_static_segment(self, x0, y0, x1, y1):
        segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        segment_shape = pymunk.Segment(segment_body, [x0, y0], [x1, y1], 0)
        segment_shape.friction = 0.1
        self.space.add(segment_body, segment_shape)
        self.lines.append((x0, y0, x1, y1))

    def add_static(self):
        # agregar piso
        self.add_static_segment(0, 0, WIDTH, 0)
        self.add_static_segment(0, 0, 0, HEIGHT)
        self.add_static_segment(WIDTH, 0, WIDTH, HEIGHT)
        self.add_static_segment(0, 100, 650, 10)
        self.add_static_segment(500, 200, WIDTH, 300)
        
    def draw_segments(self):
        for x0, y0, x1, y1 in self.lines:
            arcade.draw_line(x0, y0, x1, y1, (255, 0, 0), 3) 

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.sprites.append(
            Box(x, y, self.space)
        )

    def on_update(self, delta_time: float):
        self.space.step(1 / 60) # OJO
        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        self.draw_segments()


if __name__ == "__main__":
    app = App()
    arcade.run()