---
layout: post
title: 联邦学习 Federated Learning
permalink: /docs/人工智能/DNN理论/联邦学习FederatedLearning
---

# 联邦学习

联邦学习需要解决的问题是：如何在**不上传数据**的情况下，利用边缘设备的算力，对模型进行**训练并共享**。

联邦学习和传统分布式学习的区别在于：

1. 用户节点作为worker对数据进行计算，不需要将数据分发到服务器或其他节点；
2. 用户节点worker并不稳定，数据可能呈现**非独立同分布(non-IID)**，数据分布可能在不同节点具有**偏移性**；
3. 用户节点worker和服务器server的**通信代价**远大于计算代价。



# Communication-Efficiency

提高通信效率的核心理念在于**“多做计算少做通信”**。



# Privacy

需要保证用于训练的用户数据在用户**本地被训练**，并且保证不能通过训练模型的梯度或参数**逆向推理**。



# FedAVG

[FedAVG](http://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf)是在边缘节点Worker将本地数据经过 1~5 epoch 训练后，将更新的权重发送到Server进行**加权**平均后，重新发送回边缘节点Worker。

目标函数（最小化经验损失）：$ \min{\sum_{k=1}^K\frac{n_k}{n}F_k(w)}$, where $F_k(w)=\frac{1}{n_k}L_k(w)$

---
**Server executes:**

​    initialize $w_0$

​    for each round $t = 1, 2, . . .$ do

​        $m ← max(C · K, 1)$​  // a fixed set of $K$​ clients, a random fraction $C$​ of clients is selected

​        $St ← (random\;set\;of\;m\;clients)$

​        for each client $k ∈ St$ in parallel do

​            $w_{t+1}^k ← ClientUpdate(k, w_t)$​

​        $w_{t+1}← \sum_{k=1}^K(\frac{n_k}{n}w_{t+1}^k)$​​



**ClientUpdate($k$​​, $w$​​): **

​    $B ← (split\;P_k\;into\;batches\;of\;size\;B)$​

​    for each local epoch $i$ from $1$ to $E$ do

​        for batch $b ∈ B$ do

​            $w ← w − η·g(w,b)$​

​    return $w$ to server 

---



# FedProx

[FedProx](https://arxiv.org/abs/1812.06127)是对FedAVG的补充，其为了使边缘节点Worker更新**不要太远离初始Global Model**，减少Non-IID的影响。

目标函数（最小化经验损失）：$ \min{\sum_{k=1}^K\frac{n_k}{n}F_k(w)}$​, where $F_k(w)=\frac{1}{n_k}L_k(w)+\frac{\mu}{2}||w-w_t||^2$​

---
**Server executes:**

​    initialize $w_0$

​    for each round $t = 1, 2, . . .$ do

​        $m ← max(C · K, 1)$​  // a fixed set of $K$​ clients, a random fraction $C$​ of clients is selected

​        $St ← (random\;set\;of\;m\;clients)$

​        for each client $k ∈ St$ in parallel do

​            $w_{t+1}^k ← ClientUpdate(k, w_t)$​

​        $w_{t+1}← \sum_{k=1}^K(\frac{n_k}{n}w_{t+1}^k)$​​



**ClientUpdate($k$​​, $w$​​): **

​    $B ← (split\;P_k\;into\;batches\;of\;size\;B)$​

​    for each local epoch $i$ from $1$ to $E$ do

​        for batch $b ∈ B$ do

​            $w = argmin(\frac{1}{n_k}L'_k(w)+\frac{\mu}{2}||w-w_t||^2)$​

​    return $w$ to server 

---



# FedCurv

[FedCurv](http://www.edgify.ai/wp-content/uploads/2020/04/Overcoming-Forgetting-in-Federated-Learning-on-Non-IID-Data.pdf)是**联邦学习**对**连续学习EWC算法**的适用场景。对于第$k$​个节点的$t$​个任务，其损失函数可以定义为：

$L_{t,k}(\theta) = L'_k(\theta) + \lambda\sum_{j\in{K/k}}(\theta-\hat{\theta}_{t-1,j})^TF_{t-1,j}(\theta-\hat{\theta}_{t-1,j})$​​​

---
**Server executes:**

​    for each round $t = 1, 2, . . .$ do

​        $m ← max(C · K, 1)$​  // a fixed set of $K$​ clients, a random fraction $C$​ of clients is selected

​        $St ← (random\;set\;of\;m\;clients)$​

​        $\theta_{t}← \sum_{k=1}^K(\frac{n_k}{n}\theta_{t-1}^k)$​​

​        for each client $k ∈ St$ in parallel do

​            $\theta_{t+1}^k,F^k_{t+1} ← ClientUpdate(k, \theta_t,F_t)$​​​​​​​​​​​

​       ​​​

**ClientUpdate($k$​​​​, $\theta$​, $F$​​​​): **

​    $B ← (split\;P_k\;into\;batches\;of\;size\;B)$​

​    for each local epoch $i$ from $1$ to $E$ do

​        for batch $b ∈ B$ do

​            $\theta = argmin(L'(\theta) + \lambda\sum_{j\in{K/k}}(\theta-\hat{\theta}_{t-1,j})^TF_{t-1,j}(\theta-\hat{\theta}_{t-1,j}))$​

​    return $\theta_{t+1}^k,F^k_{t+1}$ to server 

---

