import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """

    m= len(data)
    data= data[np.random.default_rng(seed).permutation(m)]

    train_end=int(m*train_frac)
    validation_end=train_end+int(m*validation_frac)

    train=data[:train_end]
    validation=data[train_end:validation_end]
    test=data[validation_end:]
    return [train,validation, test]
    # Your code here
    # pass