import numpy as np
from sigmoid import *


def nn_cost_function(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lmd):
    # Reshape nn_params back into the parameters theta1 and theta2, the weight 2-D arrays
    # for our two layer neural network
    theta1 = nn_params[:hidden_layer_size * (input_layer_size + 1)].reshape(hidden_layer_size, input_layer_size + 1)
    theta2 = nn_params[hidden_layer_size * (input_layer_size + 1):].reshape(num_labels, hidden_layer_size + 1)

    # Useful value
    m = y.size

    # You need to return the following variables correctly
    cost = 0
    theta1_grad = np.zeros(theta1.shape)  # 25 x 401
    theta2_grad = np.zeros(theta2.shape)  # 10 x 26

    # ===================== Your Code Here =====================
    # Instructions : You should complete the code by working thru the
    #                following parts
    #
    # Part 1 : Feedforward the neural network and return the cost in the
    #          variable cost. After implementing Part 1, you can verify that your
    #          cost function computation is correct by running ex4.py
    #
    # Part 2: Implement the backpropagation algorithm to compute the gradients
    #         theta1_grad and theta2_grad. You should return the partial derivatives of
    #         the cost function with respect to theta1 and theta2 in theta1_grad and
    #         theta2_grad, respectively. After implementing Part 2, you can check
    #         that your implementation is correct by running checkNNGradients
    #
    #         Note: The vector y passed into the function is a vector of labels
    #               containing values from 1..K. You need to map this vector into a 
    #               binary vector of 1's and 0's to be used with the neural network
    #               cost function.
    #
    #         Hint: We recommend implementing backpropagation using a for-loop
    #               over the training examples if you are implementing it for the 
    #               first time.
    #
    # Part 3: Implement regularization with the cost function and gradients.
    #
    #         Hint: You can implement this around the code for
    #               backpropagation. That is, you can compute the gradients for
    #               the regularization separately and then add them to theta1_grad
    #               and theta2_grad from Part 2.
    #

    # Part 1
    h = np.eye(10)
    y = h[y-1, :]
    
    a1 = np.c_[np.ones(m), X]
    
    z2 = np.dot(a1, np.transpose(theta1))
    a2 = np.c_[np.ones(z2.shape[0]), sigmoid(z2)]
    
    a3 = sigmoid(np.dot(a2, np.transpose(theta2)))
    
    cost = -1./m * np.sum(y * np.log(a3) + (1 - y) * np.log(1-a3))
    cost += lmd/(2.*m) * (np.sum(theta1[:, 1:]**2) + np.sum(theta2[:, 1:]**2))
    
    # Part 2
    delta3 = a3 - y
    delta2 = np.dot(delta3, theta2)[:, 1:] * sigmoid(z2)
    
    delta_1 = np.zeros(theta1.shape)
    delta_2 = np.zeros(theta2.shape)
    
    delta_1 = delta_1 + np.dot(np.transpose(delta2), a1)  # (25L, 401L)
    delta_2 = delta_2 + np.dot(np.transpose(delta3), a2)  # (10L, 26L)
    
    theta1_grad = (1./m * delta_1) + (lmd/m * theta1)
    theta2_grad = (1./m * delta_2) + (lmd/m * theta2)
    
    theta1_grad[:, 1] = theta1_grad[:, 1] - (lmd/m * (theta1[:, 1]))
    theta2_grad[:, 1] = theta2_grad[:, 1] - (lmd/m * (theta2[:, 1]))
    # ====================================================================================
    # Unroll gradients
    grad = np.concatenate([theta1_grad.flatten(), theta2_grad.flatten()])
    
    return cost, grad
