def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a=matrix
    dete= a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if dete==0:
        return None
    else:
        return  [[a[1][1]/dete,-a[0][1]/dete],[-a[1][0]/dete,a[0][0]/dete]]
    # Your code here
    # pass