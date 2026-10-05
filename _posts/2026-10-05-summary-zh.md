---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 4 条内容中筛选出 2 条重要资讯。

---

1. [Strata 在 RTX 4090 上以约 124 tokens/s 运行 125B Qwen3.8-Flash-Next](#item-1) ⭐️ 7.0/10
2. [第三方脚本可在 macOS 27 上关闭 Apple Intelligence 并回收磁盘空间](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Strata 在 RTX 4090 上以约 124 tokens/s 运行 125B Qwen3.8-Flash-Next](https://github.com/Niko1221/Strata) ⭐️ 7.0/10

由开发者 Niko1221 发布的开源推理引擎 Strata（v0.1.38）能够在单张消费级显卡上运行 1250 亿参数的 Qwen3.8-Flash-Next 模型——有社区用户报告在配备 128GB DDR5 内存和 Ryzen 7950X3D 的 RTX 4090 上达到约 124 tokens/s。Strata 的做法是把模型分散到 GPU、CPU、内存和 SSD 上，而不是要求整个模型塞进显存；有报告称在 12GB 显存的 RTX 5070 上使用 IQ3\_XXS 量化也能跑到约 65 tokens/s。 如果这些数据经得起检验，那么在本地以交互级速度运行 125B 级别的模型将大幅降低本地 LLM 推理的硬件门槛——此前这一规模的模型通常需要多卡工作站或云端 API。这也给 llama.cpp、Ollama 等成熟的本地运行时带来压力，促使它们重新证明自己在质量与速度之间的取舍是否合理，因为 Strata 只是目前在消费级硬件性能上相互竞争的多个项目之一。 Strata 更适合被理解为针对 Qwen3.8-Flash-Next 的专用运行时，而非通用推理引擎，因此它的性能优势未必能迁移到其他模型架构上。一项社区视觉基准测试发现，在完全相同的 GGUF 权重和视觉适配器下，Strata 的坐标中位误差为 154.8 像素，而 llama.cpp 为 46.5 像素，说明这种激进的量化与卸载方案即便吞吐量出色，也可能在对精度敏感的任务上造成实际的质量损失。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: 大语言模型通常以 GGUF 格式存储，这是由 llama.cpp 项目创建的单一二进制容器格式，把量化后的权重、分词器数据和元信息打包在一起，使模型能在本地机器上快速加载。量化通过以更低精度（4 位、3 位甚至更低）存储权重来压缩模型的内存占用，这正是让大模型能塞进消费级显卡的关键，但过于激进的低于 4 位的方案可能损害输出质量。卸载（offloading）则是一种相关技术：把模型的一部分放在 GPU 上、其余放在 CPU、系统内存甚至 SSD 上运行，用速度换取运行远超显存容量的大模型的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linuxcompatible.org/story/strata-v0138-runs-a-125billionmodel-llm-on-any-gaming-pc/">Strata v0.1.38 Runs a 125-Billion-Model LLM on Any Gaming PC</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一位实践者表示对低于 4 位的量化持怀疑态度，并称在租用的 RTX Pro 6000 上使用 4 位量化效果良好；另一位用户用 50 张图片做视觉基准测试后，发现 Strata 的中位误差（154.8 像素）远差于在相同权重下 llama.cpp 的 46.5 像素。正面反馈包括在 RTX 4090 上达到 124 tokens/s，以及在 RTX 6000 Pro 上 4 位量化解码达 255 tokens/s 且可支持 4 路并发；但也有评论者警告 Strata 的链接正在被到处刷屏，怀疑这股热度在蜜月期结束后还能剩下多少。

**标签**: `#llm-inference`, `#quantization`, `#consumer-hardware`, `#qwen`, `#gguf`

---

<a id="item-2"></a>
## [第三方脚本可在 macOS 27 上关闭 Apple Intelligence 并回收磁盘空间](https://github.com/omlahore/RemoveMacAI) ⭐️ 7.0/10

GitHub 上的第三方项目 RemoveMacAI 提供了一段脚本，用于在 macOS 上关闭 Apple Intelligence，并删除其附带的本地模型文件，从而把被占用的磁盘空间收回。该工具是在 macOS 27「Golden Gate」的背景下被讨论的——在这个最新版本的 macOS 中，Apple Intelligence 被深度集成，而非可选项。 这款工具的走红，反映出用户对默认开启、又无法干净卸载的 AI 功能日渐不满，这种「清理预装垃圾」的文化过去长期与 Windows 相伴。它也说明有相当一部分 Mac 用户希望在 AI 集成、磁盘占用以及哪些数据会离开本机等问题上拥有明确且原生的控制权。 Apple Intelligence 仅在 Apple 芯片（M1 及以后）的 Mac 上运行，采用本地处理与私有云计算相结合的方式，并可选接入 ChatGPT，其本地模型会占用相当可观的存储空间。由于 RemoveMacAI 是删除系统组件的非官方脚本，它可能导致相关功能异常、被系统更新部分还原，并且不受 Apple 官方支持。

hackernews · privacyisntdead · 10月4日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=49957116)

**背景**: Apple Intelligence 是 Apple 于 2024 年 6 月 10 日在 WWDC 2024 上发布的一套 AI 功能，作为 iOS 18、iPadOS 18 和 macOS Sequoia 的内置组成部分推出，涵盖写作工具、图像生成、通知摘要以及与 ChatGPT 的集成。代号「Golden Gate」的 macOS 27 于 WWDC 2026 发布、2026 年 9 月 14 日正式推出，是首个仅支持 Apple 芯片的 macOS 版本，也是最后一个完整支持 Rosetta 2 的版本。对于从不使用这些 AI 功能的用户来说，随系统捆绑的模型越来越被视为多余的负担而非福利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://en.wikipedia.org/wiki/MacOS_27">MacOS 27</a></li>
<li><a href="https://9to5mac.com/2026/09/14/macos-27-golden-gate-now-available-here-is-everything-new/">macOS 27 Golden Gate now available, here is everything new - 9to5 Mac</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者把这一情况类比为 Windows 上的 O&amp;O ShutUp10 等去臃肿工具，并直言质疑 Apple 的产品策略；也有用户抱怨 iOS 上已不再提供一键关闭这些 AI 功能的简单开关。另一些人则持反对意见，认为随系统附带的本地模型体积不大、效果均衡且无需把数据上传到云端；还有评论者回忆多年前曾花时间从 OS X 中删除数 GB 的打印机驱动，并好奇 Apple 究竟如何权衡这类取舍。

**标签**: `#macOS`, `#Apple Intelligence`, `#privacy`, `#bloatware`, `#disk space`

---