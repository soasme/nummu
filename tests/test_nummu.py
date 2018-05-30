import numpy as np
from nummu import draw


def test_rect_in_one_pixel():
    pallete = np.zeros((1, 1, 3), dtype=np.uint8)
    draw.rect(pallete, 0, 0, 1, 1, color=(255, 255, 255))
    np.testing.assert_array_equal(pallete, [[[255, 255, 255]]])
