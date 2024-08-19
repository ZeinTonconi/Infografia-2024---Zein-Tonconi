import pymunk

# crear space
space = pymunk.Space()
space.gravity = (0, -9)

# crear body
body = pymunk.Body()
body.position = (50, 100)
body.mass = 10

# crear shape
shape = pymunk.Poly.create_box(body)

# agregar al espacio
space.add(body, shape)

print_options = pymunk.SpaceDebugDrawOptions()

for _ in range(100):
    space.step(0.02) # 50 fps
    space.debug_draw(print_options)
