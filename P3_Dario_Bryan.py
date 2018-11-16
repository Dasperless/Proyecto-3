import pyglet
from pyglet.window import mouse
window = pyglet.window.Window()
image = pyglet.resource.image('mina.png')

@window.event
def on_draw():
    window.clear()
    image.blit(350, 400)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
pyglet.app.run()
