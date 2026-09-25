import numpy as np

def to_categorical(x, n_col=None):
    en = []
    if n_col is None:
        n_col = np.max(x) + 1
    for e in x:
        b = np.zeros(n_col)
        b[e] = 1
        en.append(b.tolist())
    return en