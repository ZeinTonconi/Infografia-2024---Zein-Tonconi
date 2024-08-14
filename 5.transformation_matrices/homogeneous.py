import arcade
import arcade.color
import math
import numpy as np

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Matrices de transformacion"


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.vertices = [(100, 100), (100, 200), (200, 200), (200, 100)]
        
    def on_update(self, delta_time: float):
        pass
        # print(delta_time)
        # self.vertices = self.rotate(self.vertices, 10 * delta_time, 200, 200)
        # self.vertices = self.translate(self.vertices, 10 * delta_time, 10 * delta_time)
        
    def on_draw(self):
        arcade.start_render()
        self.draw_shape(self.vertices)
        new = self.translate(self.vertices, 50, 50)
        self.draw_shape(new)

    def translate(self, vertices, dx, dy):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        v_array = np.array([[x, y, 1] for x, y in vertices])
        v_array = np.transpose(v_array)
        # apply transformation
        new_v_array = np.dot(TM, v_array)
        new_v_array = new_v_array[:2, :]
        new_v_array = np.transpose(new_v_array)
        new_v_list = new_v_array.tolist()
        return new_v_list


    def scale(self, vertices, s):
        pass

    def rotate(self, vertices, angle, px=0, py=0):
        pass
    
    def draw_shape(self, vertices):
        for x, y in vertices:
            arcade.draw_point(x, y, arcade.color.RED, 4)

        arcade.draw_line_strip(vertices+[vertices[0]], arcade.color.RED)


    
if __name__ == "__main__":
    app = MyWindow()
    arcade.run()