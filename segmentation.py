#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

print 'Morphological operations'

# Read
image = data.coins()
io.imsave('figures/s_image.png', image)
