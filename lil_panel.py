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

    def on_touch(self, event):
        """Called when button is released"""
        # event.channel = index of button, from 0 = back, 1 = A, etc
        pass

    def on_release(self, event):
        """Called when button is released"""
        # event.channel = index of button, from 0 = back, 1 = A, etc
        pass