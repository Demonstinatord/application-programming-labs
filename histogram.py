import matplotlib.pyplot as plt
import numpy as np


def get_data_imgs(img: np.ndarray) -> tuple:
    """
    This function extracts data from an image, namely, collects a list of the number of pixels from
    a certain brightness according to the formula, that is, creates a histogram, and receives size data
    this picture. After that, it enters all the received data into the tuple and returns it.
    This function also displays a scale of the data extraction progress:
        Building histogram:
        |###############################                      |
    It is needed to understand how long it will take to extract data
    :param img: an array with RGB data of the values of each pixel obtained using OpenCV
    :return histogram_data: tuple of image data(histogram, width, height)
    """
    height = img.shape[0]
    width = img.shape[1]

    if len(img.shape) == 3:
        return color_hist_data(img, height, width)
    if len(img.shape) == 2:
        return gray_hist_data(img, height, width)


def gray_hist_data (img: np.array, height, width) -> tuple:
    """
    this function return grayscale image data
    :param img:
    :param height:
    :param width:
    :return tuple:
    """
    gr = []

    for i in range(0, 256):
        gr.append(0)

    for x in range(0, height):
        for y in range(0, width):
            gr[img[x, y]] += 1

    return (gr,)


def color_hist_data(img: np.array, height: int, width: int) -> tuple:
    """
    this function return color image data
    :param img:
    :param height:
    :param width:
    :return tuple:
    """
    rp = []
    gp = []
    bp = []

    for i in range(0, 256):
        rp.append(0)
        gp.append(0)
        bp.append(0)

    for x in range(0, height):
        for y in range(0, width):
            rp[img[x, y][2]] += 1
            gp[img[x, y][1]] += 1
            bp[img[x, y][0]] += 1

    return (rp, gp, bp)


def hist_display(hist: tuple) -> None:
    """
    This function creates and shows the histogram
    :param hist: data for histogram
    """

    try:
        fig,axs = plt.subplots(len(hist))
        fig.suptitle("Histogram")
        if len(hist) > 1:
            for i in range(0,len(hist)):
                if i == 0:
                    name = "red"
                if i == 1:
                    name = "green"
                if i == 2:
                    name = "blue"


                y = np.linspace(0, len(hist[i])-1, len(hist[i]))
                x = hist[i]

                axs[i].plot(y,x, label=f'histogram {name}', color=f'{name}')
                axs[i].set_title(f"{name} ")
                axs[i].set_xlabel("кол-во пикселей")
                axs[i].set_ylabel('Яркость')
                axs[i].axhline(0, color=f'{name}', linewidth=0.5, ls='--')
                axs[i].axvline(0, color=f'{name}', linewidth=0.5, ls='--')
        if len(hist) == 1:
            y = np.linspace(0, len(hist[0]) - 1, len(hist[0]))
            x = hist[0]
            name="gray"
            axs.plot(y, x, label=f'histogram {name}', color=f'{name}')
            axs.set_title(f"{name} ")
            axs.set_ylabel("кол-во пикселей")
            axs.set_xlabel('Яркость')
            axs.axhline(0, color=f'{name}', linewidth=0.5, ls='--')
            axs.axvline(0, color=f'{name}', linewidth=0.5, ls='--')

        plt.show()
    except Exception as ex:
        raise Exception("histogram is not created: ", ex)