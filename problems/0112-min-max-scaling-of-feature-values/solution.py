def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    mini=min(x)
    maxa=max(x)
    return list(map(lambda x:(x-mini)/(maxa-mini),x))
    # Your code here
    # pass