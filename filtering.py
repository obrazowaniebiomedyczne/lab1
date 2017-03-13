#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

print 'Filtering'

# Read
image = io.imread('lena.png')
image = image[:,:,1]
io.imsave('figures/f_image.png', image)

# Structural element
selem = morphology.disk(2)

## Noise
noisedImage = util.random_noise(image, mode = 's&p')
io.imsave('figures/f_noisedImage.png', noisedImage)

## Gaussian
gau = filters.gaussian(noisedImage, sigma = .5)
io.imsave('figures/f_gau.png', gau)

## Median
med = filters.median(noisedImage, selem)
io.imsave('figures/f_med.png', med)
