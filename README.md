# Lil Buddy

Code that powers lil buddy (my home Power and Control tool).

Note: The code is sloppy. Commit messages are nonsense.

## Credits:

- pywemo, for the wemo api in python
- the folks at [pimoroni](https://github.com/pimoroni) for the hardware and the software

## virtualenv

Use virtualenv

    $ source ~/.virtualenv/lilbuddy/bin/activate

pip install -r requirements.txt

## On pi only

Don't use virtualenv (pi comes with specific packages that work - TODO replicate via requirements.txt)

    pip install -r requirements.txt
    sudo pip install einky
    sudo apt-get install python-touchphat # or pip; also there's python3 versions

## Troubleshooting

Sometimes the pHAT screen won't update.  Not sure why.  Power cycling Pi is required to fix it.

TODO:
- Add cleaning method
- left/right panel nav
- start on boot

rsync -avzh -e ssh . pi@192.168.0.105:~/rsync-dest/lilbuddy

## PubSub Events

`add_image` - Adds a PIL image to the quote-unquote frame buffer, takes PIL image as input
`render` - triggers a re-render of current panel (eg: useful if button tapped and state changed)


## Links

touch pHAT https://github.com/pimoroni/touch-phat
enable some stuff
- https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all