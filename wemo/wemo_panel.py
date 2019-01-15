import pywemo

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold
from inky import InkyPHAT

from lil_panel import LilPanel

class WemoPanel(LilPanel):

    def onMount(self):
        self.loading_screen("Discovering devices...")
        #print "[WemoPanel __init__] Discovering devices..."
        #self.devices = pywemo.discover_devices()
        print "[WemoPanel onMount] Discovering devices..."
        self.devices = pywemo.discover_devices()
        self.title = "Switches"
        print self.devices

    def loading_screen(self, msg):
        hanken_bold_font = ImageFont.truetype(HankenGroteskBold, 14)
        # Create a new canvas to draw on
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)
        # Draw Message
        msg_w, msg_h = hanken_bold_font.getsize(msg)
        msg_x = int((self.inky_display.WIDTH - msg_w) / 2)
        msg_y = int((self.inky_display.HEIGHT - msg_h) / 2)
        draw.text((msg_x, msg_y), msg, self.inky_display.BLACK, font=hanken_bold_font)

        # Display the completed image
        self.inky_display.set_image(img)
        self.inky_display.show()

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

        # List each device
        device_list_font = ImageFont.truetype(HankenGroteskBold, 16)
        count = 0
        padding_x = 5
        paddying_y = 2
        for device in self.devices:
            name = device.name
            w, h = device_list_font.getsize(name)
            y = title_y + (count * h + paddying_y)
            draw.text((padding_x, y), self.title, self.inky_display.BLACK, font=device_list_font)


        # Display the completed image
        self.inky_display.set_image(img)
        self.inky_display.show()