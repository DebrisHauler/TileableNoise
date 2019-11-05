import DiamondSquare
from PIL import Image, ImageDraw

grid = DiamondSquare.Grid(9)

w = grid.size
h = grid.size

#https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
im=Image.new('L', (w,h), 255) # create a new blank image
draw = ImageDraw.Draw(im)
for y in range(grid.size):
    for x in range(grid.size):
        draw.point((x,y),fill=int(grid.data[y][x]))
im.save('ds.png', 'PNG')
im.show()