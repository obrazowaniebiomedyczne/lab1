#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

print 'Morphological operations'

# Read
image = data.chelsea()
image = image[:,:,1]
io.imsave('figures/m_image.png', image)

# Structural element
selem = morphology.disk(4)

## Dilation
dil = morphology.dilation(image, selem)
io.imsave('figures/m_dil.png', dil)

## Erosion
ero = morphology.erosion(image, selem)
io.imsave('figures/m_ero.png', ero)
