import matplotlib.pyplot as plt
import numpy as np

def plot_data(X, y):
    plt.figure()

    # ===================== Your Code Here =====================
    # Instructions : Plot the positive and negative examples on a
    #                2D plot, using the marker="+" for the positive
    #                examples and marker="o" for the negative examples
    #
    
    pos = np.where(y == 1)
    neg = np.where(y == 0)
    
    plt.scatter(X[pos, 0], X[pos, 1], c = 'b', marker = '+')
    plt.scatter(X[neg, 0], X[neg, 1], c = 'y', marker = 'o')
