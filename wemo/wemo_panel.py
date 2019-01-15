import pywemo

from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT

from lil_panel import LilPanel

class WemoPanel(LilPanel):
    def __init__(self, inky):
        super().__init__()
        self.title = "Light Switches"
        print "[WemoPanel __init__] Discovering devices..."
        self.devices = pywemo.discover_devices()

    def onMount(self):
        print "[WemoPanel onMount] Discovering devices..."
        self.devices = pywemo.discover_devices()

    def render(self):
        print "[WemoPanel] Rendering..."
        # Set up the correct display and scaling factors
        hanken_bold_font = ImageFont.truetype(HankenGroteskBold, 35)

        inky_display = InkyPHAT("black")

        # Create a new canvas to draw on
        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Draw title
        title_w, title_h = hanken_bold_font.getsize(self.title)
        title_x = int((inky_display.WIDTH - title_w) / 2)
        title_y = 0
        draw.text((title_x, title_y), self.title, inky_display.WHITE, font=hanken_bold_font)

        # Display the completed image
        inky_display.set_image(img)
        inky_display.show()