#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

print 'Morphological operations'

# Read
image = io.imread('lena.png')
image = image[:,:,1]
io.imsave('figures/00_image.png', image)

# Structural element
selem = morphology.disk(2)

## Dilation
dil = morphology.dilation(image, selem)
io.imsave('figures/dil.png', dil)

## Erosion
ero = morphology.erosion(image, selem)
io.imsave('figures/ero.png', ero)

# Sobel
sob = filters.sobel(image)
io.imsave('figures/sob.png', sob)
