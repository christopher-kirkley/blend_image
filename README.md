# Flickr Image Blend #

Command line interface to blend together results from flickr image searches

Image Blend can blend images from a variety of sources:

- Directory
- Flickr

# API Key #

To use, create a config.py file in the root directory.

FLICKR_KEY = (your key here)
FLICKR_SECRET = (your secret here)

# USAGE #

python blend_image.py

-s   Size, takes a tuple of output size
-k   Flickr keyword
-d   Directory to pull images
