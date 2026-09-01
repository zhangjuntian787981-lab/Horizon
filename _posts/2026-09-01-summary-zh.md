---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 16 条内容中筛选出 4 条重要资讯。

---

1. [谷歌移除 MV2 扩展，影响 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [用 BirdNET-Go 将安防摄像头变成自动鸟类识别系统](#item-2) ⭐️ 7.0/10
3. [ChatGPT 广告年化收入达 10 亿美元，全球扩展](#item-3) ⭐️ 7.0/10
4. [Graham Dumpleton 发布 Wrapture，用于 Python 追踪与测试](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌移除 MV2 扩展，影响 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已从 Chrome 网上应用商店移除 Manifest V2（MV2）扩展，包括 uBlock Origin 和许多其他广告拦截器。这一强制措施是谷歌长期宣布的以 Manifest V3（MV3）取代 MV2 计划的一部分。 这是浏览器扩展生态系统的一个重要里程碑，因为 MV2 扩展包含 uBlock Origin 等对隐私至关重要的工具。担心广告拦截、安全和谷歌对网络控制权的用户，可能会转向 Firefox 等替代品。 Manifest V3 的 declarativeNetRequest API 对规则集数量设有限制，使基于 MV3 的广告拦截器弱于基于 MV2 的工具；uBlock Origin 的 MV3 继任者是 uBlock Origin Lite。对于企业用户，ExtensionManifestV2Availability 策略将在 Chrome 139 中移除，影响该版本的所有用户。

hackernews · twapi · 8月31日 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 和 V3 是 Chrome 的扩展平台。MV3 的引入旨在提升安全性和性能，但用 declarativeNetRequest 取代了 webRequest API，限制了扩展拦截网络请求的方式。uBlock Origin 依赖 MV2 的 webRequest 实现高效、全面的拦截，因此无法直接移植到 MV3。Firefox 仍支持 MV2 风格的 webRequest，因此许多用户推荐改用 Firefox。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/mv2/">About Manifest V2 | Chrome for Developers</a></li>
<li><a href="https://www.spacebar.news/chrome-ad-blocking-manifest-v3-ublock-origin/">Here&#x27;s what&#x27;s happening to ad blockers in Google Chrome</a></li>

</ul>
</details>

**社区讨论**: 评论者对谷歌表达了强烈不满，并推荐改用 Firefox。许多人指出 uBlock Origin 在 Firefox 上表现更好，还有人提到不太懂技术的用户点击恶意广告的安全隐患。总体情绪是认为谷歌对网络单方面的控制有问题，而 Firefox 是可行的替代方案。

**标签**: `#Chrome`, `#Manifest V2`, `#uBlock Origin`, `#privacy`, `#web browsers`

---

<a id="item-2"></a>
## [用 BirdNET-Go 将安防摄像头变成自动鸟类识别系统](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 7.0/10

在一篇博客文章中，一位爱好者详细介绍了如何使用 BirdNET-Go 与现有安防摄像头的 RTSP 视频流构建自动鸟类识别系统。BirdNET-Go 接入网络音频流，运行多模型分类，并在网页界面中展示检测结果。 该项目展示了如何以低成本将现有家庭安防基础设施重新用于野生动物监测和公民科学。这是将业余 AI、家庭自动化和生态观察相结合的一个令人鼓舞的范例。 BirdNET-Go 运行在 Raspberry Pi 上，需要 48 kHz 音频采样；一些摄像头（如 Aqara）仅支持 16 kHz，可能影响识别精度。作者还指出，摄像头麦克风的风噪可能是个问题，有时需要外接麦克风。

hackernews · speckx · 8月31日 16:47 · [社区讨论](https://news.ycombinator.com/item?id=49511856)

**背景**: BirdNET 是康奈尔大学基于 AI 的鸟类声音识别工具，而 BirdNET-Go 是其自托管实时版本，可接入声卡输入或网络音频流并持续运行分类。RTSP（实时流媒体协议）是 IP 摄像头通过网络传输视频和音频的标准协议，因此 BirdNET-Go 无需额外硬件就能“听”现有安防摄像头的音频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/ birdnet - go : Self-hosted realtime soundscape...</a></li>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://en.wikipedia.org/wiki/Real-Time_Streaming_Protocol">Real-Time Streaming Protocol - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区分享了各自的实现，包括带有 RTSP 视频流的 Unifi 门铃摄像头，以及带 e-ink 显示屏的便携式 BirdNET-Pi。也有人指出一些坑：Aqara 摄像头风噪严重且采样率仅 16 kHz，因此他们外接了一个麦克风。不少人还称赞康奈尔大学的 Merlin 鸟鸣识别应用，能引发非鸟类爱好者的兴趣。

**标签**: `#BirdNET-Go`, `#security cameras`, `#machine learning`, `#home automation`, `#DIY project`

---

<a id="item-3"></a>
## [ChatGPT 广告年化收入达 10 亿美元，全球扩展](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 7.0/10

OpenAI 宣布，ChatGPT 广告的年化收入运行率已达到 10 亿美元，并正在全球扩展，通过免费和经济实惠的选项支持更广泛地获取 AI。 这一里程碑凸显了 OpenAI 通过广告实现商业可行性的能力，有助于维持数亿 ChatGPT 用户的免费访问。它可能重塑 AI 平台的变现方式，并影响更广泛的数字广告行业。 年化收入运行率将当前时期的收入推算至全年；10 亿美元是一个预测数据，而非实际年度收入。根据行业指南，ChatGPT 广告的 CPM 为 60 美元，最低投放承诺为 20 万美元，截至 2026 年 6 月，产品信息流广告已进入测试版。

rss · OpenAI News · 8月31日 04:00

**背景**: ChatGPT 被数亿人用于学习、工作和日常决策，维持免费计划需要大量的基础设施投资。OpenAI 在 ChatGPT 中引入广告，以在不改变核心体验的情况下支持更广泛的访问。广告会在对话中按语境呈现，当启用个性化时，可能使用用户在 ChatGPT 整体活动中的特定信号来提供相关消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001047-ads-in-chatgpt">Ads in ChatGPT - OpenAI Help Center</a></li>
<li><a href="https://stripe.com/resources/more/what-is-annualized-run-rate-arr-how-to-calculate-arr-and-use-it-strategically">What Is Annualized Run Rate (ARR)? | Stripe</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#AI business`, `#Advertising`, `#Revenue`

---

<a id="item-4"></a>
## [Graham Dumpleton 发布 Wrapture，用于 Python 追踪与测试](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

wrapt 与 mod\_wsgi 的作者 Graham Dumpleton 发布了一个名为 Wrapture 的新 Python 库，它将 wrapt 风格的函数包装扩展到同时支持追踪和测试时的覆盖。该库支持 OpenTelemetry，并提供了一种基于配置的机制，可为现有 Python 项目添加追踪而无需修改代码。 Wrapture 为打桩提供了一个有前景的 unittest.mock 替代方案，并为实现可观测性提供了新思路，可能简化 Python 生态中的测试与追踪工作流。它由资深开发者背书，并且早期就支持 OpenTelemetry，这有望加速其在生产监控和测试套件中的采用。 该项目非常年轻，仅有几周历史，并且按作者在公告中的描述，所有代码和文档均由 AI 助手在他的指导下编写。后续文章展示了测试模式，例如在上下文管理器中将函数绑定为返回桩值；而基于配置的追踪示例使用 TOML 文件，捕获调用摘要并写入 JSON Lines 目标。

rss · Simon Willison · 8月31日 23:59

**背景**: Wrapture 基于 wrapt 模块构建，该模块为 Python 提供了透明对象代理，用于构造函数包装器、装饰器和猴子补丁，同时保留内省、签名和类型检查能力。猴子补丁指的是在运行时动态修改或扩展类或模块的行为，而函数追踪通常通过 sys.settrace 或自定义包装器来记录调用、参数和返回值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/wrapt/">wrapt · PyPI</a></li>
<li><a href="https://github.com/GrahamDumpleton/wrapt">GitHub - GrahamDumpleton/wrapt: A Python module for decorators ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monkey_patch">Monkey patch - Wikipedia</a></li>

</ul>
</details>

**标签**: `#python`, `#testing`, `#tracing`, `#monkeypatching`, `#tools`

---