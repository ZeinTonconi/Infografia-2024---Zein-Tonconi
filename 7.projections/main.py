import arcade
import numpy as np
import random
from game_object import Object3D

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Projeccion 3d"


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
        self.cube = Object3D(
            [
                (0.5, 0, 1),
                (-1,-1,2),
                (2,-1,2),
                (0.5,2,2)
            ],
            [
                (0,1),
                (0,2),
                (0,3),
                (1,2),
                (1,3),
                (2,3)
            ],
            arcade.color.YELLOW
        )
        self.cube.translate(399, 399, 0)
        self.cube.scale(100, 100, 100)
        # self.cube.rotate(0.1, "x")
        # self.cube.rotate(2, "y")
        # self.cube.rotate(0.1, "z")
        self.mouse_vector = np.array([600.0,600.0,100.0])
        
    
  

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_vector[0] = x
        self.mouse_vector[1] = y
        pass

    def on_update(self, delta_time: float):
        
        mouse_centered = self.mouse_vector - np.array([400,400,0])

        self.cube.follow_mouse(mouse_centered, delta_time)
        pass

    def on_draw(self):
        arcade.start_render()
        self.cube.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()