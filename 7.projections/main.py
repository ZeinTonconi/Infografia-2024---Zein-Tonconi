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
        self.fox = Object3D(
            [
                (2,0,0),
                (0,-1.8,0),
                (0,-1,1),
                (0,1,1),
                (0,1.8,0),
                (0,0,-1),
                (-2,-3.5,1),
                (-2,3.5,1),
                (-2,1,3),
                (-2,-1,3) ,
                (-4,0,3.5),
                (-3,-1,3.3),
                (-3,-2.3,2.5),
                (-3,1,3.3),
                (-3,2.3,2.5),
                (-3,-1.5,5),
                (-3,1.5,5)
            ],
            [  
                (0,5),
                (5,4),
                (3,4),
                (2,3),
                (1,2),
                (1,5),
                (0,1),
                (0,4),
                (0,2),
                (0,3),
                (1,6),
                (6,9),
                (9,8),
                (8,7),
                (3,8),
                (2,9),
                (8,10),
                (10,9),
                (4,7),
                (7,14),
                (14,13),
                (10,11),
                (11,12),
                (13,10),
                (12,6),
                (12,15),
                (15,11),
                (16,13),
                (16,14),
                (5,7),
                (5,6)
            ],
            arcade.color.YELLOW
        )
        self.fox.translate(399, 399, 0)
        self.fox.scale(50, 50, 50)
        self.fox.rotate(-np.pi/2, "x")
        self.fox.rotate(np.pi/2, "y")
        # self.fox.rotate(np.pi*3/2, "x")
        # self.fox.rotate(0.1, "x")
        # self.fox.rotate(2, "y")
        # self.fox.rotate(0.1, "z")
        self.mouse_vector = np.array([400.0,400.0,200.0])
        
    
  

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_vector[0] = x
        self.mouse_vector[1] = y
        pass

    def on_update(self, delta_time: float):
        
        mouse_centered = self.mouse_vector
        self.fox.follow_mouse(mouse_centered, delta_time)
        pass

    def on_draw(self):
        arcade.start_render()
        self.fox.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()