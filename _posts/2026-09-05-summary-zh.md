---
layout: default
title: "Horizon Summary: 2026-09-05 (ZH)"
date: 2026-09-05
lang: zh
---

> 从 12 条内容中筛选出 2 条重要资讯。

---

1. [Chromium 浏览器沙箱远程代码执行零日漏洞（CVE-2026-85046）遭积极利用](#item-1) ⭐️ 10.0/10
2. [Anthropic AI 智能体在 Lean 中正式证明费马大定理](#item-2) ⭐️ 10.0/10

---

<a id="item-1"></a>
## [Chromium 浏览器沙箱远程代码执行零日漏洞（CVE-2026-85046）遭积极利用](https://nvd.nist.gov/vuln/detail/cve-2026-85046) ⭐️ 10.0/10

一个影响所有基于 Chromium 浏览器的关键零日漏洞（CVE-2026-85046）正被积极利用，该漏洞允许绕过沙箱进行远程代码执行（RCE）。谷歌已于 2026 年 9 月发布稳定版本更新（版本 152.0.7977.82 或更高版本）以修复这一 V8 引擎类型混淆缺陷。 由于 Chromium 驱动着 Google Chrome、Microsoft Edge、Opera 和 Brave 等主流浏览器，该漏洞使数以亿计的用户面临远程攻击的风险。它被列入 CISA 的“已知被利用漏洞”（KEV）目录，突显了其对企业和个人用户环境的即时威胁。 该漏洞源于 V8 JavaScript 引擎中的类型混淆缺陷，使攻击者能够建立读/写原语并逃逸浏览器沙箱。强烈建议用户立即将浏览器更新至 152.0.7977.82 或更高版本以降低风险。

hackernews · negura · 9月4日 21:52 · [社区讨论](https://news.ycombinator.com/item?id=49570669)

**背景**: Chromium 是一个开源浏览器项目，构成了许多现代网页浏览器的基础。V8 引擎是 Chromium 的开源 JavaScript 和 WebAssembly 引擎，其中的漏洞（如类型混淆）经常被攻击者利用，以绕过浏览器沙箱等安全边界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://app.opencve.io/cve/CVE-2026-85046">CVE-2026-85046 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://thecybersecguru.com/news/cve-2026-85046-exploit-explained/">CVE-2026-85046 Explained: Inside Chrome&#x27;s V8 Zero-Day | The ...</a></li>
<li><a href="https://shattered.io/chrome-zero-day-cve-2026-85046-sixth-2026/">Chrome Zero-Day CVE-2026-85046: 6th of 2026, CVSS 8.8</a></li>

</ul>
</details>

**社区讨论**: 社区对谷歌为报告这一关键漏洞支付的极低赏金（1000 美元）表示失望，认为这与其实际的漏洞利用价值极不匹配。其他人则感叹在互联网上运行不受信任的 JavaScript 和 WebAssembly 所带来的固有安全风险，还有人对比了不同 Chromium 浏览器之间的更新速度。

**标签**: `#Security`, `#CVE`, `#Chromium`, `#RCE`, `#Browser`

---

<a id="item-2"></a>
## [Anthropic AI 智能体在 Lean 中正式证明费马大定理](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐️ 10.0/10

Anthropic 的 AI 智能体成功在 Lean 定理证明器中正式证明了费马大定理，生成了 1300 万行证明代码和 29,500 个中间定理。该项目由一个智能体团队在不到两周的时间内完成，使用的是与 Claude Fable 5.1 相当的内部研究模型，消耗了约 60 亿个输出 Token。 这一成就代表了 AI 驱动的正式数学和自动推理领域的重大范式转变，证明了 AI 可以应对高度复杂、多步骤的数学证明。它为数字化和形式化海量数学知识、发现现有文献中的错误以及显著减轻新研究的同行评审负担开辟了可能性。 AI 并非创造了新的证明，而是形式化了 1995 年 Darmon-Diamond-Taylor 对 Wiles-Taylor-Wiles 论证的阐释，这需要构建诸如 Fontaine 理论和 Mazur 关于 Eisenstein 理想的研究等高级数学框架。据估计，按标准 API 费率计算，这一壮举的计算成本约为 30 万美元。

hackernews · jlebar · 9月4日 18:42 · [社区讨论](https://news.ycombinator.com/item?id=49568506)

**背景**: Lean 是一款开源的定理证明辅助工具和函数式编程语言，旨在验证数学命题并确保代码的正确性。证明助手允许数学家使用形式化语言编写证明，以便计算机能够严格检查其逻辑有效性，从而在人类数学推理与计算机验证之间架起桥梁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对该证明的规模表示了极大的震撼，同时重点关注了 Kevin Buzzard 关于这一成就对数学未来意味着什么和不意味着什么的评论。用户还讨论了利用 AI 纠正数学错误的前景，并指出了运行这些智能体所需的 30 万美元高昂计算成本。

**标签**: `#AI`, `#formal mathematics`, `#theorem proving`, `#Lean`, `#Fermat&\#x27;s Last Theorem`

---