if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dezero.datasets import Spiral
from dezero import DataLoader

import numpy as np
import dezero.functions as F

batch_size = 10
max_epoch = 1

train_set = Spiral(train = True)
test_set = Spiral(train = False)
train_loader = DataLoader(train_set, batch_size)
test_loader = DataLoader(test_set, batch_size, shuffle= False)

for epoch in range(max_epoch):
    for x, t in train_loader:
        print(x.shape, t.shape)
        break

    for x,t in test_loader:
        print(x.shape, t.shape)
        break




y = np.array([[0.2, 0.8, 0], [0.1, 0.9, 0],[0.8, 0.1, 0.1]])
t = np.array([1,2,0])
acc = F.accuracy(y,t)
print(acc)