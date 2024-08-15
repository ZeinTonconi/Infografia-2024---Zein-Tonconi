import arcade
from game_object import Polygon2D

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Polygon2d"


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.objects = []

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.C:
            self.objects.append(
                Polygon2D(
                    vertices=[
                        (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50),
                        (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50),
                        (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 + 50),
                        (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50),
                    ],
                    color=arcade.color.YELLOW,
                )
            )
            print(f"objetos: {len(self.objects)}")c
        

    def on_draw(self):
        arcade.start_render()
        for obj in self.objects:
            obj.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()