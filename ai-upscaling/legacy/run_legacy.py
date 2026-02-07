import cv2
from upscaler import (
    upscale_bilinear,
    upscale_bicubic,
    upscale_lanczos
)

# ---------------- Configuration ----------------
INPUT_IMAGE_PATH = "input_lr.png"
SCALE_FACTORS = [2, 3, 4]
OUTPUT_PREFIX = "output"
# -----------------------------------------------


def main():
    image = cv2.imread(INPUT_IMAGE_PATH)

    if image is None:
        raise FileNotFoundError(
            f"Could not load input image: {INPUT_IMAGE_PATH}"
        )

    for scale in SCALE_FACTORS:
        bilinear = upscale_bilinear(image, scale)
        bicubic = upscale_bicubic(image, scale)
        lanczos = upscale_lanczos(image, scale)

        cv2.imwrite(f"{OUTPUT_PREFIX}_bilinear_x{scale}.png", bilinear)
        cv2.imwrite(f"{OUTPUT_PREFIX}_bicubic_x{scale}.png", bicubic)
        cv2.imwrite(f"{OUTPUT_PREFIX}_lanczos_x{scale}.png", lanczos)

        print(f"Saved outputs for {scale}x upscaling")


if __name__ == "__main__":
    main()
