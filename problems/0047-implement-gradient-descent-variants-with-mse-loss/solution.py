import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    m,n=X.shape
    # weights=weights.copy()
    for epoch in range(n_epochs):
        if method=="batch":
            pred=np.dot(X,weights)
            error=pred-y 
            gradient=(2/m)*np.dot(X.T,error)
            weights=weights-learning_rate*gradient
            
        elif method=="stochastic":
            for i in range(m):
                X_train=X[i:i+1]
                y_train=y[i:i+1]
                pred=np.dot(X_train,weights)
                error=pred-y_train 
                gradient=2*np.dot(X_train.T,error)
                weights=weights-learning_rate*gradient
        elif method=="mini_batch":
            
            for i in range(0,m,batch_size):
                X_train=X[i:i+batch_size]
                y_train=y[i:i+batch_size]
                batch_s=X_train.shape[0]
                pred=np.dot(X_train,weights)
                error=pred-y_train 
                gradient=(2/batch_s)*np.dot(X_train.T,error)
                weights=weights-learning_rate*gradient
            
    return weights    
    # Your code here
    # pass
