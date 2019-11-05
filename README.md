# Tileable Noise
This is my python implementation of the Diamond Square algorithm to generate noisy pngs that tile seamlessly.

![Test Image 1](https://github.com/DebrisHauler/TileableNoise/blob/master/ds.png)

* different everytime
* noise tiles seamlessly
* always refits to use full color spectrum 0-255
* can represent terrain heightmap
* can represent biomes
* can represent caves
* looks like clouds if you remap colors from black-white to skyblue-white
* more fun can be had by applying a smooth step to all the pixels (can help for things like biomes, caves, & clouds)


Sorry for the lack of comments in the code, but I'm throwing this online for people who quickly need some tileable noise.

Made with python 3.6

Dependencies: PIL

You'll have PIL if you're working with the Anaconda.

Just download the two python files to the same folder, then run ImageDrawer.py. ds.png will appear in the directory where you ran it.

Be careful initializing DiamondSquare.Grid() higher than 9 if you muck with the code. If you try 10 for example, then the image width & height is (2^10)+1 and this can take a while.

Generation is single threaded on the cpu. I didn't really need this for real-time purposes. You'll have to wait a few seconds to get an image.
