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
        self.sprites.append(
            Box(400, 400, self.space)
        )

    def on_update(self, delta_time: float):
        self.space.step(1 / 60) # OJO
        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()