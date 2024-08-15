import arcade
import random

import arcade.key
from game_object import Tank

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Polygon2d"

SPEED = 40
ANGULAR_SPEED = 1.5

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.tank = Tank(400, 400, get_random_color())

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED
        
        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = ANGULAR_SPEED
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = -ANGULAR_SPEED
        

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.tank.speed = 0
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.tank.angular_speed = 0

        if symbol == arcade.key.SPACE:
            self.tank.fire()
            
    def on_update(self, delta_time: float):
        self.tank.update(delta_time)

    def on_draw(self):
        arcade.start_render()
        self.tank.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()