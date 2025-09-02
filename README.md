<div align="center">

# `image_compare`
<p>
<h5><code>image_compare</code> is a small python script to check if two
image look similar based a similarity score and threshold</h5>
</p>
</div>

## Dependencies:
image_compare uses [scikit-image](https://github.com/scikit-image/scikit-image) and [pillow](https://github.com/python-pillow/Pillow), to install them type
```bash
pip install scikit-image pillow
```
## Usage:
```bash
python image_compare.py <image1> <image2> [score_threshold]
```

Note that all input images are internally converted to grayscale, scaled to 50% then scaled again
 to a fixed size. This means that even with a score of 1.0, images are not necessarily identical.

The script will return 0 to the shell if the score is above the threshold, or 1 if below.

