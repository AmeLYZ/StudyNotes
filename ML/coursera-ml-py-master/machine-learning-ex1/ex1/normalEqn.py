import numpy as np

def normal_eqn(X, y):
    theta = np.zeros((X.shape[1], 1))

    # ===================== Your Code Here =====================
    # Instructions : Complete the code to compute the closed form solution
    #                to linear regression and put the result in theta
    #
    
    p1 = np.dot(np.transpose(X), X)
    p2 = np.dot(np.transpose(X), y)
    theta = np.dot(np.array(np.matrix(p1).I), p2)
    
    return theta
