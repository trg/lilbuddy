from inky import InkyPHAT

class LilPanel(object):
    def __init__(self):
        # I did a bad thing and forgot in python, composition > inheritance
        pass

    # Screen
    def build_image(self):
        """Returns image for inky display"""
        print "Method missing"
        pass

    # EVENTS

    def on_mount(self):
        """Called when panel comes into view"""
        print "Method missing"
        pass

    def on_dismount(self):
        """Called when panel is moved away from"""
        print "Method missing"
        pass


    def on_touch(self, event):
        """Called when button is released"""
        # event.channel = index of button, from 0 = back, 1 = A, etc
        print "Method missing"
        pass

    def on_release(self, event):
        """Called when button is released"""
        # event.channel = index of button, from 0 = back, 1 = A, etc
        print "Method missing"
        pass