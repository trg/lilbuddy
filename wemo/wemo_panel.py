#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pywemo
import touchphat
from pubsub import pub

from PIL import Image, ImageFont, ImageDraw
# from font_source_sans_pro import SourceSansPro
from font_hanken_grotesk import HankenGroteskBold
from font_font_awesome import FontAwesome5Free, FontAwesome5FreeSolid
from inky import InkyPHAT

from lil_panel import LilPanel

class WemoPanel(LilPanel):

    def __init__(self):
        self.inky_display = InkyPHAT("black")
        self.devices = []

    def on_mount(self):
        self.title = "Switches"
        if len(self.devices) == 0:
            print "[WemoPanel on_mount] Discovering devices..."
            pub.sendMessage('add_image', img=self.loading_screen("Discovering Devices..."))
            self.devices = pywemo.discover_devices()
            print "[WemoPanel on_mount] Discovered:", self.devices
        # register touch events, right now limited to 4, TODO add "More" as button 5
        touchphat.on_release(2, handler=self.on_release)
        touchphat.on_release(3, handler=self.on_release)
        touchphat.on_release(4, handler=self.on_release)
        touchphat.on_release(5, handler=self.on_release)

    # TODO - make this part of build_image
    def loading_screen(self, msg):
        current_font = ImageFont.truetype(HankenGroteskBold, 16)
        # Create a new canvas to draw on
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Draw Message
        msg_w, msg_h = current_font.getsize(msg)
        msg_x = int((self.inky_display.WIDTH - msg_w) / 2)
        msg_y = int((self.inky_display.HEIGHT - msg_h) / 2)
        draw.text((msg_x, msg_y), msg, self.inky_display.BLACK, font=current_font)

        return img

    def build_image(self):
        print "[WemoPanel] build_image..."

        # Set up the correct display and scaling factors
        title_font = ImageFont.truetype(HankenGroteskBold, 24)

        # Create a new canvas to draw on
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Draw title
        title_w, title_h = title_font.getsize(self.title)
        title_x = int((self.inky_display.WIDTH - title_w) / 2)
        title_y = 0
        draw.text((title_x, title_y), self.title, self.inky_display.BLACK, font=title_font)

        # List each device
        device_list_font = ImageFont.truetype(HankenGroteskBold, 16)
        count = 0
        padding_x = 5
        padding_y = 2
        button_map = ["A", "B", "C", "D"]
        for device in self.devices:
            name = device.name
            is_on = device.get_state() == 1
            # solid font for off; regular (outline only) for on
            if is_on:
                icon_font = ImageFont.truetype(FontAwesome5Free, 14)
            else:
                icon_font = ImageFont.truetype(FontAwesome5FreeSolid, 14)
            letter_text = button_map[count] + ") "
            line_of_text = letter_text + "    "
            line_of_text += name
            _, h = device_list_font.getsize(line_of_text)
            # offset each row in the Y axis
            y = title_h + (count * h) + padding_y
            # String, with space for icon
            draw.text((padding_x, y), line_of_text, self.inky_display.BLACK, font=device_list_font)
            # Icon:
            iw, _ = device_list_font.getsize(letter_text)
            # some magic numbers for positioning icon in empty space between A) and Hallway Lamp (name)
            draw.text((padding_x + iw + 2, y + 4), u'\uf0eb', self.inky_display.BLACK, font=icon_font)
            count += 1

        # Display the completed image
        # print "Setting image..."
        # self.inky_display.set_image(img)
        # print "Showing..."
        # self.inky_display.show()
        # print "Complete!"
        return img

    def on_release(self, event):
        try:
            device = self.devices[event.channel - 1]
            print "[WemoPanel buttonPressed] toggling ", device.name
            device.toggle()
            pub.sendMessage('render')
        except IndexError:
            print "[WemoPanel buttonPressed] No device at channel ", event.channel
            pass