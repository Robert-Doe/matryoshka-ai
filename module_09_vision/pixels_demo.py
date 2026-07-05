"""
pixels_demo.py  —  Module 09

The one idea that unlocks computer vision: AN IMAGE IS JUST A GRID OF NUMBERS.
A grayscale image is a 2-D array of brightness values (0=black, 255=white). A
color image is three such grids stacked (Red, Green, Blue). Once you see images
as arrays, every vision operation becomes arithmetic you already know.

Run:  python module_09_vision/pixels_demo.py
"""

import numpy as np

line = lambda: print("-" * 56)

# 1. BUILD a tiny 8x8 grayscale image by hand: a bright square on dark background.
img = np.zeros((8, 8), dtype=int)
img[2:6, 2:6] = 200          # a bright square
img[3:5, 3:5] = 255          # brighter center
print("1) A grayscale image IS a 2-D array of brightness (0-255):")
print(img)
line()

# 2. VISUALIZE it as text so you can SEE the numbers are a picture.
print("2) The same array, drawn with characters (darker number = darker char):")
ramp = " .:-=+*#%@"
for row in img:
    print("   " + "".join(ramp[min(len(ramp) - 1, v * len(ramp) // 256)] for v in row))
print("   >> Those numbers ARE the square. Vision models see exactly this.")
line()

# 3. IMAGE OPERATIONS = array math (Module 02 broadcasting).
print("3) Editing an image = array arithmetic:")
brighter = np.clip(img + 40, 0, 255)
inverted = 255 - img
threshold = (img > 128).astype(int) * 255      # simple segmentation
print(f"   brighten: add 40 and clip. center pixel {img[4,4]} -> {brighter[4,4]}")
print(f"   invert:   255 - value.    corner pixel {img[0,0]} -> {inverted[0,0]}")
print("   threshold (>128 -> white): a 1-line 'segmentation'")
for row in threshold:
    print("   " + "".join("#" if v else "." for v in row))
line()

# 4. COLOR = 3 stacked grids (channels). Shape (H, W, 3).
print("4) A COLOR image is 3 grids stacked: Red, Green, Blue.")
color = np.zeros((4, 4, 3), dtype=int)
color[:, :, 0] = 255          # full red channel
print(f"   a 4x4 all-red image has shape {color.shape}")
print(f"   pixel [0,0] = {color[0,0].tolist()}  (R=255, G=0, B=0 -> pure red)")
print("   A photo from your phone is just a big version of this: HxWx3 numbers.")
line()

print("""
Why this matters:
  * Every vision model's input is an array of pixel numbers — nothing more.
  * 'Features' like edges and shapes are patterns WITHIN those numbers, which we
    extract with convolution (next: convolution_demo.py).
  * A 1000x1000 color image is 3,000,000 numbers — too many to feed a plain neural
    net efficiently. That problem is exactly what CNNs solve.
""")
