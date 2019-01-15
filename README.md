# Lil Buddy

Code that powers lil buddy (my home Power and Control tool).

Note: The code is sloppy. Commit messages are nonsense.

## virtualenv

Use virtualenv

    $ source ~/.virtualenv/lilbuddy/bin/activate

pip install -r requirements.txt

## On pi only

Don't use virtualenv (pi comes with specific packages that work - TODO replicate via requirements.txt)

    pip install -r requirements.txt
    sudo pip install einky


TODO:
- Add cleaning method
- left/right panel nav
- start on boot