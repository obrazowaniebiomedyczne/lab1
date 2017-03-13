#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

image = io.imread('lena.png')
image = image[:,:,1]
io.imsave('figures/image.png', image)

noisedImage = util.random_noise(image, mode = 's&p')
io.imsave('figures/noisedImage.png', noisedImage)

selem = morphology.disk(8)

gau = filters.gaussian(noisedImage, sigma = .5)
io.imsave('figures/gau.png', gau)

med = filters.median(noisedImage, selem)
io.imsave('figures/med.png', med)

sob = filters.sobel(image)
io.imsave('figures/sob.png', sob)

dil = morphology.dilation(sob, selem)
io.imsave('figures/dil.png', dil)

ero = morphology.erosion(sob, selem)
io.imsave('figures/ero.png', ero)
