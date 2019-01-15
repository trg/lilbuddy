class LilPanel():
    def __init__(self, inky_display):
        self.inky_display = inky_display

    def onMount(self):
        """Called when panel comes into view"""
        pass

    def onDismount(self):
        """Called when panel is moved away from"""

    def render(self):
        """Called when screen needs to be rendered. Main render method"""
        pass

    def buttonPressed(self, button):
        """Called on any button press, before more specific methods below"""
        pass

    def a(self):
        """Called when A button is tapped"""
        pass
    
    def b(self):
        """Called when B button is tapped"""
        pass

    def c(self):
        """Called when C button is tapped"""
        pass

    def d(self):
        """Called when D button is tapped"""
        pass