import sys
import lil_panel
import time

from wemo import wemo_panel
from inky import InkyPHAT

class App():
    """Entry point for Program Access Control"""

    def __init__(self):
        self.inky_display = InkyPHAT("black")
        self.panels = [wemo_panel.WemoPanel(self.inky_display)]
        self.panels[0].onMount() # mount first panel
        while True:
            # TODO - re-render only if state is dirty
            self.render()
            time.sleep( 5 ) # re-render every 5 seconds, TODO replace with asyncio?

    def render(self):
        print "[App] Rendering..."
        self.panels[0].render()

def main(argv):
    App()

if __name__ == "__main__":
    main(sys.argv)