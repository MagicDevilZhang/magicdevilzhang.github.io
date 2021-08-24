---
layout: post
title: 连续学习 Continual Learning
permalink: /docs/人工智能/DNN理论/连续学习ContinualLearning
---

# Scenarios for continual learning

- Three scenarios for continual learning: https://arxiv.org/pdf/1904.07734.pdf


# Strategies for Continual Learning

- Task-specific Components

  连续学习过程中，在模型上选出特定的子网络（Sub-network）去应对特定的任务，从而抑制灾难性遗忘。这种策略仅限于Task-IL连续学习场景下，也就是说必须明确任务标识（Task Identity）才能正确候选特定的子网络（Sub-network）。

  - Context-dependent Gating, XdG
  - Hard Attention To the Task, HAT: http://proceedings.mlr.press/v80/serra18a/serra18a.pdf

- Regularized Optimization

  在训练新的任务时，为了防止对之前任务的灾难性遗忘，限制神经网络上某些权重的更新弹性。这种策略适用于测试过程中任务标识不明确的场景下。

  - Elastic Weight Consolidation, EWC: https://arxiv.org/abs/1612.00796
  - Synaptic Intelligence, SI: https://arxiv.org/abs/1703.04200
  - Memory Aware Synapses, MAS: https://arxiv.org/abs/1711.09601
  - RWalk: https://arxiv.org/abs/1801.10112
  - Sliced Cramer Preservation, SCP: https://openreview.net/forum?id=BJge3TNKwH

- Modifying Training Data

  - Learning without Forgetting, LwF: 
  - Deep Generative Replay, DGR:

- Using Exemplars
  - iCaRL

