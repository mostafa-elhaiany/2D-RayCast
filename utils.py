import numpy as np

def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm  # normalized matrix
    return matrix

def dir_from_angle(angle):
    radians = np.radians(angle)
    direction = np.array([np.cos(radians), np.sin(radians)])
    return normalize_2d(direction)
