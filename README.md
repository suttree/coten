# coten

# .plan:
- Using code from https://github.com/lvzon/kindle-clippings/blob/master/extract-kindle-clippings.py
-   Open kindle quote file
-       Shuffle list and iterate through
-           reject duplicates, empties and too-long quotes
-       Create an image from the quote
- Display the image on the screen (eink: https://github.com/pimoroni/inky)


11/4/20
- Review https://github.com/pimoroni/inky/blob/master/examples/clean.py
- Update script to use https://github.com/pimoroni/inky/blob/master/examples/what/quotes-what.py

# Installation:

brew install python3
Maybe? pip install requirements.txt
Or pip install pillow

# Links:
https://github.com/lvzon/kindle-clippings

https://code-maven.com/create-images-with-python-pil-pillow

https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil

http://tsaith.github.io/combine-images-into-a-video-with-python-3-and-opencv-3.html

https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python/44948030

https://medium.com/@enriqueav/how-to-create-video-animations-using-python-and-opencv-881b18e41397

# Setup:
pip install virtualenv
virtualenv env --python=python3.6
source env/bin/activate
pip install numpy
pip install opencv-python

# Questions:
Output to USB drive or run via a Raspberry Pi Zero?
