import arcade
import pymunk

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Spring-Damper System Example"

# Physics parameters
MASS = 1.0
DAMPING = 0.5
STIFFNESS = 100.0
ANCHOR_POINT = (400, 500)
INITIAL_POSITION = (400, 300)

class SpringDamperSimulation(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.space = pymunk.Space()
        self.space.gravity = (0, -981)  # Gravity in pixels/second^2
        
        # Create the ball (dynamic body)
        body = pymunk.Body(MASS, pymunk.moment_for_circle(MASS, 0, 20))
        body.position = INITIAL_POSITION
        shape = pymunk.Circle(body, 20)
        shape.elasticity = 0.5
        self.space.add(body, shape)
        self.ball_sprite = arcade.SpriteCircle(20, arcade.color.BLUE)
        
        # Create the spring-damper (DampedSpring joint)
        anchor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        anchor_body.position = ANCHOR_POINT
        
        self.spring = pymunk.DampedSpring(
            anchor_body, body,  # Anchor and ball bodies
            (0, 0), (0, 0),  # Attachment points on the bodies
            rest_length=200, stiffness=STIFFNESS, damping=DAMPING
        )
        self.space.add(self.spring)
        
        # Anchor point
        self.anchor_sprite = arcade.SpriteCircle(10, arcade.color.RED)
        self.anchor_sprite.position = ANCHOR_POINT

    def on_draw(self):
        arcade.start_render()
        
        # Draw the anchor point
        self.anchor_sprite.draw()

        self.ball_sprite.draw()
        
        # Draw the spring as a line between the anchor and the ball
        arcade.draw_line(
            self.anchor_sprite.center_x, self.anchor_sprite.center_y,
            self.ball_sprite.center_x, self.ball_sprite.center_y,
            arcade.color.YELLOW, 2
        )

    def on_update(self, delta_time):
        self.space.step(1/60)
        self.ball_sprite.position = self.spring.b.position

def main():
    window = SpringDamperSimulation(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
