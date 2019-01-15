import lil_panel

from wemo import wemo_panel

from inky import InkyPHAT

class App():
    """Entry point for Program Access Control"""

    def __init__(self):
        self.panels = [wemo_panel.WemoPanel(inky)]
        self.render()

    def render(self):
        print "[App] Rendering..."
        self.panels[0].render()
