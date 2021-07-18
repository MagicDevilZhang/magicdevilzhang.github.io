---
layout: post
title: PyTorch使用手册
permalink: /docs/人工智能/PyTorch/PyTorch使用手册
---
# 基本数据结构Tensor

## 构造Constructor

```python
# From list / NumPy array
x = torch.tensor([[1, -1], [-1, 1]])
x = torch.from_numpy(np.array([[1, -1], [-1, 1]]))

# Zero tensor
x = torch.zeros([2, 2])

# Unit tensor
x = torch.ones([1, 2, 5])
```

## 操作Operators

- `squeeze(arg)`: 表示第arg维的维度值为1，则去掉该维度。否则tensor不变。（即若tensor.shape()[arg] = 1，则去掉该维度）

```python
>>> x = torch.zeros([1, 2, 3])
>>> x.shape
torch.Size([1, 2, 3])

>>> x = x.squeeze(0)
>>> x.shape
torch.Size([2, 3])
```

- `unsqueeze(arg)`: 表示在第arg维增加一个维度值为1的维度。

 ```python
>>> x = torch.zeros([2, 3])
>>> x.shape
torch.Size([2, 3])

>>> x = x.unsqueeze(1)
>>> x.shape
torch.Size([2, 1, 3])
 ```

- `transpose(arg)`: 矩阵转置。

```python
>>> x = torch.zeros([2, 3])
>>> x.shape
torch.Size([2, 3])

>>> x = x.transpose(0, 1)
>>> x.shape
torch.Size([3, 2])
```

- `cat(arg)`: 矩阵连接。

```python
>>> x = torch.zeros([2, 1, 3])
>>> y = torch.zeros([2, 3, 3])
>>> z = torch.zeros([2, 2, 3])
>>> w = torch.cat([x, y, z], dim=1)
>>> w.shape
torch.Size([2, 6, 3])
```

- 其他操作

```python
z = x + y  #Addition
z = x - y  #Subtraction
y = x.pow(2) #Power
y = x.sum()  #Summation
y = x.mean()  #Mean
```

### 使用设备Devices

```python
torch.cuda.is_available()
x = x.to('cpu')
x = x.to('cuda')
```

### 计算微分Gradient

```python
>>> x = torch.tensor([[1., 0.], [-1., 1.]], requires_grad=True) 
>>> z = x.pow(2).sum()
>>> z.backward()
>>> x.grad
tensor([[ 2., 0.], [-2., 2.]])
```


## PyTorch训练DNN过程


### 定义Dataset & Dataloader

```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, file):
        self.data = ...
        
    def __getitem__(self, index):
        return self.data[index]
        
    def __len__(self):
        return len(self.data)


dataset = MyDataset(file)
dataloader = DataLoader(dataset, batch_size, shuffle=True)
```




## 定义Neural Network Layers

```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(10, 32), # Fully-connected Layer
            nn.Sigmoid(), # nn.ReLU()
            nn.Linear(32, 1)  # Fully-connected Layer
        )
        self.criterion = nn.MSELoss() #nn.CrossEntropyLoss()

    def forward(self, x):
        return self.net(x)
        
    def call_loss(self, predict, target):
        return self.criterion(predict, target)


torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
```

## 训练过程Trainning

```python
dataset = MyDataset(file)
tr_set = DataLoader(dataset, 16, shuffle=True)
model = MyModel().to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), 0.1)

for epoch in range(n_epochs):
    #Training Set
    model.train()
    for x, y in tr_set:
        optimizer.zero_grad()
        x, y = x.to(device), y.to(device)
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        optimizer.step()
        
    #Validation Set
    model.eval()
    total_loss = 0
    for x, y in dv_set:
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            pred = model(x)
            loss = criterion(pred, y)
            total_loss += loss.cpu().item() * len(x)
    avg_loss = total_loss / len(dv_set.dataset)

    #Testing Set
    model.eval()
    preds = []
    for x in tt_set: x = x.to(device)
        with torch.no_grad():
        pred = model(x)
        preds.append(pred.cpu())

```

