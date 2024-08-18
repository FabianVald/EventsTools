import cv2
import numpy as np

def canny(image):
    if image is None:
        raise ValueError("La imagen no se ha cargado correctamente.")
    
    if image.dtype != 'uint8':
        image = cv2.convertScaleAbs(image)
    
    edges = cv2.Canny(image, 0, 2,apertureSize=5, L2gradient=True)
    
    return edges


def GaussianBlur_(image):
    if image is None:
        raise ValueError("La imagen no se ha cargado correctamente.")
    
    if image.dtype != 'uint8':
        image = cv2.convertScaleAbs(image)

    blurred_image = cv2.GaussianBlur(image, (3, 3), 0.5)
        
    return blurred_image


def dilated_(image,kernel_size=3, iterations=1):
    if image is None:
        raise ValueError("La imagen no se ha cargado correctamente.")
    
    if image.dtype != 'uint8':
        image = cv2.convertScaleAbs(image)
        
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    
    return dilated_image

def eroded_(image, kernel_size=3, iterations=1):
    if image is None:
        raise ValueError("La imagen no se ha cargado correctamente.")
    
    if image.dtype != 'uint8':
        image = cv2.convertScaleAbs(image)
        
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=iterations)
    
    return eroded_image

def median_(image):
    if image is None:
        raise ValueError("La imagen no se ha cargado correctamente.")
    
    if image.dtype != 'uint8':
        image = cv2.convertScaleAbs(image)
        
    image = cv2.medianBlur(image, 3)
    return image 