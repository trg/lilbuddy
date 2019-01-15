import pywemo

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold
from inky import InkyPHAT

from lil_panel import LilPanel

class WemoPanel(LilPanel):
    # def __init__(self, inky_display):
    #     super(LilPanel, self).__init__(inky_display)
    #     self.title = "Light Switches"
    #     print "[WemoPanel __init__] Discovering devices..."
    #     self.devices = pywemo.discover_devices()

    def onMount(self):
        self.title = "Light Switches"
        #print "[WemoPanel __init__] Discovering devices..."
        #self.devices = pywemo.discover_devices()
        print "[WemoPanel onMount] Discovering devices..."
        self.devices = pywemo.discover_devices()
        print self.devices

    def render(self):
        print "[WemoPanel] Rendering..."
        # Set up the correct display and scaling factors
        hanken_bold_font = ImageFont.truetype(HankenGroteskBold, 24)

        # Create a new canvas to draw on
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Draw title
        title_w, title_h = hanken_bold_font.getsize(self.title)
        title_x = int((self.inky_display.WIDTH - title_w) / 2)
        title_y = 0
        draw.text((title_x, title_y), self.title, self.inky_display.BLACK, font=hanken_bold_font)

        # Display the completed image
        self.inky_display.set_image(img)
        self.inky_display.show()