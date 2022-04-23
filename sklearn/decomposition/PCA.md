---
title: PCA
---

除了 PCA 类以外，最常用的 PCA 相关类还有 KernelPCA 类，它主要用于非线性数据的降维，需要用到核技巧。

另外一个常用的 PCA 相关类是 IncrementalPCA 类，它主要是为了解决单机内存限制的。
IncrementalPCA 先将数据分成多个 batch，然后对每个 batch 依次递增调用 partial_fit 函数，这样一步步的得到最终的样本最优降维。

此外还有 SparsePCA 和 MiniBatchSparsePCA。