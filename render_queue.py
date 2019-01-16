from inky import InkyPHAT
import time
from pubsub import pub

# TODO - major refactor to use correct types
# specifically related to KeyboardInterrupt

class RenderQueue():

    def __init__(self):
        self.img_stack = []
        self.inky_display = InkyPHAT("black")
        pub.subscribe(self.add_image, 'add_image')

    def add_image(self, img):
        self.img_stack.append(img)

    def run(self):
        while True:
            if len(self.img_stack) > 0:
                most_recent_frame = self.img_stack.pop()
                self.img_stack = []
                self.inky_display.set_image(most_recent_frame)
                self.inky_display.show()
            time.sleep( 0.1 )