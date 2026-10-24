import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    gradient=[]
    for i in range(x.shape[0]):
        x_ip=x.copy()
        x_ip[i]+=epsilon
        x_in=x.copy()
        x_in[i]-=epsilon
        gradient.append((f(x_ip)-f(x_in))/(2*epsilon))
    t_grad=np.linalg.norm(analytical_grad)
    c_grad=np.linalg.norm(gradient)
    denominator = t_grad+ c_grad
    numerator=np.linalg.norm((analytical_grad-gradient))
    if denominator==0:
        return gradient,0.0
    else:
        return gradient, numerator/denominator
    # Your code here
    # pass