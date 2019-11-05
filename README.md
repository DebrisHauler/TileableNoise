# TileableNoise
Python implementation of the Diamond Square to generate noisy pngs that tile seamlessly.

Sorry for the lack of comments, but I'm throwing this online for people who quickly need some tileable noise.

Made with python 3.6

Just download the two python files to the same folder, then run ImageDrawer.py. ds.png will appear in the directory where you ran it.

Be careful initializing DiamondSquare.Grid higher than 9 if you muck with the code. If you try 10 for example, then the image width & height is (2^10)+1.

Generation is single threaded on the cpu. I didn't really need this for real-time purposes. You'll have to wait a few seconds to get an image.
