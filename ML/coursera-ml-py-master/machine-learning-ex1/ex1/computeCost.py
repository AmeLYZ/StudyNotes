import numpy as np


def compute_cost(X, y, theta):
    # Initialize some useful values
    m = y.size
    cost = 0

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta.
    #                You should set the variable "cost" to the correct value.
    
    diff = np.dot(X, theta) - y
    cost = (1./(2 * m) * np.dot(np.transpose(diff), diff))
    
    # ==========================================================

    return cost
