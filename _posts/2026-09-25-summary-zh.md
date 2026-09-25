---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 18 条内容中筛选出 4 条重要资讯。

---

1. [F-Droid 2.0 发布：开源安卓应用商店迎来大规模改版](#item-1) ⭐️ 9.0/10
2. [英国的两级加密与 Apple 撤回 ADP](#item-2) ⭐️ 8.0/10
3. [Google DeepMind 发布 Gemini 3.8 Live，新增 Live Avatar 能力](#item-3) ⭐️ 8.0/10
4. [Liquid AI 发布 LFM2.5-VL-DSpark，用 2.795 亿参数草稿模型加速视觉语言推理](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [F-Droid 2.0 发布：开源安卓应用商店迎来大规模改版](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 9.0/10

F-Droid 于 2026 年 9 月 24 日发布博客文章《F-Droid 2.0：安卓自由的新篇章》，正式宣布开源安卓应用商店的 2.0 大版本更新。从社区讨论来看，此次更新包含大幅度的界面重构，并且据评论者所述，F-Droid Privileged Extension（FPE）正在被逐步淘汰。 F-Droid 是自由开源安卓应用仓库中的旗舰项目，因此一次完整的大版本重构会直接影响大量依赖它作为 Google Play 替代方案的 FOSS 用户、维护者和应用开发者。这次发布恰逢安卓平台开放性受到更多讨论的时期，使得该商店的易用性与独立性尤为关键。 由于原始材料中没有包含公告正文，2.0 的技术细节主要通过讨论体现：社区成员指出界面存在一些问题，例如某截图中的应用名“Syncthing-For k”把一个字母单独换行、界面各区块之间缺乏视觉区隔、可点击元素缺少明确提示。还有人提到诸如仓库时间戳不匹配这类晦涩报错仍未解决，并就这类诊断信息是否应引入任何形式的遥测产生争论。

hackernews · daveoc64 · 9月24日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=49831968)

**背景**: F-Droid 是一个面向安卓的自由开源应用目录与客户端，只分发 FOSS 应用，主要由志愿者维护，被视为注重隐私的 Google Play 替代方案。其官方客户端长期被批评界面陈旧、偏向开发者，因此催生了 Droid-ify 等第三方客户端，这些客户端在 GrapheneOS、LineageOS 等系统的用户中尤其受欢迎。F-Droid Privileged Extension 是一个配套组件，可让应用无需手动确认即可安装和更新，但由于需要系统级权限，配置起来历来比较麻烦。

**社区讨论**: 讨论整体对这次迟来的大改版表示支持——一位在 GrapheneOS 上使用 F-Droid 的用户对重构以及 FPE 的逐步淘汰表示欢迎——但评论主体仍是实质性批评：有人认为 F-Droid 依然像面向开发者/高级用户的工具，有人认为新设计跟风了“不做分隔线、不给可点击提示”的潮流，还有人指出仓库时间戳不匹配之类的晦涩报错需要更明确的受众定位，而不是让每个用户都发送“无意义的遥测”。评论者还提到 Droid-ify 等替代客户端，并对谷歌明年收紧安卓分发规则后 F-Droid 的前景表示担忧。

**标签**: `#F-Droid`, `#Android`, `#Open Source`, `#App Store`, `#UI/UX`

---

<a id="item-2"></a>
## [英国的两级加密与 Apple 撤回 ADP](https://macanorak.com/two-tier-encryption-in-the-uk/) ⭐️ 8.0/10

一篇被广泛讨论的文章及 Hacker News 讨论帖聚焦于英国正在形成的“两级加密”做法：面对一份要求其修改 ADP 所依赖的安全架构的法律命令，Apple 选择撤下面向英国 iCloud 用户的 Advanced Data Protection（ADP）功能，而不是照办。受影响的英国 iCloud 数据因此回退到 Standard Data Protection，即由 Apple 持有密钥、并可依法响应合法法律程序。 这一事件树立了一个先例：政府可以迫使一个全球性平台在整一个国家范围内撤下其最强的消费者加密功能，隐私倡导者警告这可能波及其他司法辖区，并助长类似密钥托管式的诉求。数百万英国 iCloud 用户因此失去了备份、照片、备忘录和文件上的端到端加密，而该事件也加深了关于执法访问权与用户隐私之间拉锯的争论。 根据 Apple 官方文档，英国用户默认仍有 14 类 iCloud 数据（如 iCloud Keychain 和 Health）保持端到端加密，而 ADP 此前可将这一数字提升至 23 类；失去 ADP 后，多出的类别——包括 iCloud Backup、Photos、Notes 和 iCloud Drive——回退到由 Apple 掌握密钥的 Standard Data Protection。评论者还指出，即便是所谓“未受影响”的类别在实践中也可能被削弱，因为某些端到端加密密钥可能会通过设备备份或账户恢复等常规使用场景而暴露。

hackernews · ReturnoftheHack · 9月24日 10:39 · [社区讨论](https://news.ycombinator.com/item?id=49828731)

**背景**: iCloud 的 Advanced Data Protection 是 Apple 提供的一项可选设置，可将端到端加密扩展到绝大多数 iCloud 数据，也就是说解密密钥只掌握在用户自己的设备上，连 Apple 都无法获取。相比之下，Standard Data Protection 把加密密钥保存在 Apple 数据中心，以便公司协助数据恢复并响应法律请求。这里的“两级加密”指的是这样一种制度：部分数据或用户享有最强的端到端保护，而另一部分则落入当局可访问的较弱层级——批评者认为这种结构会催生“密钥托管”安排，即为政府保留一份密钥副本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/en-us/108756">How to turn on Advanced Data Protection for iCloud - Apple Support</a></li>
<li><a href="https://support.apple.com/en-us/102651">iCloud data security overview - Apple Support</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上持怀疑与批评态度：有人认为 Apple 在 2015 年有勇气对抗 FBI，如今却已不再如此，并以强制性的年龄验证界面作为其原则退让的证据；也有人预计英国的“第二层级”中必然内置了密钥托管要求。一个反复出现的观点是，Apple 应当更进一步，退出英国市场或停止向英国政府机构销售产品，而不是悄悄降低用户的安全等级。

**标签**: `#encryption`, `#privacy`, `#UK policy`, `#Apple`, `#end-to-end encryption`

---

<a id="item-3"></a>
## [Google DeepMind 发布 Gemini 3.8 Live，新增 Live Avatar 能力](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) ⭐️ 8.0/10

Google DeepMind 发布了 Gemini 3.8 Live with Live Avatar，这是其实时多模态模型的新版本，通过将实时对话能力与低延迟流式视频原生结合，新增了实时会话式虚拟形象（avatar）能力。该功能面向企业及其用户，提供更自然、近似面对面的对话体验，而不再局限于纯语音交互。 实时多模态虚拟形象对交互式 AI 智能体而言是重要的一步，它让会话式 AI 从纯语音助手转向具备视觉存在的智能体，可部署在面向客户的企业场景中。作为头部实验室的旗舰级更新，它也抬高了其他厂商在实时、低延迟会话智能体赛道上的竞争门槛。 其核心技术主张是将实时对话与低延迟流式视频原生耦合，从而避免把语音、视频生成与传输等彼此独立的部分拼接在一起。不过该发布材料并未披露模型规模、延迟基准、定价或地区可用性，因此具体性能与获取方式仍有待确认。

rss · Google DeepMind · 9月24日 16:20

**背景**: Gemini Live 是 Google 为 Gemini 提供的低延迟实时交互模式，用户在对话时可获得地图、天气卡片和图片等可视化回应。面向开发者，随 Gemini 2.0 时代推出的 Gemini Live API 通过 WebSocket 将语音与视觉流式接入应用，实现实时多模态体验。生产级的实时多模态智能体通常由感知、融合、推理核心、会话记忆、工具调用动作层以及 WebRTC 或实时 WebSocket API 等实时传输层组合而成，Live Avatar 正是把这一模式应用到虚拟形象对话中。与此类似，Live Avatar 等竞品研究项目也在探索基于 Qwen3-Omni 等模型的流式、面对面虚拟形象对话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/">Introducing Gemini 3.8 Live with Live Avatar - The Keyword</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/live-api">Gemini Live API overview | Gemini API | Google AI for Developers</a></li>
<li><a href="https://liveavatar.github.io/">Live Avatar Project Page</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google DeepMind`, `#Gemini`, `#multimodal`, `#real-time agents`

---

<a id="item-4"></a>
## [Liquid AI 发布 LFM2.5-VL-DSpark，用 2.795 亿参数草稿模型加速视觉语言推理](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) ⭐️ 7.0/10

Liquid AI 推出了 LFM2.5-VL-DSpark，这是一个用于加速 LFM2.5-VL-3B 的视觉语言推测解码草稿模型，草稿模型参数量为 2.795 亿。该模型已在 Hugging Face 上以 Safetensors 和 GGUF 格式发布，并在首发当日就支持 llama.cpp、MLX-VLM 和 SGLang。 多模态推理成本高且受内存带宽限制，因此一个小巧且深度集成的草稿模型可以在不改变输出分布的前提下显著降低图文任务的延迟。首发即支持 llama.cpp、MLX-VLM 与 SGLang，意味着开发者可以在笔记本、Apple 芯片和本地服务器上直接享受加速，而不必依赖云端 GPU 集群，这也契合 Liquid AI 所宣称的“随处可运行的 AI”这一目标。 该视觉草稿模型沿用了 Liquid AI 文本版 LFM2.5-DSpark 草稿模型的架构：它在目标模型的若干固定中间层上抓取隐藏状态，并以此为条件一次草拟出 k 个候选 token，再由 3B 的目标模型并行校验。由于它属于推测解码组件，必须与其针对训练的特定目标检查点配套使用，实际加速幅度取决于草稿 token 的接受率。

rss · Hugging Face Blog · 9月24日 14:08

**背景**: 视觉语言模型（VLM）通常由三部分组成：视觉编码器、把视觉特征映射到语言模型嵌入空间的多模态投影器，以及负责生成文本的语言模型主干；Liquid AI 此前的 LFM2-VL 就采用了这种三段式设计。自回归解码受内存带宽制约，因为每个 token 都必须按顺序生成，而推测解码正是针对这一瓶颈：先让一个又小又快的草稿模型向前猜测若干 token，再由更大的目标模型在一次前向计算中全部校验，接受正确的、丢弃其余的，从而在保持目标模型输出分布不变的同时提升吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark">Accelerating vision-language models with LFM2.5-VL-DSpark</a></li>
<li><a href="https://www.liquid.ai/blog/lfm2-5-vl-dspark">LFM 2 . 5 - VL - DSpark : Accelerating vision-language models ... | Liquid AI</a></li>
<li><a href="https://www.orcarouter.ai/blog/lfm2-5-vl-3b-dspark-explained">LFM 2 . 5 - VL -3B- DSpark : Liquid AI &#x27;s 279.5M Drafter, Explained</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#model acceleration`, `#multimodal AI`, `#efficient inference`, `#Liquid AI`

---