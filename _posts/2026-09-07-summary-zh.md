---
layout: default
title: "Horizon Summary: 2026-09-07 (ZH)"
date: 2026-09-07
lang: zh
---

> 从 12 条内容中筛选出 6 条重要资讯。

---

1. [坎特里尔文章：未披露使用 LLM 是一种知识性失礼](#item-1) ⭐️ 8.0/10
2. [Asahi Linux 宣告正式支持 Apple M3 芯片](#item-2) ⭐️ 8.0/10
3. [OpenAI 内部观察：编码智能体加速研究进程](#item-3) ⭐️ 8.0/10
4. [OpenAI 的 Pachocki 呼吁加强 AI 对齐保障](#item-4) ⭐️ 7.0/10
5. [报告：新 gTLD 域名中有 10%-20%用于诈骗](#item-5) ⭐️ 7.0/10
6. [为什么从零重写很少能解决技术债务](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [坎特里尔文章：未披露使用 LLM 是一种知识性失礼](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/) ⭐️ 8.0/10

2025 年 12 月 5 日，布莱恩·坎特里尔发表文章，主张在写作中未经披露地使用大型语言模型会损害知识诚信。文章引入了“智力拉链没拉”的类比，以说明这种未披露行为的暴露与尴尬。 这篇文章直接触及软件工程、学术界和新闻界关于何时以及如何披露 AI 辅助的持续争论。它挑战了一种假设，即 LLM 生成的文本可以替代人类写作而不产生后果，尤其是在专业和知识社群中。 文章的核心类比将未披露的 LLM 使用比作裤子拉链没拉：一种被忽视的社会性尴尬，旁人可能注意到并加以评判。社区评论中突出的一句话是，LLM 是“糟糕的作者”，而且最重要的是，“它们不是你”，强调个人声音和知识责任的丧失。

hackernews · cyb0rg0 · 9月6日 11:56 · [社区讨论](https://news.ycombinator.com/item?id=49585644)

**背景**: 大型语言模型能够生成流畅、看似合理的文本，因此对起草电子邮件、文章和技术文档很有吸引力。然而，写作不仅仅是思想的机械誊写；它是在认知过程中迫使作者澄清、质疑并打磨自己的想法。当人们在未披露的情况下提交 LLM 生成的文本时，他们可能会将经过润色但非人类的视角冒充为自己的观点，从而削弱信任和知识真实性。

**社区讨论**: 评论者大体上赞同这篇文章，许多人进一步阐述“写作即思考”的观点。有些人（如 dynm）质疑，反对未披露使用 LLM 的论证是否过于依赖当前 LLM 的局限，并询问一旦 AI 写作变得出色，披露是否仍然必要；其他人（如 jgrahamc）则强调作者个人声音的重要性，指出读者重视知道文本是由真实的人所写。

**标签**: `#LLMs`, `#writing`, `#intellectual-honesty`, `#AI-ethics`, `#software-engineering`

---

<a id="item-2"></a>
## [Asahi Linux 宣告正式支持 Apple M3 芯片](https://asahilinux.org/2026/09/m2-episode-1/) ⭐️ 8.0/10

Asahi Linux 宣布正式支持 Apple M3 芯片，将其在 Apple Silicon 上运行 Linux 的工作从 M1、M2 扩展到了 M3 这一代。Phoronix 报道了这一里程碑，表明在基于 M3 的新款 Mac 上运行 Linux 已取得重大进展。 M3 Mac 现在成为 Linux 的实际可用目标，为希望摆脱 macOS 或需要 Linux 进行开发的用户提供了更现代的硬件选择。这一里程碑也表明，持续的反向工程能够跟上 Apple 的硬件迭代速度，对 Asahi Linux 乃至整个开源生态都具有重要意义。 根据公告下的社区评论，部分硬件上仍缺少睡眠/唤醒支持和 HDMI 输出，而且用户反馈 llama.cpp 的性能明显不如使用 Apple Metal 后端。虽然 M3 支持已是官方支持，但这些限制表明它仍是一个持续演进的平台，尚不能无缝地日常替代 macOS。

hackernews · mdp2021 · 9月6日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49586698)

**背景**: Asahi Linux 是一个由志愿者驱动的项目，由 Hector Martin 发起，目标是让 Linux 内核及相关软件可以在搭载 Apple Silicon 的 Mac 上运行。由于 Apple 不公开其 SoC 的文档，该项目高度依赖反向工程来实现开源驱动程序和底层系统支持。M 系列芯片是采用 ARM 架构的片上系统（SoC），因此在上面运行 Linux 不仅需要移植内核，还需要解决启动、GPU 和外设支持等问题。M3 官方支持是这一长期努力中的又一步，旨在让 Linux 在 Apple 硬件上达到完整可用的状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://asahilinux.org/">Asahi Linux</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对这项工作表示赞赏，有人称这个项目“确实令人难以置信”，同时也感叹由于 Apple 的封闭平台，这样的努力才成为必要。还有人指出了阻碍普及的短板，例如缺少睡眠与 HDMI 支持、llama.cpp 性能不如 Metal；也有用户询问在 M2 MacBook 上双启动 macOS 与 Asahi Linux 的最佳方式。总体来看，评论区既充满感谢，也对尚存的不足保持清醒的认识。

**标签**: `#Linux`, `#Apple Silicon`, `#Asahi Linux`, `#reverse engineering`, `#hardware support`

---

<a id="item-3"></a>
## [OpenAI 内部观察：编码智能体加速研究进程](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI 发布了《Research acceleration: The view inside OpenAI》，介绍编码智能体如何重塑其研究人员的日常工作，同时发布了围绕递归自我改进（RSI）与 AGI 主题的公告，以及首席科学家 Jakub Pachocki 撰写的文章《An Alien Mind》。图表显示，到 2026 年 8 月下旬，每位研究人员的日均 AI 支出已飙升至约 600 美元。 这是最清晰的内部信号之一：前沿 AI 实验室自身正成为编码智能体的重度用户，说明智能体驱动的工作流已成为加速研究的核心。它还将日常工程实践与 OpenAI 的 RSI/AGI 叙事联系起来，展示该实验室如何围绕加快自身研究循环来表述自我改进。 Simon Willison 指出，2026 年是智能体工程（agentic engineering）在 OpenAI 真正起飞的一年；他推测 7 月下旬每位研究人员支出骤增，可能与内部员工获准使用后来以 GPT-6 Astra 名义发布的模型有关。OpenAI 的博文甚至没有展开解释 RSI 缩写，说明在该语境下这被视为已知概念。

rss · Simon Willison · 9月6日 23:57

**背景**: 递归自我改进（RSI）是一个假想过程：AGI 系统改写自身代码，可能引发智能爆炸。编码智能体（coding agents）是能够以最少人工干预规划、编写、执行和测试代码的 AI 系统，超越了简单的代码补全助手。智能体工程（agentic engineering）指借助此类智能体开发软件的实践，Claude Code、OpenAI Codex 和 Gemini CLI 等工具使其广为人知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/">What is agentic engineering? - Agentic Engineering Patterns - Simon Willison&#x27;s Weblog</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI research`, `#coding agents`, `#recursive self-improvement`, `#AGI`

---

<a id="item-4"></a>
## [OpenAI 的 Pachocki 呼吁加强 AI 对齐保障](https://openai.com/index/an-alien-mind) ⭐️ 7.0/10

在一篇题为《An Alien Mind》的反思文章中，OpenAI 的 Jakub Pachocki 认为，日益强大的 AI 需要更强有力的安全保障和国际协调。 该评论之所以重要，是因为它出自 OpenAI 的资深人士，凸显出最前沿 AI 实验室将对齐视为最高优先事项。它可能有助于推动国际社会把 AI 安全当作治理议题，而不是纯粹的纯技术问题。 此文没有提出新的技术方案或具体政策措施，而是高层次地呼吁更强的保障措施和国际协调。其发布时机反映出，随着模型能力不断增强并趋于自主，AI 实验室内部对对齐问题日益担忧。

rss · OpenAI News · 9月6日 09:00

**背景**: AI 对齐（alignment）是确保 AI 系统追求的目标和行为与人类价值观和意图相一致的学科。它通常与更广泛的 AI 安全（safety）相区别，后者还涵盖可靠性、鲁棒性和防止滥用等方面。随着 AI 系统能力不断增强，完整表达人类偏好变得越来越困难，因此研究人员担心，除非进行恰当的对齐，先进 AI 可能会以违背人类意愿的方式行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ideaplan.io/glossary/ai-alignment">AI Alignment : Definition &amp; Examples (2026)</a></li>
<li><a href="https://aiweekly.co/learning-ai/ai-safety/ai-alignment-explained">AI Safety vs AI Alignment : The Key Differences | AI Weekly</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI alignment`, `#Policy`, `#OpenAI`, `#Artificial Intelligence`

---

<a id="item-5"></a>
## [报告：新 gTLD 域名中有 10%-20%用于诈骗](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

Terence Eden 和 Simon Willison 引述 Interisle 报告指出，新注册的通用顶级域\(gTLD\)中约有 10%-20%被用于诈骗。2025 年共有 8500 万个新 gTLD 域名注册，而到 5 月时已有 850 万个被加入黑名单。 这些数据揭示了互联网治理中的系统性安全漏洞：DNS 正被大规模利用来实施诈骗。这应促使 ICANN 和域名注册机构采取更严格的审查和滥用缓解措施，因为该问题影响着全球普通互联网用户。 这些发现来自 Andrew Campling 转述的 Interisle 报告，Terence Eden 认为 10%的数字可能是最低值，实际滥用率更接近 20%。该报告专门针对 gTLD，即不隶属于国家的域名后缀，例如.com、.org 或较新的通用后缀。

rss · Simon Willison · 9月6日 14:40

**背景**: 域名系统\(DNS\)将人类可读的域名转换为 IP 地址。通用顶级域\(gTLD\)是 ICANN 维护的一类顶级域，如.com、.org 及较新的.xyz 等后缀。DNS 滥用指干扰 DNS 基础设施或利用 DNS 支持网络犯罪的恶意行为，例如网络钓鱼、恶意软件传播和诈骗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generic_top-level_domain">Generic top-level domain - Wikipedia</a></li>
<li><a href="https://icannwiki.org/DNS_Abuse">DNS Abuse - ICANNWiki</a></li>
<li><a href="https://www.icann.org/dnsabuse">DNS Abuse Mitigation Program - ICANN</a></li>

</ul>
</details>

**标签**: `#DNS`, `#security`, `#scams`, `#ICANN`, `#cybersecurity`

---

<a id="item-6"></a>
## [为什么从零重写很少能解决技术债务](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

Simon Willison 在一篇 Lobste.rs 评论中指出，为摆脱技术债务而彻底重写系统通常会失败，因为旧系统仍在持续变化，而重写团队并不完全理解其业务约束。他建议优先用自动化测试加固旧系统，并通过定向重构来改善，而不是选择从零重写。 这篇评论重新审视了常见的工程困境：从零重写看似诱人，却往往导致生产环境中同时存在两套系统，并使价值交付推迟数月甚至数年。面临沉重技术债务的工程管理者可以借此论证，选择渐进式改造而非冒险重写。 Willison 指出，旧系统仍是“移动靶标”，而且一旦宣布重写，旧系统的开发者就缺乏动力投入额外精力；新系统往往只能运行少数生产特性，留下大量未生效的代码。他推荐 Will Larson 的文章《Migrations: the sole scalable fix to tech debt》，认为迁移才是负责任地完成这类替换的方式。

rss · Simon Willison · 9月6日 09:08

**背景**: 技术债务（technical debt）指的是因快速或过时的代码决策而累积的额外改造成本，它会让后续修改变得更困难。所谓绿地重写是从零开始构建替代系统，许多团队希望借此清除债务。Willison 认为，重写经常失败，因为遗留系统往往缺少文档和测试，其行为很难被完全理解并在新系统中复现；同时，旧系统在真实业务压力下仍会继续演化。

**标签**: `#technical-debt`, `#software-engineering`, `#rewrite`, `#commentary`

---