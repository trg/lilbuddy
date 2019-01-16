#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw
# from font_source_sans_pro import SourceSansPro
from font_hanken_grotesk import HankenGroteskBold

from inky import InkyPHAT
from lil_panel import LilPanel

class WelcomePanel(LilPanel):
    def __init__(self):
        self.inky_display = InkyPHAT("black")

    def build_image(self):
        print "[WelcomePanel] Rendering..."
        # Set up the correct display and scaling factors
        title_font = ImageFont.truetype(HankenGroteskBold, 24)

        # Create a new canvas to draw on
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        message = "hey y'all it's lilbuddy"

        # Draw title
        title_w, _ = title_font.getsize(message)
        title_x = int((self.inky_display.WIDTH - title_w) / 2)
        title_y = 0
        draw.text((title_x, title_y), message, self.inky_display.BLACK, font=title_font)

        return img