### 模型的保存与载入

```python
# Save
torch.save(model.state_dict(), path)

# Load
ckpt = torch.load(path)
model.load_state_dict(ckpt)
```

## Regression样例

```python
import csv
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


class Covid19Dataset(torch.utils.data.Dataset):
    data: torch.Tensor()
    target: torch.Tensor()
    mode: str

    def __init__(self, path, mode):
        with open(path, 'r') as fp:
            source = np.array(list(csv.reader(fp))[1:])[:, 1:].astype(float)
            if mode == 'train':
                self.data = torch.FloatTensor(source)[:, list(range(93))]
                self.target = torch.FloatTensor(source)[:, -1]
                self.mode = 'train'
            elif mode == 'dev':
                self.data = torch.FloatTensor(source)[::5, list(range(93))]
                self.target = torch.FloatTensor(source)[::5, -1]
                self.mode = 'dev'
            elif mode == 'test':
                self.data = torch.FloatTensor(source)[:, list(range(93))]
                self.mode = 'test'
            else:
                raise Exception("mode error")

        self.data[:, 40:] = \
            (self.data[:, 40:] - self.data[:, 40:].mean(dim=0, keepdim=True)) \
            / self.data[:, 40:].std(dim=0, keepdim=True)

    def __getitem__(self, index):
        if not self.mode == 'test':
            return self.data[index], self.target[index]
        else:
            return self.data[index]

    def __len__(self):
        return len(self.data)


class RegressionModel(torch.nn.Module):
    net: torch.nn.Sequential()
    criterion: torch.nn.MSELoss()

    def __init__(self, n_feature, n_hidden, n_ouput):
        super(RegressionModel, self).__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(n_feature, n_hidden),
            torch.nn.ReLU(),
            torch.nn.Linear(n_hidden, n_ouput)
        )
        self.criterion = torch.nn.MSELoss(reduction="mean")

    def forward(self, x):
        return self.net(x).squeeze(1)

    def loss(self, predict, target):
        return self.criterion(predict, target)


tr_set = DataLoader(dataset=Covid19Dataset(path='../data/covid.train.csv', mode='train'), batch_size=300, shuffle=True)
dev_set = DataLoader(dataset=Covid19Dataset(path='../data/covid.train.csv', mode='dev'), batch_size=300, shuffle=True)
test_set = DataLoader(dataset=Covid19Dataset(path='../data/covid.test.csv', mode='test'), batch_size=300, shuffle=False)

model = RegressionModel(n_feature=93, n_hidden=256, n_ouput=1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

min_mse = 1000

for epoch in range(3000):
    model.train()
    for x, y in tr_set:
        optimizer.zero_grad()
        pred = model(x)
        loss = model.loss(pred, y)
        loss.backward()
        optimizer.step()

    model.eval()
    total_loss = 0
    for x, y in dev_set:
        with torch.no_grad():
            pred = model(x)
            loss = model.loss(pred, y)
        total_loss += loss.detach().item() * len(x)
    total_loss = total_loss / len(tr_set.dataset)
    if min_mse > total_loss:
        min_mse = total_loss
        torch.save(model.state_dict(), 'regression_model')
        print("train {}, loss {:.5f}".format(epoch, min_mse))

model.eval()
preds = []
for x in test_set:
    with torch.no_grad():
        pred = model(x)
        preds.append(pred.detach().cpu())
preds = torch.cat(preds, dim=0).numpy()
print(preds)

```

# 参考链接
- [PyTorch 官方文档](https://pytorch.org/docs/stable/index.html)
- [李宏毅 Pytorch Tutorial](https://speech.ee.ntu.edu.tw/~hylee/ml/ml2021-course-data/hw/Pytorch/Pytorch_Tutorial_1.pdf)
- [李宏毅 PyTorch Youtube 视频课](https://www.youtube.com/watch?v=8DaeP2vSu90)
- [李宏毅 PyTorch Bilibili 视频课](https://www.bilibili.com/video/BV1Wv411h7kN?p=5)