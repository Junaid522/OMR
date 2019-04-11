from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu

from skimage import measure

import matplotlib.pyplot as plt

original = imread('https://i.stack.imgur.com/nkQpj.png')

original = original[1278:2082, 599:1006].copy()

blurred = gaussian(original, sigma=.8)

binary = blurred > threshold_otsu(blurred)

labels = measure.label(binary)

plots = {'Original': original, 'Blurred': blurred,
         'Binary': binary, 'Labels': labels}

fig, ax = plt.subplots(1, len(plots))

for n, (title, img) in enumerate(plots.items()):

    cmap = plt.cm.gnuplot if n == len(plots) - 1 else plt.cm.gray
    ax[n].imshow(img, cmap=cmap)
    ax[n].axis('off')
    ax[n].set_title(title)

plt.show(fig)

props = measure.regionprops(labels)

for prop in props:
    print('Label: {} >> Object Size: {}'.format(prop.label, prop.area))