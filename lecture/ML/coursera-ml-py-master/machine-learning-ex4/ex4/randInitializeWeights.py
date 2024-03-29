import numpy as np


def rand_initialization(l_in, l_out):
    # You need to return the following variable correctly
    w = np.zeros((l_out, 1 + l_in))

    # ===================== Your Code Here =====================
    # Instructions : Initialize w randomly so that we break the symmetry while
    #                training the neural network
    #
    # Note : The first column of w corresponds to the parameters for the bias unit
    #
    
    epsolon_init = 0.12
    w = np.random.rand(l_out, 1 + l_in) * 2 * epsolon_init - epsolon_init

    # ===========================================================

    return w
