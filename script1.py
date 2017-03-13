#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

# Read
image = data.coins()
io.imsave('figures/image.png', image)

# Noise
noisedImage = util.random_noise(image, mode = 's&p')
io.imsave('figures/noisedImage.png', noisedImage)

# Selem
selem = morphology.disk(5)

# Gaussian
gau = filters.gaussian(noisedImage, sigma = .5)
io.imsave('figures/gau.png', gau)

# Median
med = filters.median(noisedImage, selem)
io.imsave('figures/med.png', med)

# Dilation
dil = morphology.dilation(image, selem)
io.imsave('figures/dil.png', dil)

# Erosion
ero = morphology.erosion(image, selem)
io.imsave('figures/ero.png', ero)

# Sobel
sob = filters.sobel(image)
io.imsave('figures/sob.png', sob)
