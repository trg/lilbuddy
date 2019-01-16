#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from threading import Thread

from render_queue import RenderQueue

# my panels
import lil_panel
from wemo import wemo_panel
from dummy_panel import DummyPanel
from welcome_panel import WelcomePanel

# pHAT libraries
import touchphat
from pubsub import pub

class App():
    """Entry point for Program Access Control"""

    def __init__(self):
        touchphat.all_off()
        self.panels = [
            wemo_panel.WemoPanel(),
            DummyPanel(),
            WelcomePanel()
        ]
        self.panel_index = 0
        touchphat.on_release(1, handler=self.tap) # the pad index and channel index are off by one :(
        touchphat.on_release(6, handler=self.tap)

        # first time startup tasks
        self.current_panel().on_mount() # mount first panel
        self.render() # initial render
    
    def current_panel(self):
        return self.panels[self.panel_index]

    def tap(self, event):        
        print "[App tap] event.channel", event.channel
        direction = 0
        if event.channel == 0: # TODO use enums or names instead of channel numbers
            direction = -1
        if event.channel == 5:
            direction = 1
        self.panel_index = (self.panel_index + direction) % len(self.panels)
        print "[App tap] self.panel_index = ", self.panel_index
        self.render()

    def render(self):
        print "[App render] Rendering..."
        img = self.current_panel().build_image()
        pub.sendMessage('add_image', img=img)

def main(argv):
    # Start rendering queue:
    render_queue = RenderQueue()
    process = Thread(target=render_queue.run)
    process.start()

    # Start biz logic
    app = App()
    pub.subscribe(app.render, 'render')
    
    # TODO - build a queue of img objects to be rendered, but only render most recent
    # https://christopherdavis.me/blog/threading-basics.html

    while True:
        time.sleep( 0.25 )

if __name__ == "__main__":
    main(sys.argv)