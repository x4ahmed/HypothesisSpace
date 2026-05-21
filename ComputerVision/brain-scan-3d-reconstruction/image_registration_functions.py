import numpy as np
import cv2
from scipy.spatial.distance import cdist
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

def get_affine_transformation(points_in, points_out):
    """
    TODO for students:
    Estimate the affine transformation matrix mapped from points_in to points_out.
    Transform the input points to homogenous coordinates and solve the least-squares problem.
    """
    # transform to homogenous coordinates

    # solve the least-squares problem A.T@Ax = A.Tb
    pass

def transform_points(points, matrix):
    """
    TODO for students:
    Given a set of 2D points, apply the transformation matrix.
    Return the new (x, y) coordinates.
    """
    # homogneous coordinates

    # transform the points
    pass

def backwards_mapping(image, output_shape, transformation, background=0):
    """
    TODO for students:
    Apply a backward mapping transformation to the input image.
    """
    # create the points of the new image

    # transform the points into the original image

    # remove all points, that land outside the original image

    # write the pixel values at the correct location
    output_image = np.zeros(output_shape, dtype=image.dtype)
    return output_image

def downsample_bilinear(img, factor):
    """
    TODO for students:
    Downsample a grayscale image by the given factor using bilinear interpolation.
    """
    pass

def histogram_equalization(img):
    """
    TODO for students:
    Compute histogram equalization mapping from an image.
    Return the equalized image.
    """
    pass

def convolve2d(img, kernel):
    """
    TODO: Apply a 2D convolution (without padding, assumes odd kernel).
    
    Parameters:
        img (np.ndarray): Grayscale image.
        kernel (np.ndarray): 2D filter kernel.
    
    Returns:
        np.ndarray: Convolved image (same size as input, zero-padded).
    """
    pass

def sobel_filter(img):
    """
    TODO: Apply Sobel edge detection filter (magnitude of gradients).
    
    Parameters:
        img (np.ndarray): Grayscale image.
    
    Returns:
        np.ndarray: Sobel gradient magnitude image.
    """
    pass

def filter_wrapper_fn(img, mode, kernel_size=3, sigma=1.0):
    """
    TODO Apply one of the following filters to the image: mean, median, gaussian, sobel.

    Parameters:
        img (np.ndarray): Grayscale image.
        mode (str): One of "mean", "median", "gaussian", "sobel"
        kernel_size (int): Kernel size (must be odd)
        sigma (float): Gaussian std dev (only used for gaussian)
    
    Returns:
        np.ndarray: Filtered image.
    """
    pass

def get_keypoints(image, filtering=True, sigma=3):
    """
    Extracts keypoints from the image. 
    You might want to optionally smooth the image with a gaussian filter first.
    """
    if filtering:
        image = gaussian_filter(image, sigma=sigma)
    
    return keypoints, descriptors

def intersect2d(array1, array2):
    """ Helper to get intersection of row matches """
    test = array1[:, None] == array2
    return array2[np.all(test.mean(0) > 0, axis=1)]

def matching(descriptors_1, descriptors_2, max_ratio=0.7, cross_checking=True):
    """
    TODO:
    Matches the descriptors against each other.
    Returns the best match for each descriptor, if it is significant.
    The significance is defined by the max_ratio: distance_1 / distance_2 < max_ratio.
    Optional cross-checking of matches.
    """

    # cross_checking
    if cross_checking:
        final_matches2 = np.stack(
            (np.arange(descriptors_2.shape[0])[mask2], matches2[mask2, 0]),
        ).T
    if cross_checking:
        # return the intersection of the two matches arrays (invert final_matches2 to point in the same direction)
        final_matches = intersect2d(final_matches, final_matches2[:, ::-1])
    return final_matches

def ransac(points_in, points_out, matches, percentage_outliers=0.5, probability=0.99, cutoff=20, k=3):
    """
    TODO:
    Implement Random Sample Consensus to predict a robust affine model on a set with outliers.
    """
    # return the inliers
    return matches[inlier_best], support_best

def helper_plot_fn(img1, img2, transformed_img2):
    """ Plotting helper """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(img1, cmap='gray')
    axes[0].set_title("Source Image")
    axes[1].imshow(img2, cmap='gray')
    axes[1].set_title("Destination Image")
    axes[2].imshow(transformed_img2, cmap='gray')
    axes[2].set_title("Transformed Image")
    plt.tight_layout()
    plt.show()
