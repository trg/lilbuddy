import sys
import lil_panel
import time

from wemo import wemo_panel
from inky import InkyPHAT

class App():
    """Entry point for Program Access Control"""

    def __init__(self):
        self.panels = [wemo_panel.WemoPanel(inky)]
        self.panels[0].onMount() # mount first panel
        while True:
            self.render()
            time.sleep( 5 ) # re-render every 5 seconds, TODO replace with asyncio

    def render(self):
        print "[App] Rendering..."
        self.panels[0].render()

def main(argv):
    App()

if __name__ == "__main__":
    main(sys.argv)