# --- cell 1 ---
import numpy as np


def split_and_baseline(X, y, train_frac, val_frac, test_frac, seed=None):
    """Split rows into train/val/test folds, fit something on the training fold, predict the test fold.

    Returns
    -------
    test_predictions : np.ndarray, shape (len(test_idx),)
    train_idx, val_idx, test_idx : 1-D integer arrays forming a partition of range(len(y))
    """
    y = np.asarray(y).ravel()
    n = len(y)
    rng = np.random.default_rng(seed)
    indices = np.arange(n, dtype=int)
    rng.shuffle(indices)

    train_pos = int(n * train_frac)
    val_pos = train_pos + int(n * val_frac)

    train_idx = indices[:train_pos]
    val_idx = indices[train_pos:val_pos]
    test_idx = indices[val_pos:] 
    X_train, y_train = X[train_idx], y[train_idx]
    X_test = X[test_idx]
    x_mean = np.mean(X_train, axis=0)
    x_std = np.std(X_train, axis=0) + 1e-8

    X_train_scaled = (X_train - x_mean) / x_std
    X_test_scaled = (X_test - x_mean) / x_std
    X_b = np.c_[np.ones((X_train_scaled.shape[0], 1)), X_train_scaled]
    X_test_b = np.c_[np.ones((X_test_scaled.shape[0], 1)), X_test_scaled]

    alpha = 1.0
    I = np.eye(X_b.shape[1])
    I[0, 0] = 0.0 

    weights = np.linalg.solve(X_b.T @ X_b + alpha * I, X_b.T @ y_train)
    predictions = X_test_b @ weights
    test_predictions = np.asarray(predictions).flatten()

    return test_predictions, train_idx, val_idx, test_idx