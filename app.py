import lil_panel
from wemo import wemo_panel

class App():
    """Entry point for Program Access Control"""

    def __init__(self):
        self.panels = [wemo_panel.WemoPanel()]
