#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

image = data.coins()
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

binary = dil > .5
io.imsave('figures/binary.png', binary)

io.imshow(dil)
io.show()
