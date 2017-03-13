#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

image = io.imread('lena.png')
image = image[:,:,1]
io.imsave('figures/image.png', image)

noisedImage = util.random_noise(image, mode = 's&p')
io.imsave('figures/noisedImage.png', noisedImage)

strel = morphology.disk(5)
io.imsave('figures/strel.png', strel)

gau = filters.gaussian(noisedImage, sigma = .5)
io.imsave('figures/gau.png', gau)

med = filters.median(noisedImage, strel)
io.imsave('figures/med.png', med)
