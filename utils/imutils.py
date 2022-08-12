import random
import numpy as np
from random import randint


def hwc_to_chw(image):
    """Covert the input image from HWC format (Height, Width, Channel) to CHW
    format (Channel, Height, Width).

    Parameters
    ----------
    image: numpy.ndarray
        Input image.

    Returns
    -------
    image: numpy.ndarray
        Converted image.
    """

    image = np.transpose(image, (2, 0, 1))
    return image




def random_crop(images, crop_size, default_values):
    """
    Randomly crop an array of images and make them become dimensioned
    (crop_size, crop_size).

    Parameters
    ----------
    images : numpy.ndarray of numpy.ndarray
        Array of images to crop.
    crop_size : int
        Target height and width of the cropped images.
    default_values : int ranging from 0 to 255
        Color in grey-scale used to fill image borders in case the crop_size
        is larger than the image size.

    Returns
    -------
    list of numpy.ndarray or numpy.ndarray
        List of cropped images. If the input array contains only one element
        a single image is returned.
    """
    if isinstance(images, np.ndarray):
        images = (images,)

    if isinstance(default_values, int):
        default_values = (default_values, )

    image_size = images[0].shape[:2]
    box = get_random_crop_box(image_size, crop_size)

    new_images = list()

    for img, default_value in zip(images, default_values):
        if len(img.shape) == 3:
            cont = np.ones(
                (crop_size, crop_size, img.shape[2]), img.dtype) * default_value
        else:
            cont = np.ones((crop_size, crop_size), img.dtype) * default_value
        cont[box[0]:box[1], box[2]:box[3]] = img[box[4]:box[5], box[6]:box[7]]

        new_images.append(cont)

    if len(new_images) == 1:
        new_images = new_images[0]

    return new_images


def random_flip(img):
    num = randint(0, 3)
    if num == 0:
        return img
    elif num == 1:
        if isinstance(img, tuple):
            return [np.fliplr(m).copy() for m in img]
        else:
            return np.fliplr(img).copy()
    elif num == 2:
        if isinstance(img, tuple):
            return [np.flipud(m).copy() for m in img]
        else:
            return np.flipud(img).copy()
    elif num == 3:
        if isinstance(img, tuple):
            return [np.flipud(np.fliplr(m)).copy() for m in img]
        else:
            return np.flipud(np.fliplr(img)).copy()



def random_resize_long(img, min_long, max_long):
    target_long = random.randint(min_long, max_long)
    h, w = img.shape[:2]

    if w < h:
        scale = target_long / h
    else:
        scale = target_long / w

    return rescale_image(img, scale, 3)


def random_scale(img, scale_range, order):

    target_scale = scale_range[0] + \
        random.random() * (scale_range[1] - scale_range[0])

    if isinstance(img, tuple):
        return (pil_rescale(img[0], target_scale, order[0]), pil_rescale(img[1], target_scale, order[1]))
    else:
        return pil_rescale(img[0], target_scale, order)



def top_left_crop(img, cropsize, default_value):

    h, w = img.shape[:2]

    ch = min(cropsize, h)
    cw = min(cropsize, w)

    if len(img.shape) == 2:
        container = np.ones((cropsize, cropsize), img.dtype)*default_value
    else:
        container = np.ones(
            (cropsize, cropsize, img.shape[2]), img.dtype)*default_value

    container[:ch, :cw] = img[:ch, :cw]

    return container
