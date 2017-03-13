# Laboratorium 1

```python
from skimage import data, io, filters, util, morphology
```

- [data](http://scikit-image.org/docs/dev/api/skimage.data.html) — standardowe obrazy testowe,
- [io](http://scikit-image.org/docs/dev/api/skimage.io.html) — odczytywanie i zapisywanie obrazów

## Wczytywanie, wyświetlanie i zapisywanie plików graficznych

Baza danych

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

Wczytujemy obraz

```
image = data.coins()
```

![](figures/image.PNG)

i dodajemy szum typu pieprz i sól.

```
noisedImage = util.random_noise(image, mode = 's&p')
```

![](figures/noisedImage.PNG)


Filtr gaussowski

```
gau = filters.gaussian(image, sigma = .5)
```

![](figures/gau.PNG)

Filtr medianowy Tworzymy element strukturalny

```
selem = morphology.disk(5)
med = filters.median(image, selem)
```

![](figures/med.PNG)

## Wykrywanie krawędzi

```
sob = filters.sobel(med)
```

![](figures/sob.PNG)

## Dylatacja

![](figures/dil.PNG)

## Erozja

![](figures/ero.png)
