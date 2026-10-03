---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 17 条内容中筛选出 2 条重要资讯。

---

1. [新 AI 以更低训练成本首次击败人类顶尖 Stratego 选手](#item-1) ⭐️ 8.0/10
2. [Greg Kroah-Hartman 剖析 LLM 发现的内核漏洞与安全炒作](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [新 AI 以更低训练成本首次击败人类顶尖 Stratego 选手](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

一套新的 AI 系统在一对一对局中击败了人类历史上最强的 Stratego 选手，其棋力超过了 DeepMind 在 2022 年提出的 DeepNash，而训练所用的对局数量却减少了约 34 倍。相关成果发表在《Nature》上，并有配套论文发布在 arXiv（2511.07312）。 Stratego 属于非完美信息博弈，这类问题会让 AlphaGo、AlphaZero 所依赖的朴素前瞻搜索失效，因此这里的突破意味着在信息不完全条件下做决策的研究取得了更广泛的进展。同时在训练算力大幅减少的情况下击败顶尖人类选手，也说明这类方法正变得更便宜、更具实用价值，其意义不限于棋类游戏。 该《Nature》论文描述的智能体把学习到的博弈模型与对隐藏状态的搜索结合起来，作者特别强调了其样本效率：对局数量约为 DeepNash 的 1/34，但最终棋力更强。与所有博弈类成果一样，这一成绩受限于所采用的具体 Stratego 规则与版本，也不会自动迁移到状态空间大得多的现实问题中。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**背景**: Stratego 是一款 1946 年问世的两人棋盘游戏，双方的棋子对对手都是隐藏的，因此玩家必须在不完全了解对方布阵的情况下行动。国际象棋和围棋属于“完美信息”博弈——所有信息都可见——AI 可以假设对手会做出最优应对，从而进行前瞻搜索。而在 Stratego、扑克这类非完美信息博弈中，这一假设不成立，因为一步棋的价值取决于你看不到的棋子，这使得传统基于搜索的 AI 面临大得多的困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/mastering-stratego-the-classic-game-of-imperfect-information/">Mastering Stratego, the classic game of imperfect information</a></li>
<li><a href="https://arxiv.org/abs/2206.15378">Mastering the Game of Stratego with Model-Free Multiagent ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stratego">Stratego - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这是一项真正的里程碑，其中一条高赞评论解释了为什么隐藏信息会让朴素的前瞻搜索失效：一步棋的好坏取决于玩家无法知道的事实。也有人从历史角度指出，DeepMind 在 2022 年宣称的 Stratego“掌握”似乎并未真正超越人类；此外还有不少评论是关于童年游戏经历、甚至给棋子做记号作弊的怀旧故事。

**标签**: `#AI`, `#game-playing`, `#imperfect-information`, `#reinforcement-learning`, `#research-breakthrough`

---

<a id="item-2"></a>
## [Greg Kroah-Hartman 剖析 LLM 发现的内核漏洞与安全炒作](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

在 Kernel Recipes 2026 上，Linux 内核维护者 Greg Kroah-Hartman 发表了题为《Security in the LLM Age》的演讲，逐条拆解了 Anthropic 声称其 Mythos 模型发现的 79 个内核漏洞：其中 24 个只有“某个东西崩溃了”而毫无细节，14 个根本不是漏洞，3 个是凭空捏造的数据，15 个在最新版本中早已修复，真正需要修复的只有约 20 个。他把整场宣传的成果总结为大约相当于一小时的内核开发工作量。 这是全球最大开源项目的顶级维护者首次对某家 AI 厂商的漏洞发现“战绩”进行可核查的详细审计，而此时维护者们本就已被 AI 生成的大量漏洞报告淹没。它直接挑战了“LLM 正在发现海量严重安全缺陷”的叙事，也暴露出 AI 实验室的安全宣传与其实际工程贡献之间的尴尬落差。 即便在真正值得修复的约 20 项发现中，也有多项依赖不现实的前提——其中 7 项假定攻击者能提供恶意文件系统镜像，另一些则假定可以注入特殊输入；此外 Kroah-Hartman 指出，Anthropic 并未向 Mythos 所“模式匹配”的那些原始补丁作者署名致谢。演讲的核心技术指控是：该模型主要是复用过去几十年已有的修复模式，并检查这些修复是否被普遍应用，而非推理出全新类别的缺陷。

hackernews · usernomdeguerre · 10月2日 02:51 · [社区讨论](https://news.ycombinator.com/item?id=49929391)

**背景**: Greg Kroah-Hartman 是 Linux 内核稳定版与长期支持版分支的维护者，因此他对内核漏洞修复、CVE 编号分配以及协调漏洞披露（coordinated vulnerability disclosure）的实际运作最具发言权。Kernel Recipes 是每年在巴黎举行的内核开发者会议，聚焦真实的开发与安全实践。“LLM 发现的漏洞”指的是用大语言模型扫描源代码并生成候选漏洞报告，这种做法自 2024 年以来迅速普及，一些项目表示其产生的报告数量已远超人类的分诊能力。与此同时，Anthropic、OpenAI 等 AI 实验室不断把自身安全研究与模型能力和风险的宣称捆绑在一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.xda-developers.com/canonical-is-speeding-up-ubuntus-kernel-updates-because-its-drowning-in-ai-discovered-bugs/">Canonical is speeding up Ubuntu&#x27;s kernel updates because it&#x27;s ...</a></li>
<li><a href="https://socket.dev/blog/ai-slop-polluting-bug-bounty-platforms">AI Slop Is Polluting Bug Bounty Platforms with Fake Vulnerability ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍感谢 Kroah-Hartman 的坦率，以及他让这些说法可以借助公开的 Linux 内核记录被核实；有人特别指出其中的“强烈反差”：这些实验室一边宣称自家模型危险到不能全面发布，一边又高调宣传并不算亮眼的漏洞发现成果。多人指出 Mythos 本质上只是在几十年历史补丁之上做模式匹配，却没有向原作者署名，这与此前 OpenAI 引用问题如出一辙；但也有人认为，用内核专门知识训练的专用模型最终能加快漏洞的发现、分析与修复并非天方夜谭。

**标签**: `#LLM security`, `#Linux kernel`, `#AI safety`, `#vulnerability disclosure`, `#open source`

---