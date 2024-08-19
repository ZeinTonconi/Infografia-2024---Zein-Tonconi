import arcade
import math
import pymunk

WIDTH = 800
HEIGHT = 800
TITLE = "hello physics"

class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        # crear espacio
        self.space = pymunk.Space()
        self.space.gravity = (0, -9)

        # agregar body
        body = pymunk.Body(mass=1, moment=pymunk.moment_for_box(1, (30, 30)))
        body.position = (WIDTH // 2, HEIGHT // 2)

        # agregar shape
        self.shape = pymunk.Poly.create_box(body, (30, 30))
        self.shape.elasticity = 0.3
        self.shape.friction = 0.5

        # agregar piso
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, (0, 20), (WIDTH, 200), 0)
        floor_shape.friction = 0.1

        # agregar al espacio
        self.space.add(body, self.shape)
        self.space.add(floor_body, floor_shape)

        self.sprites = arcade.SpriteList()
        self.body_sprite = arcade.SpriteSolidColor(30, 30, (0, 255, 0))
        self.sprites.append(self.body_sprite)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60) # OJO

        # acoplar movimiento del body con el sprite
        self.body_sprite.center_x = self.shape.body.position.x
        self.body_sprite.center_y = self.shape.body.position.y
        self.body_sprite.radians = self.shape.body.angle
        

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()