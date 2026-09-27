---
layout: default
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> 从 5 条内容中筛选出 2 条重要资讯。

---

1. [DeepSeek DSec：160 个 EPYC 节点上并发运行 38 万个沙箱](#item-1) ⭐️ 7.0/10
2. [Reladraw：让你自己决定元素位置的新型图表语言](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DeepSeek DSec：160 个 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978) ⭐️ 7.0/10

DeepSeek 发布论文介绍 DeepSeek Elastic Compute（DSec）：这是一个生产级沙箱平台，通过统一的 SDK 对外提供 FnCall、容器、microVM 与完整虚拟机四类沙箱后端，并宣称在 160 个基于 AMD EPYC 的服务器节点上实现了 38 万个沙箱的并发运行。该论文另一个引发关注之处是异常庞大的作者名单——列出的作者超过 131 人，据说还有数十人未能列出。 沙箱容量是强化学习后训练、智能体评测以及大规模智能体部署的核心瓶颈，因此一个能在相对小规模集群上支撑数十万隔离环境的生产系统，对 AI 基础设施生态来说是一个有分量的扩容数据点。这也表明 DeepSeek 正在投入智能体类产品所需的底层执行基座，而不只是模型权重。 其核心设计亮点是统一 SDK 抽象出四种隔离级别——纯函数调用、容器、microVM 和完整虚拟机——让调用方可以按工作负载在启动延迟与隔离强度之间取舍；AMD 顶配的 EPYC 9005 系列单路可达 192 核，这意味着 38 万这一数字很大程度上依赖于每个节点上密集打包大量轻量级沙箱。需要注意的局限是，这属于自述性质的生产报告而非第三方独立基准测试，而且社区的注意力基本绕过了技术指标，集中在作者名单这一异常现象上。

hackernews · shenli3514 · 9月26日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=49859112)

**背景**: 沙箱是一种隔离的执行环境，允许不受信任或由机器生成的代码运行而不危及宿主机。隔离强度从共享宿主内核的轻量级容器，到加入硬件虚拟化边界的 microVM（例如 Firecracker 一类的设计），再到拥有独立客户机操作系统的完整虚拟机。AI 智能体系统之所以需要这项能力，是因为智能体会不断生成并执行代码、调用工具、运行评测，而每个此类任务最好都在各自独立的、可随时丢弃的隔离实例中运行。“FnCall”后端指的是把单次函数调用隔离执行，而不必为每次调用都启动一个完整的容器或虚拟机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22978">[2609.22978] DeepSeek Elastic Compute (DSec): A Sandbox ...</a></li>
<li><a href="https://arxiv.org/html/2609.22978v1">DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48940231">Scaling to 1M concurrent sandboxes in seconds - Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（156 分、42 条评论）观点不一：几位评论者对规模本身印象深刻，有人称在 160 个 EPYC 节点上跑 38 万个并发沙箱是“ crazy stuff”；另一些人则聚焦于 131 人的作者名单，认为这可能是一种人才保留或“资产保护”策略，让竞争对手无从判断该挖走谁，并打趣说真正值得关注的是 131 人如何协作把论文发出来。还有少数评论者联想到更阴暗的可能性，怀疑这套基础设施是否也能支撑 38 万个智能体组成的群体，也有人直接发问这是否就是所谓的“智能体基座”。

**标签**: `#distributed-systems`, `#cloud-infrastructure`, `#sandboxing`, `#DeepSeek`, `#scalability`

---

<a id="item-2"></a>
## [Reladraw：让你自己决定元素位置的新型图表语言](https://github.com/reladraw/reladraw) ⭐️ 7.0/10

Reladraw 是一种全新的文本化图表语言，让用户可以显式控制各个元素的摆放位置，而不是把布局完全交给自动布局引擎。它提供了无需安装的在线 playground，同时给出简单的 npm 安装方式，以及可供 Claude 等 AI 智能体使用的 agent 技能包。 它切中了当前工具生态中的一个真实痛点：Mermaid 和 Graphviz 由引擎自动摆放节点，结果难以预测；而 Draw.io 虽然可控，但操作耗时且不利于智能体操作。借助让图表既便于人工编辑又便于机器读取，Reladraw 顺应了 AI 辅助编程时代「以图表作为对齐工具」工作流的增长需求——开发者与智能体需要一个共享的可视化模型。 该语言采用相对定位而非精确坐标，作者认为这通常已经足够，同时还能保持格式的可预测性和可读性。早期社区测试也暴露出一些粗糙之处，有用户反馈像 \`edge parser -&gt; renderer &quot;test edge&quot; from: left to: right\` 这样的简单连线并没有被渲染成弯曲箭头，说明连线路由逻辑仍有待完善。

hackernews · jpwalsh234 · 9月26日 17:10 · [社区讨论](https://news.ycombinator.com/item?id=49858513)

**背景**: 「图表即代码」类工具允许用纯文本描述图表，而不必手工绘制，这使得图表可以被纳入版本控制，也便于脚本或 AI 智能体生成。主流工具 Mermaid 和 Graphviz 都使用自动布局引擎：你只需描述元素之间的关系，由引擎决定坐标，这对结构化图表效果好，但在大型自由流程图里常常显得凌乱。像 Draw.io 这样的拖拽式编辑器提供完全的控制力，但操作全靠手工、十分耗时，而且其文件格式也很难让智能体理解和处理。Reladraw 试图占据中间地带：既保留声明式、对智能体友好的语法，又允许作者指定元素的位置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.skills.sh/reladraw/reladraw/reladraw">reladraw — reladraw / reladraw</a></li>
<li><a href="https://alto.gab.com/feed/hacker-news-best/item/433456">Show HN: Reladraw – A diagram language where you decide... | Alto</a></li>
<li><a href="https://contentbuffer.com/news/reladraw-new-text-language-diagrams-without-installation-36075cbc">reladraw : A New Text Language for Diagrams ... — ContentBuffer News</a></li>

</ul>
</details>

**社区讨论**: 评论区总体相当热情，认为它处在 Mermaid 与 Draw.io 之间的理想位置，并指出 Mermaid 在时序图、甘特图等固定布局图表上表现出色，但对位置至关重要的流程图则效果不佳。有人建议把语言的拓扑部分（连线、分组等）与布局问题解耦，从而让它能充当 C4 模型的布局层；还有多位用户表示会把它加入自己智能体的图表工具集。最主要的批评集中在连线路由的 bug 上，也有评论者好奇智能体自身能否很好地生成复杂图表。

**标签**: `#diagramming`, `#developer-tools`, `#DSL`, `#AI-agents`, `#visualization`

---