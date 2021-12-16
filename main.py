import numpy as np
import torch 

if __name__ == '__main__':
    x = torch.Tensor(np.array([[1,2,3],[4,5,6]]))
    y = torch.rand((2,3))
    z = x + y
    print(z)

