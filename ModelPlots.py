import numpy as np
import matplotlib.pyplot as plt

class ModelPlots:
    def __init__(self):
        pass

    def plot_image(images: []=[]): # type: ignore
        img1 = np.ones([1, 10, 10, 1])
        img2 = np.ones([1, 10, 10, 1])

        fig, axs = plt.subplots(3, figsize=(10, 10))

        axs[0].imshow(img1[0, :, :, 0], cmap="Blues")
        axs[1].imshow(img2[0, :, :, 0])

        plt.show()