import cv2


def upscale_bilinear(image, scale):
    """
    Upscale an image using bilinear interpolation.
    """
    h, w = image.shape[:2]
    return cv2.resize(
        image,
        (w * scale, h * scale),
        interpolation=cv2.INTER_LINEAR
    )


def upscale_bicubic(image, scale):
    """
    Upscale an image using bicubic interpolation.
    """
    h, w = image.shape[:2]
    return cv2.resize(
        image,
        (w * scale, h * scale),
        interpolation=cv2.INTER_CUBIC
    )


def upscale_lanczos(image, scale):
    """
    Upscale an image using Lanczos resampling.
    """
    h, w = image.shape[:2]
    return cv2.resize(
        image,
        (w * scale, h * scale),
        interpolation=cv2.INTER_LANCZOS4
    )
