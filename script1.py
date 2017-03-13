#!/usr/bin/env python
from skimage import util, data, io, filters, morphology

# Read
image = io.imread('lena.png')
image = image[:,:,1]
io.imsave('figures/00_image.png', image)

# Noise
noisedImage = util.random_noise(image, mode = 's&p')
io.imsave('figures/01_noisedImage.png', noisedImage)


# Gaussian
gau = filters.gaussian(noisedImage, sigma = .5)
io.imsave('figures/02_gau.png', gau)

# Median
selem = morphology.disk(5)  # selem
med = filters.median(noisedImage, selem)
io.imsave('figures/03_med.png', med)

# Dilation
dil = morphology.dilation(image, selem)
io.imsave('figures/dil.png', dil)

# Erosion
ero = morphology.erosion(image, selem)
io.imsave('figures/ero.png', ero)

# Sobel
sob = filters.sobel(image)
io.imsave('figures/sob.png', sob)
