import cv2
import numpy as np
import matplotlib.pyplot as plt

data = np.load('train_test_data.npz')

test_data = data['test_data']
train_data = data['train_data']
