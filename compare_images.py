#
# Install dependencies: pip install scikit-image pillow
#

from skimage.metrics import structural_similarity as ssim
from PIL import Image
import numpy
import sys

FIXED_IMAGE_SIZE = (256, 256)
DEFAULT_THRESHOLD = 0.95

def load_and_prepare(img_path):
    # load and convert to grayscale (mode "L" == grayscale)
    img = Image.open(img_path).convert("L")

    # scale down image to 50% size, than scale to fixed size
    half_size = (int(img.size[0] * 0.5), int(img.size[1] * 0.5))
    img = img.resize(half_size).resize(FIXED_IMAGE_SIZE) 
    return numpy.array(img)

def compare_images(img1_path, img2_path):
    img1 = load_and_prepare(img1_path)
    img2 = load_and_prepare(img2_path)
    return ssim(img1, img2, Full=True)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(f"Usage: python {sys.argv[0]} <image1> <image2> [score_threshold]")
        print(f"score_threshold should be a value between 0 and 1 (default: {DEFAULT_THRESHOLD})")
        sys.exit(1)
    
    threshold = float(sys.argv[3]) if len(sys.argv) == 4 else DEFAULT_THRESHOLD
    img1, img2 = sys.argv[1], sys.argv[2]
    score = compare_images(img1, img2)

    print(f"Similarity score: {score:.2f}")
    if score >= threshold:
        print("Images are similar.")
    else:
        print("Images are NOT similar.")