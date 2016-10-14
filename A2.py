"""
work on making a function that will take a black image
and put that into the GPU so that the graphics card can
do the work to make it faster. also make the function input
an image so that it doesnt have to be just a black image.

"""

import sys
import sdl2
import sdl2.ext
import time
import Audio


"""
@Author: Nathan Levis
@Date:	 10/14/2016
		 This file includes everything necessary to create a window and change the color of the window surface.
"""

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):

    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, (255, 255, 255)) # initial window will be white
        super(SoftwareRenderer, self).render(components)


class SoftwareRen(sdl2.ext.SoftwareSpriteRenderSystem):
    def render(self, components):
       
        for x in Audio.myArray1:
            color = sdl2.ext.Color(x, x, x)
			# deems the color black to color the window.
            sdl2.ext.fill(self.surface, color)
            time.sleep(1)
            super(SoftwareRen, self).render(components)

def run():
    sdl2.ext.init()  # Initializes SDL2
    window = sdl2.ext.Window("Frequency Image", size=(600, 600))
    # deems the window specs
    window.show()  # makes the window visible
    world = sdl2.ext.World()
    # deems the world environment
    spriteRenderer = SoftwareRenderer(window)
    # Renders the window
    world.add_system(spriteRenderer)
    # adds the world to the window environment
    world.add_system(SoftwareRen(window))

    running = True

    while running:
        events = sdl2.ext.get_events()  # makes it so the window looks for events
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        world.process()


if __name__ == "__main__":
    sys.exit(run())
