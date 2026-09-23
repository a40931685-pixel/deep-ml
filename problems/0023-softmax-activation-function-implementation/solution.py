import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores=np.array(scores)
    scores =np.exp(scores-np.max(scores))
    s=np.sum(scores)
    return (scores/s).tolist()
    pass