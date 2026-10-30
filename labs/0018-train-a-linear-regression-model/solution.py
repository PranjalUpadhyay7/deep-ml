# --- cell 1 ---
import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.
    # pass
    epoch=1000
    alpha=0.01
    m = X.shape[0]
    
    for i in range(epoch):
        # W is 1D, so np.dot(X, W) works cleanly without .T
        pred = np.dot(X, W) + b
        error = pred - y
        
        # Calculate gradients
        gradient_w = (1 / m) * np.dot(X.T, error)
        # FIX: Sum the errors to keep bias a single scalar value
        gradient_b = (1 / m) * np.sum(error)
        
        # Update parameters
        W = W - alpha * gradient_w
        b = b - alpha * gradient_b
        
    return W, float(b)