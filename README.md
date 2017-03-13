# Laboratorium 1

```python
from skimage import data, io, filters, util, morphology
```

- [data](http://scikit-image.org/docs/dev/api/skimage.data.html) — standardowe obrazy testowe,
- [io](http://scikit-image.org/docs/dev/api/skimage.io.html) — odczytywanie i zapisywanie obrazów

## Wczytywanie, wyświetlanie i zapisywanie plików graficznych

Baza danych

http://scikit-image.org/docs/dev/api/skimage.data.html

```python
image = data.coins()
```

Plik

```python
image = io.imread('lena.png')
```

Wyświetlenie

```python
io.imshow(image)
io.show()
```

![](figures/ss1.png)

Zapis do pliku.

```python
io.imsave('foo.png', image)
```


## Filtrowanie

Wczytujemy obraz, ograniczamy go tylko do kanału zielonego i dodajemy szum.

```
image = io.imread('lena.png')
image = image[:,:,1]
```

![](figures/image.png)

```
noisedImage = util.random_noise(image, mode = 's&p')
```

![](figures/noisedImage.png)


Filtr gaussowski

```
gau = filters.gaussian(image, sigma = .5)
```

![](figures/gau.png)

Filtr medianowy Tworzymy element strukturalny

```
selem = morphology.disk(5)
med = filters.median(image, selem)
```

![](figures/med.png)

## Wykrywanie krawędzi

```
sob = filters.sobel(med)
```

![](figures/sob.png)

## Dylatacja

![](figures/dil.png)

## Erozja
