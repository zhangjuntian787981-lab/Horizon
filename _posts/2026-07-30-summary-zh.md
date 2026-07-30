---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> 从 21 条内容中筛选出 6 条重要资讯。

---

1. [针对微软 Word Copilot 的自复制提示注入蠕虫](#item-1) ⭐️ 9.0/10
2. [开源引擎在 M 系列 Mac 上用 2GB 内存运行 Gemma 4 26B](#item-2) ⭐️ 8.0/10
3. [Mitchell Hashimoto 宣布成立新公司 Superlogical，基于 libghostty](#item-3) ⭐️ 8.0/10
4. [两个 API 设置使 GPT-5.6 在 ARC-AGI-3 得分翻三倍](#item-4) ⭐️ 8.0/10
5. [AI 密码分析恰逢后量子密码转型时机](#item-5) ⭐️ 8.0/10
6. [OpenAI 为 10 万研究人员免费提供 ChatGPT](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [针对微软 Word Copilot 的自复制提示注入蠕虫](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 9.0/10

安全研究员 Håkon Måløy 展示了一种新的提示注入攻击，可将微软 Word 的 Copilot 转变为自复制蠕虫。隐藏在文档中的指令会诱导 Copilot 修改当前文档，并将这些指令复制到新文档中，从而实现无需原始攻击者文档即可传播。 这是首个已知的自复制提示注入蠕虫，拓宽了 AI 集成办公工具的安全威胁模型。在广泛使用 Copilot 的企业环境中，可能导致文档大规模污染，削弱对 AI 辅助工作流的信任。 该攻击利用白底白字隐藏文本，使 Copilot 将其当作合法指令，从而触发文档修改和自复制。Måløy 已向微软负责任的披露该漏洞，但 144 天过去仍未发布全面修复方案。

rss · Simon Willison · 7月29日 18:43

**背景**: 提示注入是一种网络安全攻击，通过恶意输入使 AI 模型忽略原始指令并执行非预期操作。在驱动 Copilot 的大型语言模型（LLM）中，间接提示注入可嵌入检索到的内容中。此攻击更进一步，使注入的提示自动复制到新文档，形成自复制蠕虫——类似于计算机蠕虫的传播方式，但利用的是 AI 语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>

</ul>
</details>

**标签**: `#Security`, `#Prompt Injection`, `#AI`, `#Microsoft Word`, `#LLM`

---

<a id="item-2"></a>
## [开源引擎在 M 系列 Mac 上用 2GB 内存运行 Gemma 4 26B](https://github.com/drumih/turbo-fieldfare) ⭐️ 8.0/10

TurboFieldfare 是一个用 Swift 和 Metal 编写的开源推理引擎，通过从 SSD 流式传输路由专家，在 M 系列 Mac 上仅用 2 GB 内存运行 4-bit 量化的 Gemma 4 26B 模型。 这一突破使得在有限内存下运行大型 MoE 模型成为可能，使设备端 AI 对消费级硬件更易用、更实用，无需昂贵的硬件升级即可扩展强大模型的应用范围。 该模型的 4-bit 量化权重约为 14 GB，但 TurboFieldfare 仅将共享层和 KV 缓存保留在 RAM 中（约 2 GB），并按需从 SSD 流式传输专家权重，在 8 GB M2 MacBook Air 上达到 5-6 tok/s，在 M5 MacBook Pro 上达到 31-35 tok/s。

hackernews · gitpusher42 · 7月29日 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**背景**: 像 Gemma 4 26B 这样的大型语言模型采用混合专家（MoE）架构，每个 token 仅激活一部分专家。4-bit 量化减小了模型尺寸。传统推理需要将整个模型加载到 RAM 中；TurboFieldfare 利用 SSD 流式传输来克服这一限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://leimao.github.io/article/Neural-Networks-Quantization/">Quantization for Neural Networks - Lei Mao&#x27;s Log Book</a></li>
<li><a href="https://www.mindstudio.ai/blog/ssd-streaming-ai-models-ram-dial">SSD Streaming for AI Models: How to Turn RAM from a Wall into a Dial | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区评论对这种方法表示赞赏，与 llama.cpp 中的 mmap 进行了比较，并提供了在较旧 macOS 上编译的故障排除。一位用户提到 2.4 倍的预填充加速权衡，另一位建议在 DiffusionGemma 上进行潜在合作。

**标签**: `#inference engine`, `#edge AI`, `#Gemma`, `#macOS`, `#efficient inference`

---

<a id="item-3"></a>
## [Mitchell Hashimoto 宣布成立新公司 Superlogical，基于 libghostty](https://www.superlogical.com/) ⭐️ 8.0/10

HashiCorp 工具和 Ghostty 终端模拟器的创建者 Mitchell Hashimoto 宣布成立新公司 Superlogical，该公司将在开源 libghostty 库的基础上构建商业产品，同时将 Ghostty 的所有权移交给一个非营利组织。 此举展示了一种可持续的开源模式：核心库在 MIT 许可下保持免费开放，而公司在此基础上构建商业应用，从而确保持续开发和社区受益。 Superlogical 将把 libghostty 作为公共构建块，使用与其他人相同的 MIT 许可组件，并将共享终端工作上游化，使所有 libghostty 用户受益。Ghostty 本身是一个带有 GPU 加速的快速跨平台终端模拟器，将被移交给非营利组织。

hackernews · yan · 7月29日 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49098965)

**背景**: Ghostty 是一个快速、功能丰富、跨平台的终端模拟器，使用平台原生 UI 和 GPU 加速，最初由 Mitchell Hashimoto 开发。libghostty 是一个可嵌入的库，允许任何应用程序嵌入终端模拟器，使用 C 和 Zig 构建。这一公告延续了 Hashimoto 在开源基础上构建社区和商业利益的愿景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mitchellh.com/writing/libghostty-is-coming">Libghostty Is Coming – Mitchell Hashimoto</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty -org/ ghostty : Ghostty is a fast, feature-rich, and...</a></li>
<li><a href="https://ghostty.org/">Ghostty</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞将 Ghostty 移交给非营利组织并在开源库之上构建 Superlogical 的做法。simonw 强调了将 libghostty 用作公共构建块的巧妙性。一些用户将其与 OLE/COM 等较旧的技术相提并论，还有一位评论者表示对晦涩的标题感到沮丧。

**标签**: `#terminal`, `#open-source`, `#startup`, `#software-engineering`

---

<a id="item-4"></a>
## [两个 API 设置使 GPT-5.6 在 ARC-AGI-3 得分翻三倍](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores) ⭐️ 8.0/10

OpenAI 发现，启用两个特定的 API 设置——推理力度（reasoning effort）和上下文压缩（context compaction）——使 GPT-5.6 在具有挑战性的交互式推理测试 ARC-AGI-3 上的性能提升了三倍。 这一发现意义重大，因为它表明通过简单的 API 参数调整可以大幅提升模型在复杂推理基准上的性能，为开发者提供了可操作的见解，并凸显了推理和压缩功能的重要性。 推理力度控制模型用于推理的 token 数量，而上下文压缩则会总结过长的会话以适应上下文窗口。具体得分从之前水平翻了三倍，但确切数字未公开。

rss · OpenAI News · 7月29日 15:00

**背景**: ARC-AGI-3 是一个交互式推理基准，测试 AI 探索新环境、即时获取目标以及持续学习的能力——它被视为衡量智能体智能的挑战性标准。上下文压缩是一种技术，用于总结过长的对话历史以管理 token 限制，使模型能够在不丢失重要上下文的情况下继续工作。推理力度是一个参数，控制模型思考的深度，对于复杂任务使用更多 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://www.taskade.com/wiki/ai-agents/context-compaction">What Is Context Compaction ? Auto-Compact Explained... | Taskade AI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/reasoning">Reasoning models | OpenAI API</a></li>

</ul>
</details>

**标签**: `#AI`, `#ARC-AGI`, `#GPT`, `#benchmark`, `#reasoning`

---

<a id="item-5"></a>
## [AI 密码分析恰逢后量子密码转型时机](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

密码学专家 Matthew Green 指出，向后量子密码学的历史性转型恰逢基于 AI 的密码分析取得进展，这可能有助于验证新算法。 这种融合可能加速对 HAWK 等后量子标准的信心，并在量子计算机破解当前加密之前确保安全。 Green 提到了 Anthropic 近期在 HAWK-256 和 AES-128 上的密码分析工作，并提到了 Impagliazzo 的 Minicrypt 世界作为一种可能的情景，即 AI 并未攻克所有难题。

rss · Simon Willison · 7月29日 18:18

**背景**: 后量子密码学指同时抵抗经典计算机和量子计算机的密码算法。HAWK 是一种基于格的签名方案，正在被 NIST 考虑标准化。Impagliazzo 的五个世界是关于 P 与 NP 关系的假设情景；Minicrypt 是其中之一，其中单向函数存在但公钥密码仍然可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hawk-sign.info/">Hawk</a></li>
<li><a href="https://www.nist.gov/pqc">Post-quantum cryptography | NIST</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russell_Impagliazzo">Russell Impagliazzo - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#AI`, `#cryptanalysis`, `#security`

---

<a id="item-6"></a>
## [OpenAI 为 10 万研究人员免费提供 ChatGPT](https://openai.com/index/chatgpt-for-academic-researchers) ⭐️ 7.0/10

OpenAI 宣布向 10 万名学术研究人员免费提供其最先进的 ChatGPT AI 模型，以加速科学发现。 这一举措使研究人员能够更广泛地使用先进的 AI 工具，可能加速医学、生物学和物理学等领域的突破，并为 AI 公司支持学术界树立了先例。 该优惠包括通过 ChatGPT 访问 OpenAI 最先进的模型（可能是 GPT-4 或更新版本），名额上限为 10 万研究人员，但未提供具体时间表或资格标准。

rss · OpenAI News · 7月29日 10:00

**背景**: ChatGPT 是 OpenAI 开发的大型语言模型，能够生成类人文本并协助完成各种任务。学术研究人员通常缺乏访问昂贵 AI 工具的途径，限制了他们在研究中利用 AI 的能力。这一举措旨在通过向大量研究人员提供免费的先进 AI 资源来弥合这一差距。

**标签**: `#AI`, `#research`, `#OpenAI`, `#ChatGPT`, `#scientific discovery`

---