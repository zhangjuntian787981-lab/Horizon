---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 20 条内容中筛选出 6 条重要资讯。

---

1. [小米发布 MiMo v2.6 Flash 与 Pro 开放权重模型](#item-1) ⭐️ 8.0/10
2. [TypeSafe AI 发布 Jev：不做文本生成、只输出结构化决策的“System One”模型](#item-2) ⭐️ 8.0/10
3. [博文主张读者要的是人写的文字，而非 AI 生成的文章](#item-3) ⭐️ 7.0/10
4. [OpenAI 呼吁建立全球共享的 AI 安全标准](#item-4) ⭐️ 7.0/10
5. [Multiverse Computing 将 LLM 块剪枝重构为 Ising 优化问题](#item-5) ⭐️ 7.0/10
6. [Cloudflare Python Workers 现已正式发布](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [小米发布 MiMo v2.6 Flash 与 Pro 开放权重模型](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米发布了两款 MiMo v2.6 开放权重模型：Flash 版本总参数量 309B、激活参数 15B，Pro 版本总参数量 1.02T、激活参数 42B，两者均已在 Hugging Face 上以 MiMo-V2.6-Flash-RL 和 MiMo-V2.6-Pro-RL 的名称发布。此次发布还罕见地全面公开了训练方法，包括一个实时训练仪表盘和一份详尽的技术报告。 据报道，MiMo v2.6 Pro 在发布时登顶了 Artificial Analysis 的开放权重模型智能排行榜，同时小米给出的输出价格低于每百万 token 1 美元，使接近前沿的能力以远低于美国主流模型的成本即可获得。这进一步强化了中国实验室持续推出高性能开放权重模型的趋势，对重视成本与自托管能力的开发者尤其重要。 两款模型均采用稀疏混合专家（MoE）架构，因此庞大的总参数量（309B 与 1.02T）在每个 token 上仅部分激活（分别为 15B 与 42B），这降低了推理算力需求但内存占用依然很高。此前的 MiMo-V2-Flash 在 Artificial Analysis 智能指数上得分为 41，MiMo-V2.5-Pro 为 26，而 MiMo-V2.6-Pro 据称达到 46；值得注意的是，早前的 MiMo-V2-Pro 与 MiMo-V2-Omni 是以专有模型形式发布的。

hackernews · volf\_ · 9月21日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: 混合专家（MoE）是一种模型架构，其中包含许多独立的“专家”子网络以及一个路由器，路由器会把每个 token 只发送给其中少数几个专家，因此模型可以拥有极大的总参数量，却对每个 token 只调用其中一小部分“激活”参数。正是这种稀疏性让 MoE 模型常用总参数量与激活参数量两个数字来描述，也解释了它们推理成本较低但仍需大量 GPU 内存来容纳全部专家的原因。小米的 MiMo 是该公司自研的大语言模型系列，此前 MiMo-V2-Flash 等版本已在 Hugging Face 上公开权重与推理代码，本次命名延续了这一脉络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://alphasignal.ai/news/xiaomi-s-mimo-v2-6-pro-tops-open-weight-rankings-with-a-1t-parameter-model">Xiaomi&#x27;s MiMo-V2.6-Pro Tops Open-Weight Rankings With a 1T-Parameter Model | AlphaSignal</a></li>
<li><a href="https://venturebeat.com/technology/xiaomi-stuns-with-new-mimo-v2-pro-llm-nearing-gpt-5-2-opus-4-6-performance">Xiaomi stuns with new MiMo-V2-Pro LLM nearing GPT-5.2, Opus 4.6 performance at a fraction of the cost | VentureBeat</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍赞赏小米的透明度，有人指出实时训练仪表盘是极佳的学习与教学工具，技术报告也异常详尽。也有人主要出于成本考虑而对中国的开放模型表示兴奋，同时讨论中还核实了具体参数量（309B/15B 与 1.02T/42B），并吐槽模型输出中反复出现的界面设计怪癖，例如生成前端时爱用的“01 - 大写文本”样式。

**标签**: `#LLM`, `#open-weights`, `#mixture-of-experts`, `#model-release`, `#Xiaomi`

---

<a id="item-2"></a>
## [TypeSafe AI 发布 Jev：不做文本生成、只输出结构化决策的“System One”模型](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI 发布了 Jev，这是其称为“System One 模型”的新品类中的首个模型（Simon Willison 更倾向于叫它“决策模型”）。它接收文本或半结构化的“state”输入，返回类型化的概率化答案而非自然语言文本：Bernoulli 式的 “Noul” 是/否置信度（0 到 1 之间的浮点数）、带选项概率分布的 Choice 问题，以及数值型 Score 问题。它只按输入计费，每百万 token 0.042 美元，比 OpenAI 的 GPT-5 Nano（每百万 0.05 美元）更便宜，输出 token 免费，并且能并行评估多个问题。 Jev 为一整类任务重新定义了“调用大模型”的含义——分类、垃圾内容识别、打标签、优先级排序、排名以及搜索重排——把一个生成式模型变成了快速、廉价、类型化、可被软件直接消费的函数调用，无需解析文本或反复重试。如果这一思路成立，它可能把大量例行推理从通用聊天模型转移到专用的决策模型上，这也正是 Simon Willison 这样有影响力的评论者会关注它的原因。 由于 Jev 只返回浮点数，它完全不给任何理由说明——Simon Willison 指出这是向黑箱机器学习更进一步的回退，并提醒偏见可能被隐藏在分数之中，因此它不适合用于给求职者排序这类高风险场景。据公开信息，它的响应时间在 70–500 毫秒之间，比前沿大模型快 40–200 倍；问题并行执行，所以增加问题数量几乎不会增加延迟；加上免费输出 token 的计费方式，使大规模重排（例如对每条查询用 BM25 召回 100 个候选并逐一打分）在经济上变得可行。

rss · Simon Willison · 9月21日 23:09

**背景**: “System One”借用了 Daniel Kahneman 关于快速直觉思维与缓慢审慎思维的区分，TypeSafe AI 用它来描述那些为“快速、结构化、可被代码直接消费的决策”而构建的模型，而非用于生成文章。传统大模型是文本进、文本出，并按输入和输出 token 双向计费，输出通常贵得多；决策模型则用经过校准的概率或类别替代文本输出，因此不需要 JSON 解析或重试逻辑。Simon Willison 提到的重排例子涉及 BM25，这是一种经典且廉价的基于关键词相关性的算法，用来召回候选文档，再由更昂贵的模型重新排序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.datacamp.com/blog/system-one-models-jev">Jev: TypeSafe &#x27;s System One Model Explained | DataCamp</a></li>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI ’s System One Model</a></li>

</ul>
</details>

**标签**: `#LLM`, `#decision models`, `#TypeSafe AI`, `#Jev`, `#probabilistic outputs`

---

<a id="item-3"></a>
## [博文主张读者要的是人写的文字，而非 AI 生成的文章](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) ⭐️ 7.0/10

Colin Breck 发表了题为《我不想读不是你写的东西》的博文，主张 AI 生成的文字只是在掩盖意义，而非真正把作者的思想传递给读者。该文登上 Hacker News 首页，获得 231 分和 91 条评论，开发者们围绕技术写作与散文写作之间的界限展开了讨论。 这篇文章及其讨论揭示了开发者文化中日益突出的摩擦点：随着 LLM 生成的文本大量涌入 PR 描述、技术文档和博客，评审者不得不花时间过滤机器生成的冗词，而不是理解作者的意图。这反映了整个行业在“生成式 AI 用于沟通表达而不仅是写代码”这一议题上的更广泛张力。 评论者区分了技术写作与散文写作：技术文本通常只是快速扫读以获取事实，因此 AI 辅助的接受度较高，除非内容过于冗长、用术语堆砌掩盖了关键信息；而散文则依赖行文节奏与个人声音来传递意义。有评论者点名指出 Claude Opus 在这方面“罪状累累”，措辞浮夸、故作高深；还有人认为近几代模型的写作质量不是停滞而是明显下降了。

hackernews · mooreds · 9月21日 22:30 · [社区讨论](https://news.ycombinator.com/item?id=49794330)

**背景**: 大型语言模型（LLM）是通常基于 Transformer 架构的神经网络，通过海量文本训练来预测和生成语言，ChatGPT、Claude、Gemini 等助手均由它们驱动。由于它们是基于统计规律而非真实经历或意图来生成流畅文字，其输出是否真正传达了作者的具体意图就成了疑问。这一争论在软件团队中尤为常见——如今 AI 工具已被普遍用于起草提交信息、PR 描述和技术文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者大体认同文章的核心观点，但在适用范围上存在分歧。有读者给出信息论式的论证：如果你想传递 1000 比特的语义信息，就不能只交给 LLM 300 比特并指望它补上缺失的 700 比特，因为它根本不知道那 700 比特是什么。也有人认为，被快速扫读的技术内容尚可接受 AI 写作，但散文不行；一位评审者抱怨如今 20 行的改动会附带数页生成的辩护理由和风险分析，让人“不看也不行”。还有一位持不同意见者认为，LLM 的写作质量不是停滞，而是明显下降。

**标签**: `#AI-generated content`, `#writing`, `#developer culture`, `#code review`, `#LLM`

---

<a id="item-4"></a>
## [OpenAI 呼吁建立全球共享的 AI 安全标准](https://openai.com/index/building-standards-next-phase-ai) ⭐️ 7.0/10

OpenAI 发布了一篇立场性文章，勾勒出通往全球共享 AI 标准的路径，呼吁在评估、报告和治理方面进行协调，以应对 AI 发展的下一阶段。文章认为，安全性的提升依赖于各实验室之间共同的基准与透明度，而非各自为战。 随着前沿模型能力不断增强，缺乏统一的评估与报告规范，使得监管机构、企业和公众难以在不同实验室之间比较其安全声明。如果主要开发者能在共享标准上达成一致，可能会影响合规要求、采购决策以及国际 AI 政策讨论的走向。 该倡议属于高层的政策与治理表态，而非技术发布，并未给出具体的阈值、时间表或执行机制。它围绕三大支柱展开——协调评估、报告与治理，但对于如何验证合规、由谁仲裁分歧仍留有空白。

rss · OpenAI News · 9月21日 10:00

**背景**: 前沿 AI 实验室越来越多地发布各自的安全框架和模型说明，但术语、评估套件和披露格式各不相同。这种碎片化使第三方审计变得困难，也让欧盟《人工智能法案》以及各国 AI 安全研究所等监管工作更加复杂。标准制定机构和行业联盟一直在尝试定义共同实践，而像 OpenAI 这样的领先实验室发声，在这些讨论中颇具分量。

**标签**: `#AI governance`, `#AI safety`, `#AI standards`, `#policy`, `#OpenAI`

---

<a id="item-5"></a>
## [Multiverse Computing 将 LLM 块剪枝重构为 Ising 优化问题](https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an) ⭐️ 7.0/10

Multiverse Computing 在 Hugging Face 发布了一篇博客文章，将大语言模型中的块移除（即深度剪枝）重新表述为一个受约束的二元优化问题，其等价于在 Ising 玻璃自旋系统中寻找低能态。相关工作通过二阶泰勒展开和基于逐样本梯度的 Hessian 来近似损失，从而构造出二次型目标函数 x^T H0 x，并施加“恰好移除 M 个 Transformer 块”的约束。 把“删除哪些块”的选择转化为能量最小化问题，这一做法将统计物理与组合优化同实际的模型压缩连接起来，有可能找到比贪心或启发式剪枝更优的块子集。它也展示了 Multiverse Computing 的量子启发式求解器业务方向，正是针对这类困难优化问题，以推动更高效、更易部署的 AI 模型。 该建模引入了逐块耦合变量 alpha\_i，并要求求解恰好移除 M 个块的组合，在问题规模允许时使用精确求解器，规模过大时则采用量子或量子启发式方法。作者强调需要关注整个低能谱而不仅仅是最低能基态，因为次优配置在下游任务表现上可能存在显著差异，并指出该方法可推广到稠密 Transformer 之外的架构。

rss · Hugging Face Blog · 9月21日 13:44

**背景**: 基于 Transformer 的大语言模型由数十个结构相同的块堆叠而成，因此深度剪枝——直接删除整块而非单个权重——颇具吸引力，因为它能直接减少层数并对硬件友好，但要从众多块中挑出最优子集是一个规模呈指数增长的组合问题。Ising 模型源自统计物理，用成对耦合描述相互作用的二元自旋；一般情况下求其最低能量构型是 NP 难问题，这正是人们使用量子退火机和量子启发式算法作为求解器的原因。Multiverse Computing 是一家量子计算公司，以量子启发式的压缩与优化工作闻名，包括用量子及量子启发式技术压缩和运行 AI 模型的 Q-AINA 项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an">A Blog post by Multiverse Computing on Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2602.00161v2">LLM Compression by Block Removal with Constrained Binary Optimization</a></li>
<li><a href="https://multiversecomputing.com/">Multiverse Computing - Pioneering the Era of Efficient and Sovereign...</a></li>

</ul>
</details>

**标签**: `#LLM Pruning`, `#Model Compression`, `#Ising Model`, `#Combinatorial Optimization`, `#Quantum Computing`

---

<a id="item-6"></a>
## [Cloudflare Python Workers 现已正式发布](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 7.0/10

Cloudflare 的 Python Workers 通过在基于 V8 的 workerd 运行时内使用 Pyodide 将 CPython 编译为 WebAssembly 来运行，现已结束为期两年的预览，并作为 Cloudflare 开发者平台上的一等语言正式发布。

rss · Simon Willison · 9月21日 22:25

**标签**: `#cloudflare`, `#python`, `#webassembly`, `#serverless`, `#pyodide`

---