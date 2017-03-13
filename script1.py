#!/usr/bin/env python
from skimage import data, io, filters

print 'Hello!'

imageFromDataset = data.coins()
imageFromFile = io.imread('lena.png')

io.imshow(imageFromFile)
io.show()
