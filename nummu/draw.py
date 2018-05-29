import numpy as np
from PIL import Image, ImageDraw, ImageFont

def _get_rect(x, y, width, height, angle):
    rect = np.array([(0, 0), (width, 0), (width, height), (0, height), (0, 0)])
    theta = (np.pi / 180.0) * angle
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    offset = np.array([x, y])
    transformed_rect = np.dot(rect, R) + offset
    return transformed_rect

def rect(pallete, x, y, w, h, angle=0, color=0):
    img = Image.fromarray(pallete)
    draw = ImageDraw.Draw(img)
    _rect = _get_rect(x, y, w, h, angle)
    draw.polygon([tuple(p) for p in _rect], fill=color)
    pallete[:, :, :] = np.asarray(img)
