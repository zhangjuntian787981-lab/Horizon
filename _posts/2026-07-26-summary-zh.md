---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 13 条内容中筛选出 3 条重要资讯。

---

1. [Opus 5 展现出强大的提示注入抵抗力](#item-1) ⭐️ 8.0/10
2. [Anthropic 为 Claude 5 发布新的上下文工程规则，引发批评](#item-2) ⭐️ 7.0/10
3. [Ruff v0.16.0 启用 413 条默认规则，导致 CI 失败](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Opus 5 展现出强大的提示注入抵抗力](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

据 Boris Cherny 在模型系统卡中的引述，Anthropic 的 Opus 5 模型对提示注入攻击表现出显著的抵抗力。 这一改进标志着 AI 安全领域迈出了有意义的一步，因为提示注入是大型语言模型在实际应用中的关键漏洞。 这一断言基于 Opus 5 系统卡（第 73 页）中详述的评估和红队测试结果，表明该模型很难被成功注入提示。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种网络安全利用手段，通过恶意输入使大型语言模型绕过安全防护。系统卡是披露 AI 模型能力、安全评估和部署决策的文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#anthropic`, `#claude`, `#AI safety`, `#large language models`

---

<a id="item-2"></a>
## [Anthropic 为 Claude 5 发布新的上下文工程规则，引发批评](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.0/10

Anthropic 发布了针对 Claude 5 模型的新上下文工程指南，旨在通过系统化指令优化来提升性能。 这些指南代表了从传统提示工程向更结构化方法的转变，但社区报告的性能退化和增加的供应商锁定问题引发了对其实际效果的担忧。 社区用户报告称，与之前版本相比，Claude Opus 5 出现更多错误、意外删除，并且因反复失败而消耗更多 token。

hackernews · mellosouls · 7月25日 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**背景**: 上下文工程（Context Engineering）是一门新兴学科，超越了简单的提示设计，系统性地优化输入给大型语言模型的信息载荷。它包括结构化指令格式、记忆管理和迭代优化等技术。Anthropic 的最新指南旨在为 Claude 5 标准化最佳实践，强调清晰的任务分解和可控输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.13334">[2507.13334] A Survey of Context Engineering for Large Language Models</a></li>
<li><a href="https://github.com/Meirtz/Awesome-Context-Engineering">GitHub - Meirtz/Awesome-Context-Engineering: 🔥 Comprehensive survey on Context Engineering: from prompt engineering to production-grade AI systems. hundreds of papers, frameworks, and implementation guides for LLMs and AI agents.</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了怀疑：Fordec 认为这些指南是 Anthropic 工具链的锁定策略，并报告 Opus 5 性能下降。threecheese 批评过度依赖隐藏的自动记忆功能导致决策不稳定。orbital-decay 则认为建议过于泛泛，与实际情况不符。

**标签**: `#Claude 5`, `#context engineering`, `#Anthropic`, `#LLM best practices`, `#AI safety`

---

<a id="item-3"></a>
## [Ruff v0.16.0 启用 413 条默认规则，导致 CI 失败](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 7.0/10

Ruff v0.16.0 于 2026 年 7 月 23 日发布，将启用的默认规则从 59 条增加到 413 条，导致许多依赖未固定版本的项目在 CI 中失败。 这一重大规则扩展可能会破坏许多 Python 项目的 CI 流水线，但也能捕获更多严重问题（如语法错误和运行时错误），从而提高代码质量。 作者使用 \`uvx ruff@latest check . --fix --unsafe-fixes\` 修复了其项目中的数百个问题，该命令在发现的 1618 个错误中自动修复了 1538 个。Ruff 现在共有 968 条规则，而 v0.1.0 时为 708 条。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的极速 Python 代码检查器和格式化工具，拥有超过 900 条内置规则。它的默认规则集上次修改是在 v0.1.0 版本，新版本启用了许多之前默认未激活的规则，这些规则可以捕获语法错误和即时运行时错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/">Ruff</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>

</ul>
</details>

**标签**: `#ruff`, `#python`, `#linting`, `#astral`

---