import numpy as np
from sigmoid import *

def predict(theta1, theta2, x):
    # Useful values
    m = x.shape[0]
    num_labels = theta2.shape[0]

    # You need to return the following variable correctly
    p = np.zeros(m)

    # ===================== Your Code Here =====================
    # Instructions : Complete the following code to make predictions using
    #                your learned neural network. You should set p to a
    #                1-D array containing labels between 1 to num_labels.
    #
    
    inp_l = np.c_[np.ones(m), x]
    
    hid_l = sigmoid(np.dot(inp_l, np.transpose(theta1)))
    hid_l = np.c_[np.ones(m), hid_l]
    
    out_l = sigmoid(np.dot(hid_l, np.transpose(theta2)))
    p = np.argmax(out_l, axis=1) + 1
    
    return p


