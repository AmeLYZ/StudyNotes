import numpy as np
from sigmoid import *


def cost_function_reg(theta, X, y, lmd):
    m = y.size

    # You need to return the following values correctly
    cost = 0
    grad = np.zeros(theta.shape)

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta
    #                You should set cost and grad correctly.
    #
    
    h = sigmoid(np.dot(X, theta))
    
    # no penalty for theta0
    
    cost = 1./m * np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h)) 
    cost = cost + lmd/(2.*m) * np.dot(theta,theta) - lmd/(2.*m) * theta[0]**2
    
    loss = h - y
    grad = 1./m * np.dot(np.transpose(X), loss) + lmd / (1.*m) * theta
    grad[0] -= lmd / (1.*m) * theta[0]
    
    # ===========================================================

    return cost, grad
