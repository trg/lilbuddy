#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

# my panels
import lil_panel
from wemo import wemo_panel

# pHAT libraries
import touchphat
from inky import InkyPHAT

class App():
    """Entry point for Program Access Control"""

    def __init__(self):
        touchphat.all_on() # the ol' razzle dazzle when it boots
        time.sleep(0.5)
        touchphat.all_off()
        self.inky_display = InkyPHAT("black")
        self.panels = [wemo_panel.WemoPanel(self.inky_display)]
        self.panels[0].onMount() # mount first panel

        while True:
            # TODO - re-render only if state is dirty
            self.render()
            time.sleep( 10 ) # re-render every N seconds, TODO replace with asyncio?

    def render(self):
        print "[App] Rendering..."
        self.panels[0].render()

def main(argv):
    App()

if __name__ == "__main__":
    main(sys.argv)