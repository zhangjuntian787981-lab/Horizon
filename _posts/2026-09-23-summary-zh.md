---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 26 条内容中筛选出 4 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna，补齐 GPT-6 产品线](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5，能力提升并大幅降价](#item-2) ⭐️ 9.0/10
3. [Claude Opus 5.5、GPT-6 Sol 与 Luna 发布，AI 价格战开打](#item-3) ⭐️ 9.0/10
4. [OpenAI 为 GPT-6 推出更优提示缓存，支持显式断点](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，补齐 GPT-6 产品线](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 于 2026 年 9 月 22 日发布 GPT-6 Sol 与 GPT-6 Luna 两款新模型，它们位于旗舰模型 GPT-6 Astra（9 月 3 日发布）之下，共同补齐了 GPT-6 家族。此次发布的重点不是更强的能力，而是价格：Luna 的价格约为上一代同级模型的一半，而 Sol 被定位为面向高强度任务的中端主力模型，并以 gpt-6-sol 的名称在 API 中提供。 把前沿代际模型的价格砍半，直接改变了智能体编程（agentic coding）和长时间运行的智能体工作流的经济账——在这类场景中，决定开发者选用哪个模型的往往是 token 成本和使用额度，而不是跑分。这也对 Claude Code 等竞品编程智能体构成直接压力，因为套餐的使用上限本质上取决于单 token 价格。 Sol 是该代产品中的中端模型，以 gpt-6-sol 的形式在 API 中提供，面向高要求任务，在额度与成本上都留出更大空间；Luna 则是更便宜的一档，其定价比上一代同级模型低约一半。由于卖点是“接近上一代能力、价格却大幅下降”，用户现在需要在同一代模型内部权衡不同价位，而不再需要切换到另一个模型家族。

hackernews · OpenAI News · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 的 GPT-6 是一个“模型家族”而非单一发布：既有旗舰模型 Astra，也有复用同代训练方案、成本更低的 Sol 和 Luna。本次发布瞄准的智能体工作流（agentic workflow），指的是把大语言模型嵌入到带有工具和逻辑的结构化模式中，或者让模型自行决定控制流程，从而分多步完成目标。在这类流水线中，一个任务往往要调用模型很多次，因此单 token 价格成为工程上的首要考量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://coursiv.io/blog/gpt-6-sol-luna">GPT - 6 Sol and Luna : Pricing, Benchmarks, Availability | Coursiv Blog</a></li>
<li><a href="https://docs.langchain.com/oss/python/langgraph/workflows-agents">Workflows and agents - Docs by LangChain</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍把 Luna 价格减半视为最大新闻，Simon Willison（simonw）第一时间公开了 GPT-6 Luna、Sol 以及更早的 Astra 生成的鹈鹕 SVG 对比图。也有人关注更难以量化的方面：m\_fayer 表示 5.6 Sol 是个人心目中的“甜点”，他能预判它的行为、与之默契协作，并担心技术上更强的继任者在手感上反而没那么自然；jeffnash 则对比了 Claude Code 20x 与 Codex Pro 20x，认为 Codex 在使用额度上遥遥领先，因为该套餐下 ChatGPT 用量基本不受计量。leokennis 提出另一种视角：对普通用户而言，ChatGPT Plus 自 5.6 以来几乎无限量，在聊天、搜索、轻度编程和文档审阅上“开箱即用”。

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#GPT-6`, `#model-release`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5，能力提升并大幅降价](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，这是其旗舰模型 Claude 的一次重大更新，公司称这是自呼吁为 AI 前沿发展“放缓节奏”以来的首个版本。新模型在能力上有明显提升——包括更自然的沟通表达，以及在对比测试中显著更强的 3D 动画生成能力——同时全面下调了价格。 据报道 Claude Opus 5 曾是 OpenRouter 上支出最高的模型，因此输入与输出 token 约 20% 的降价，会直接改变所有运行大规模推理任务方的成本结构。这次发布也具有象征意义：Anthropic 不久前才呼吁放缓前沿模型的开发节奏，如今却在这轮激烈的模型竞赛中同时推进能力与价格。 官方公布的每百万 token 价格表显示：缓存读取从 $0.50 降至 $0.20，输入从 $5 降至 $4，输出从 $25 降至 $20，缓存写入从 $6.25 降至 $5。Anthropic 还强调其沟通风格有所改进——写作更清晰、会把最重要的信息前置——并将其定位为长会话中的可用性提升，同时也是一种安全层面的收益。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: Anthropic 是一家领先的 AI 研究机构，Claude 是其大语言模型系列，其中 Opus 是能力最强的档次。价格表中提到的“提示缓存”（prompt caching）允许 API 存储并复用提示词的一部分，从而降低重复上下文的处理成本。OpenRouter 是一个第三方网关，可将请求分发到多种模型，并发布基于用量的支出排行榜，因此常被用来判断哪个模型在实际生产中被使用得最多。

**社区讨论**: Hacker News 上的讨论非常热烈且意见分歧：一些评论者欢迎降价，其中有人贴出了完整的新旧 token 价格对比表；也有人对 Anthropic 一边呼吁“放缓前沿节奏”、一边快速发布新模型的做法表示质疑。一位测试者表示，相比 Opus 5，新模型在 3D 动画产物任务上进步明显；还有评论者直言自己更愿意继续使用 DeepSeek v4.1。

**标签**: `#AI/ML`, `#LLM`, `#Anthropic`, `#Claude Opus`, `#model release`

---

<a id="item-3"></a>
## [Claude Opus 5.5、GPT-6 Sol 与 Luna 发布，AI 价格战开打](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，大约一小时后 OpenAI 又发布了 GPT-6 Sol 和 GPT-6 Luna，而前一天 xAI 的 Grok 4.7 与小米的 MiMo v2.6 Flash/Pro 刚刚登场。Simon Willison 指出，GPT-6 Luna 的价格只有 GPT-5.6 Luna 的一半，GPT-6 Sol 相比 GPT-5.6 Sol 也有类似幅度下调，Claude Opus 5.5 同样降价。 四家主要实验室在约 48 小时内相继推出旗舰模型，并伴随全面降价，标志着前沿推理市场已进入全面价格战，直接压低了开发者构建 AI 应用的成本。过去因价格而做取舍的开发者，如今能以同样花费买到更强能力，而无法跟进这一价位的厂商则可能彻底失去 API 流量。 根据 Willison 的价格表，GPT-6 Luna 为每百万 token 输入 $0.10、缓存输入 $0.01、输出 $0.50；GPT-6 Sol 为 $2/$0.20/$10；Claude Opus 5.5 为 $4/$0.20/$20；Grok 4.7 为 $2/$0.50/$6。他指出 GPT-5.6 已排定 11 月涨价 25%，因此 GPT-6 的价格仅为这些模型促销价的一半；此外 GPT-5.6 Terra 与 GPT-6 Sol 同价，继续使用 Terra 的理由已不复存在。

rss · Simon Willison · 9月22日 23:46

**背景**: Simon Willison 是知名开发者与博主，多年来跟踪报道每一次重要的 LLM 发布，并用同一个提示词“生成一只骑自行车的鹈鹕的 SVG”测试所有模型，再把结果整理成对比图发布，这已成为他标志性的趣味基准。在本文中，他认为 GPT-6 家族的鹈鹕作品仍不及开启最大思考强度的 GPT-6 Astra，并观察到 5.6 家族配色更大胆明亮，而 6 家族更为柔和。诸如 $0.10/M、$20/M 的 API 定价指的是每处理一百万 token 的美元价格，其中输入 token 是发给模型的提示词，输出 token 是模型生成的内容，而缓存输入则是服务商已保存、可打折复用的提示文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">Simon Willison on pelican-riding-a-bicycle</a></li>
<li><a href="https://github.com/simonw/pelican-bicycle">GitHub - simonw/pelican-bicycle: LLM benchmark: Generate an SVG of a pelican riding a bicycle · GitHub</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI models`, `#Anthropic`, `#OpenAI`, `#pricing`

---

<a id="item-4"></a>
## [OpenAI 为 GPT-6 推出更优提示缓存，支持显式断点](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 7.0/10

OpenAI 宣布为 GPT-6 改进提示缓存（prompt caching）能力，带来更高的缓存命中率，并新增诊断工具、显式缓存断点以及一系列用于降低延迟和成本的控制手段。与此同时，官方还更新了提示缓存指南，说明开发者应如何组织可复用的提示前缀。 对于生产环境的 LLM 应用来说，提示缓存是性价比最高的降本与提速手段之一，因此更高的命中率和更好的诊断能力能直接降低大规模调用 GPT-6 的团队在 token 上的开销与响应延迟。此举也让 OpenAI 在面对 Anthropic、Azure OpenAI 等已经提供显式缓存断点的竞争平台时保持竞争力。 显式缓存断点允许开发者精确标记哪些提示前缀应被复用，相比仅依赖自动缓存提供了更细粒度的控制。更新后的指南以及配套的仪表盘/诊断工具旨在帮助团队监控缓存读取命中率并排查缓存未命中的原因，不过此次公告本身只是简短的宣传性内容，并未公布基准测试数据或具体价格。

rss · OpenAI News · 9月22日 21:00

**背景**: 提示缓存在 transformer 的注意力（attention）机制层面生效：当请求复用了完全相同的文本前缀时，模型可以跳过重复处理、直接复用此前计算好的状态，只处理提示中新增的部分。这使得带有相同系统提示、指令或文档的重复调用在成本和速度上大幅改善，目前主流厂商大多默认开启该功能，或通过缓存控制标志来启用。由于只有完全相同的前缀才能被复用，一条重要的实践原则是把稳定内容放在提示前部、把用户特定内容放在末尾——有团队仅通过将一段 300 token 的用户上下文块移出系统提示，就把缓存命中率从 23% 提升到了 71%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/better-prompt-caching-for-gpt-6/">Better prompt caching for GPT-6 - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/prompt-caching">Prompt caching | OpenAI API</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">Prompt caching - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#Prompt Caching`, `#LLM`, `#Cost Optimization`

---