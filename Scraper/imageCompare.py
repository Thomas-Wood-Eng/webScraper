import requests
import cv2
from io import BytesIO
import numpy as np
from skimage.metrics import structural_similarity as ssim
from scipy import signal
from scipy.ndimage import uniform_filter

#Thanks Chat
def ssim(image1, image2, win_size=11, L=255):
    # Ensure images are numpy arrays
    image1 = np.array(image1)
    image2 = np.array(image2)

    # Calculate constants for SSIM
    K1 = 0.01
    K2 = 0.03
    C1 = (K1 * L) ** 2
    C2 = (K2 * L) ** 2

    # Calculate means, variances, and covariances
    mu1 = uniform_filter(image1, win_size)
    mu2 = uniform_filter(image2, win_size)
    mu1_sq = mu1 * mu1
    mu2_sq = mu2 * mu2
    mu12 = mu1 * mu2
    sigma1_sq = uniform_filter(image1 * image1, win_size) - mu1_sq
    sigma2_sq = uniform_filter(image2 * image2, win_size) - mu2_sq
    sigma12 = uniform_filter(image1 * image2, win_size) - mu12

    # Calculate SSIM
    num = (2 * mu12 + C1) * (2 * sigma12 + C2)
    den = (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)
    ssim_map = num / den
    ssim_score = np.mean(ssim_map)

    return ssim_score

def compare_images(image1, image2):
    # Load images
    if isinstance(image1, str):
        image1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    if isinstance(image2, str):
        image2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    # Resize the smaller image to match the dimensions of the larger image
    if image1.shape != image2.shape:
        min_height = min(image1.shape[0], image2.shape[0])
        min_width = min(image1.shape[1], image2.shape[1])
        image1 = cv2.resize(image1, (min_width, min_height), interpolation=cv2.INTER_LINEAR)
        image2 = cv2.resize(image2, (min_width, min_height), interpolation=cv2.INTER_LINEAR)

    # Compute SSIM
    similarity_score = ssim(image1, image2)
    return similarity_score

# Example usage:
# Example usage:
if __name__ == "__main__":
    # File paths for the images in the Downloads folder
    image_path1 = "C:/Users/thoma/Downloads/0002529300100_00.jpg"
    image_path2 = "C:/Users/thoma/Downloads/21062620_front_a01_@2.png"

    # Read the images and perform the comparison
    similarity_score = compare_images(image_path1, image_path2)
    print(f"Similarity between {image_path1} and {image_path2}: {similarity_score}")