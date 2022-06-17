import numpy as np


def feature_normalize(X):
    # You need to set these values correctly
    n = X.shape[1]  # the number of features
    X_norm = np.zeros(X.shape)
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0, ddof=1)

    # ===================== Your Code Here =====================
    # Instructions : First, for each feature dimension, compute the mean
    #                of the feature and subtract it from the dataset,
    #                storing the mean value in mu. Next, compute the
    #                standard deviation of each feature and divide
    #                each feature by its standard deviation, storing
    #                the standard deviation in sigma
    #
    #                Note that X is a 2D array where each column is a
    #                feature and each row is an example. You need
    #                to perform the normalization separately for
    #                each feature.
    #
    # Hint: You might find the 'np.mean' and 'np.std' functions useful.
    #       To get the same result as Octave 'std', use np.std(X, 0, ddof=1)
    #

    # X_normalization = (X - mu)/sigma

    for i in range(n):
        X_norm[:, i] = (X[:, i]-mu[i])/sigma[i]

    # ===========================================================

    return X_norm, mu, sigma
