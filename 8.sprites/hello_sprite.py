import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Uso de Sprites"

class Mario(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.sprites = arcade.SpriteList()
        self.mario = Mario(
            "8.sprites/img/mario.png",
            0.6, 
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2
            )
        
        self.sprites.append(self.mario)
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mario.center_x = x
        self.mario.center_y = y

    def on_update(self, delta_time: float):
        self.sprites.update()

    def on_draw(self):
        self.sprites.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()