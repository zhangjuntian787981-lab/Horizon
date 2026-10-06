---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 15 条内容中筛选出 2 条重要资讯。

---

1. [Reflection 发布 Beam：5010 亿参数开源稀疏 MoE 模型](#item-1) ⭐️ 7.0/10
2. [Dust：无需反向传播即可预训练 Transformer](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Reflection 发布 Beam：5010 亿参数开源稀疏 MoE 模型](https://reflection.ai/blog/introducing-beam) ⭐️ 7.0/10

Reflection AI 发布了 Beam，这是一个开放权重的稀疏混合专家（MoE）语言模型，总参数量为 5010 亿，每个 token 激活 230 亿参数，主打编程、推理和智能体（agentic）任务。该公司称 Beam 在约 23.8 万亿个经过筛选的高质量 token 上完成预训练，并进一步通过强化学习进行优化，同时公布了将其与同量级当代模型对比的基准测试结果。 一个总参数达 5010 亿、但每 token 仅激活 230 亿的开放权重模型，对开源权重生态意义重大：它在保留超大模型容量的同时，把推理成本压到接近中等规模稠密模型的水平。这也加剧了各家实验室在大规模稀疏 MoE 权重上的竞争，并为自托管团队在编程与智能体工作流上提供了新选择——前提是他们愿意相信厂商的说法。 Beam 采用稀疏 MoE 架构，即每个 token 只激活一小部分专家子网络，因此 5010 亿总参数需要全部载入内存，而实际决定算力开销的只有 230 亿参数；社区将其与同量级的 DeepSeek V4.1 Flash 对比时指出，Beam 的预训练 token 数更少，且不包含 n-gram/PLE 之类的额外参数。值得注意的是，此次发布并未附带 Reflection 此前承诺过的透明度复盘报告（postmortem）。

hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 混合专家（MoE）是一种模型架构，其中包含许多独立的“专家”子网络，以及一个为每个输入只挑选少数专家的路由器。这一设计把“总参数”（必须全部载入内存的部分）与“激活参数”（每个 token 实际使用的一小部分）区分开，后者决定算力开销与推理速度。开放权重发布意味着任何人都可以下载并自行运行模型，与只提供 API 的闭源模型形成对比；Reflection AI 此前因其 Reflection 70B 模型受到质疑，用户指控该模型暗中把请求转发给 Anthropic 的 Claude。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters : What’s the Difference?</a></li>
<li><a href="https://spanvero.com/learn/active-vs-total-params/">Active vs total parameters — what it means (open AI models )...</a></li>
<li><a href="https://arxiv.org/html/2507.11181v1">Mixture of Experts in Large Language Models</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论褒贬不一：有人欢迎又一款开放权重模型，并注意到它在近期一道谜题上声称的泛化表现；但也有不少人怀疑 Beam 是否像此前的 Reflection 70B 那样，又是一个套壳 Claude 的产品。还有人指出，公司当初承诺的复盘报告始终没有出现，并至少有一位用户提到，帖子里若干有实质内容的问题似乎被折叠或标记为 dead。

**标签**: `#large-language-models`, `#open-weights`, `#mixture-of-experts`, `#model-release`, `#ai-ethics`

---

<a id="item-2"></a>
## [Dust：无需反向传播即可预训练 Transformer](https://qlabs.sh/research/dust) ⭐️ 7.0/10

一项名为 Dust 的研究（发布在 qlabs.sh/research/dust）证明，GPT 风格的 Transformer 可以在完全没有反向传播的情况下完成预训练，改用一种不依赖反向传播的优化方法。作者在 FineWeb 数据集上使用 4096 词表的 BPE 分词器，以 16k token 的批次（8 条 2048 token 的序列）训练一个 epoch，采用带动量的 SGD 和恒定学习率，并报告 Dust 在大规模种群下能很好地逼近反向传播，在多种设置下甚至超过它。 几十年来，反向传播几乎一直是深度神经网络训练的通用算法，因此一个可信的、面向 Transformer 的无反向传播预训练方法，暗示着大模型训练方式可能发生范式转变。如果该方法能够扩展，它有望支持比反向传播那种串行依赖链更容易在多设备上并行的训练模式，这对所有训练大语言模型的人都很重要。 取舍非常明确：Dust 需要的算力远高于反向传播，但并行性要好得多，并且比权重空间的进化策略（ES）高效几个数量级。Dust 在某些设置下能超过反向传播这一结果，暗示在算力充裕的场景中，它有可能不只是追平、而是超越反向传播。

hackernews · E-Reverance · 10月5日 21:15 · [社区讨论](https://news.ycombinator.com/item?id=49970871)

**背景**: 反向传播是训练神经网络的标准算法：它把预测误差沿网络反向传播，利用链式法则计算梯度，并通过更新权重来最小化损失。Transformer 是当今大多数语言模型所采用的神经网络架构，其核心是注意力机制——将每个 query 与每个 key 进行比较，从而生成具有上下文感知的表示。由于反向传播的更新依赖于“先前向、再反向”的串行过程，它很难并行；而进化策略类方法则是扰动并评估大量候选参数集，这类方法天然易于并行，但通常样本效率低得多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qlabs.sh/research/dust">Dust : Pretraining Transformers Without Backpropagation</a></li>
<li><a href="https://developers.google.com/machine-learning/crash-course/neural-networks/backpropagation">Neural Networks: Training using backpropagation | Machine Learning</a></li>
<li><a href="https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/">Transformers in Machine Learning - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（115 分、19 条评论）基本切题但偏推测性：有人询问能否采用混合方案——用该方法对已有的反向传播训练检查点进行微调，从而获得额外收益，并建议把它应用到不同训练阶段以观察对学习轨迹的影响。另一位评论者较公允地总结了取舍：算力效率不如反向传播，但更容易并行；还有人开了个轻松的玩笑（“more than meets the eye”）。整个讨论提出了关于算力成本和混合微调的合理疑问，但缺乏深入的技术辩论，作者也未参与互动。

**标签**: `#transformers`, `#training-methods`, `#backpropagation`, `#machine-learning-research`, `#parallelization`

---