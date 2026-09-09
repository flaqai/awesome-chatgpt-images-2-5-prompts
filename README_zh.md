# Awesome ChatGPT Images 2.5 Prompts — flaq.ai 原创提示词库

**面向电商产品图、精准修图、人物宠物、广告海报、故事分镜与多语言设计的实用提示词。由 [flaq.ai](https://flaq.ai) 团队创作、维护并开源。**

[English](README.md) · **简体中文** · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português (Brasil)](README_pt.md) · [Italiano](README_it.md) · [Русский](README_ru.md) · [العربية](README_ar.md) · [हिन्दी](README_hi.md) · [ไทย](README_th.md) · [Bahasa Indonesia](README_id.md) · [Tiếng Việt](README_vi.md)

![flaq.ai 原创 ChatGPT Images 2.5 提示词库封面：Make ideas visible](assets/images/cover.png)

[直接选提示词](prompts/README.md) · [查看修图案例](docs/editing-case-study.md) · [提示词写法](docs/prompting-guide.md) · [API 使用](docs/api-guide.md) · [图片生成记录](docs/generation-log.md)

## 新增：官方发布场景原创实践

参照 [OpenAI 发布文章](https://openai.com/index/introducing-chatgpt-images-2-5/) 的实用场景，新增7条中英双语配方、14张原创图片：宠物披风、虚构儿童换装、被套花色、纪念卡文字、立方体旋转、行程单栏修改与蜡烛计数。每组附输入图、编辑图、实际提示词和检查结果；立方体存在几何偏差，已如实标明。

[查看7组前后对照](docs/launch-examples.md) · [复制P061–P067提示词](prompts/12-launch-examples.md)

## 从一张好看的图，到可以继续修改的作品

商业创作经常需要“产品不变，只换背景”“中文换成日文，版式不要乱”“同一角色继续下一镜”。因此，本库不止描述风格，还明确任务、构图、材质、图中文字、保留项、后续修改与验收标准。

当前版本包含 **79 条原创配方、12 个场景包**：67 条完整中英双语核心提示词，以及12条本地语言配方。翻译、追问和变体不重复计数。另有 **21 张新生成图片：1张品牌封面 + 6张早期示例 + 7组输入与编辑对照**。未配图条目标明“尚未实测”，不把全部配方描述成已验证案例。

## 新增：玩法路线与版本对比

- [10条实用玩法路线](docs/playbook.md)：从商品母版、宠物写真到故事分镜，按素材选择并逐步执行。
- [GPT Image 2 与 Images 2.5 升级对比](docs/images-2-vs-2-5.md)：解释Flare、Sunburst的区别，以及哪些能力属于改进而非首次支持。

两份指南复用现有配方和图片，不增加配方计数，不冒充模型对比实测。

README现提供 **16个语言／地区版本**，默认英文。各语言入口包含使用指引、示例提示词和平台资源；核心配方仍为完整中英双语。[查看语言覆盖范围](docs/localization-guide.md#readme-language-coverage)。

## 三步开始

1. 从下表选择场景，复制其中一个语言版本，把虚构品牌、商品和文案替换成你的内容。
2. 新建图直接使用；编辑图按提示顺序上传素材，并说明每张图的用途。
3. 检查结果并保存确认稿，再使用条目中的后续修改。开启新对话时，请重新附上确认稿。

先试试这个原创简版：

```text
为虚构台灯品牌制作3:2横版产品广告。
台灯使用午夜蓝圆柱金属底座、象牙白圆盘灯罩和橙色拉环。
放在珊瑚色阶梯展台上，深蓝背景，阴影自然可信。
左侧仅排白字“LIGHT, UNPLUGGED.”和“TIDELINE”。
呈现真实材料纹理，只保留一盏灯，不添加其他文案或产品参数。
```

确认图片后继续：

```text
只把台灯底座改为低饱和玉绿色，保持形状和金属纹理。
灯罩、拉环、文字、背景、镜头与展台均保持不变。
```

[查看详细版](prompts/01-product.md#p001)；本库展示图的[实际执行提示词](assets/generation/tideline-lamp.txt)另有记录。

## 按实际工作选场景

| 场景包 | 包含内容 | 数量 |
| --- | --- | --- |
| [产品摄影与电商](prompts/01-product.md) | 台灯广告、陶瓷杯白底图、护肤静物、磨豆机结构、运动鞋特写、礼盒 | 6 |
| [广告与社交媒体](prompts/02-social.md) | 活动海报、视频封面、旅行轮播、午餐广告、播客封面、市集主视觉 | 6 |
| [人物、时尚与宠物](prompts/03-people-pets.md) | 职业头像、宠物探险照、外套试穿、生活抓拍、双人插画、宠物水彩 | 6 |
| [精准编辑](prompts/04-editing.md) | 局部换色、去杂物、光照调整、定点换字、草图添加物件、透明抠图 | 6 |
| [信息图与教育](prompts/05-information.md) | 雨水花园、风味图、示例数据图、街区地图、植物生长、流程演示 | 6 |
| [品牌与界面](prompts/06-brand-ui.md) | 字标、导视、移动应用、落地页、包装系列、创作者看板 | 6 |
| [故事与游戏](prompts/07-stories-games.md) | 六格故事、角色转面、表情表、物品图标、等距屋顶、像素海港 | 6 |
| [建筑与空间](prompts/08-spaces.md) | 阅读室、公寓翻新、精品客房、快闪店、庭院、小亭效果图 | 6 |
| [出版与插画](prompts/09-publishing.md) | 书封、食谱跨页、年度回顾、编辑隐喻、水墨画、独立刊物 | 6 |
| [系列与制作交付](prompts/10-production.md) | 四季系列、横转竖、本地化、三图合成、老照修复、分镜扩展 | 6 |
| [12种语言配方](prompts/11-multilingual.md) | 中、英、日、韩、西、法、德、葡、阿拉伯、印地、泰、俄语 | 12 |
| [官方发布场景原创实践](prompts/12-launch-examples.md) | 宠物换装、儿童肖像、被套花色、城市文字、立方体、行程卡、蜡烛计数 | 7 |

## 本次原创生成示例

| 商品广告 | 日英双语烘焙海报 |
| --- | --- |
| ![台灯产品广告：深蓝金属与珊瑚展台](assets/images/tideline-lamp.png) | ![日英双语面包店海报：焼きたての朝](assets/images/komorebi-bakery.png) |
| [P001 提示词](prompts/01-product.md#p001) | [L003 提示词](prompts/11-multilingual.md#l003) |

| 修补纸月亮故事 | 社区阅读室 |
| --- | --- |
| ![机器人修补纸月亮六格分镜](assets/images/paper-moon-story.png) | ![旧工坊改造社区阅读室概念图](assets/images/reading-room.png) |
| [P037 提示词](prompts/07-stories-games.md#p037) | [P043 提示词](prompts/08-spaces.md#p043) |

示例来自 Codex 内置生图工具，工具未返回底层模型ID，因此**不作为 Flare / Sunburst 的指定型号实测或横向评测**。六格故事第三格提前出现缝线；阅读室增加了杯子和花瓶。这些可见偏差均在[生成记录](docs/generation-log.md)中说明。

## 同一张广告：先改颜色，再改标题

| 原稿 | 第一轮：底座换绿 | 第二轮：只换标题 |
| --- | --- | --- |
| ![原始蓝色台灯](assets/images/tideline-lamp.png) | ![保留标题的绿色台灯](assets/images/tideline-lamp-jade.png) | ![保留绿色并更换标题](assets/images/tideline-lamp-copy.png) |

第二轮以第一轮绿色成图为输入，能直观看到确认稿如何继续修改。细微表面纹理仍有变化，灯杆也随底座变绿，不能理解为像素级不变。[查看完整过程与验收方法](docs/editing-case-study.md)。

## 针对 Images 2.5 做了哪些细化？

官方模型文档将 **Flare** 定位为快速日常生图，将 **Sunburst** 用于更重视编辑精度的工作流，均接受文字和图像输入。参见 [Flare 模型页](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)及 [Sunburst 模型页](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)。

本库据此强化参考图分工、保留项、多轮确认稿、局部换字和系列一致性。这是提示词设计策略，不是成功率承诺；[版本说明](docs/model-notes.md)区分官方参数与尚未验证的假设。

## 在 flaq.ai 使用 GPT Image 2 API

[flaq.ai](https://flaq.ai) 提供 GPT Image 2 生图与编辑入口，可先试用创意方向，再按模型文档接入应用。

| 用途 | 入口 |
| --- | --- |
| 从文字创建商品图、海报和插画 | [GPT Image 2 生图 API](https://flaq.ai/models/openai/gpt-image-2/) |
| 使用参考图修改或合成 | [GPT Image 2 Edit API](https://flaq.ai/models/openai/gpt-image-2-edit/) |
| 查看参数、鉴权与任务处理流程 | [GPT Image 2 接口文档](https://flaq.ai/docs/?page=api/gpt-image-2) |

先在模型页面测试提示词，再按文档提交任务并查询结果。当前价格与参数以对应页面为准。这里介绍的是 **flaq.ai 的 GPT Image 2 接口**；本库的 Images 2.5 提示词可作为适配起点，不能把两个型号或不同平台的参数混用。直接调用 OpenAI Images 2.5 请见[独立 API 指南](docs/api-guide.md)。

## 常见问题

### 可以免费使用吗？

仓库原创内容采用 [MIT](LICENSE) 开源许可。最终图片中的人物、品牌、输入素材及其他第三方权利仍需结合实际用途检查；虚构演示名称不等于经过商标检索。

### 79条都已经生成验证了吗？

没有。当前是67条双语核心配方、12条本地语言配方和21张新生成图片。各条目清楚标识配图状态，修改指令也不一概声称已执行。

### 可以直接用作商业成品吗？

可作为创作起点，但需要检查文字、人物、产品外形和用途。界面图不是可运行软件；字标不是矢量文件；数据图、施工图和长篇排版需要相应制作工具复核。

### 如何避免多轮修改越改越乱？

每次只改一个变量，重复必须保留的内容，传入最近一次确认图。如有漂移，回到确认图重新修改。不要依赖新对话记住以前的图。

### 是 OpenAI 官方项目吗？

不是。这是 **flaq.ai 团队独立输出的开源项目**，与 OpenAI 无隶属或背书关系。

## 参与贡献

欢迎提交原创场景、语言审校和带真实生成记录的图片。请阅读[贡献规范](CONTRIBUTING.md)与[原创规范](docs/originality.md)。

## 关于 flaq.ai 团队

[flaq.ai](https://flaq.ai) 是面向 AI Agent、创意应用和内容生产流程的统一 API 平台，覆盖图像、视频、音乐与语言模型。开发者可以从[模型市场](https://flaq.ai/model-market/)选择模型，通过[接口文档](https://flaq.ai/docs/)把已经验证的创作流程接入应用。

对于本提示词库，可以先选配方、生成并检查效果，再将确认后的流程用于产品。上方提供 flaq.ai 的 GPT Image 2 生成与编辑入口；Images 2.5 的 OpenAI 直连方式见独立 API 指南。

本开源项目由 flaq.ai 团队创作和维护，将提示词、原创示例与修改经验整理为可复用资源。欢迎补充实用场景、修正翻译，并提交带真实提示词和结果记录的案例。

- [访问 flaq.ai](https://flaq.ai)
- [查看 API 文档](https://flaq.ai/docs/)
- [团队 GPT Image 2 提示词库](https://github.com/flaqai/awesome-gpt-image-2-prompt)

## flaq.ai 联盟营销计划

如果你制作 AI 教程、模型评测、创作工作流或 API 接入指南，可通过 [flaq.ai 联盟计划](https://flaq.ai/affiliate-program/)推荐平台，并从符合条件的订单获得佣金。

| 推荐订单 | 公布的佣金比例 |
| --- | --- |
| 被推荐用户的首笔有效付费订单 | **20%** |
| 该用户注册后60天内的后续有效付费订单 | **10%** |

登录 flaq.ai，完善联盟资料并创建推荐链接，可在联盟工作区管理链接和查看推荐活动。退款、拒付及其他不符合条件的订单不计佣；推广时按[联盟协议](https://flaq.ai/affiliate-agreement/)披露推荐关系。条款核对日期为2026-09-09，实际以最新规则为准。

**[加入 flaq.ai 联盟计划 →](https://flaq.ai/affiliate-program/)**

## 许可

[MIT](LICENSE) © 2026 Flaq AI。

[默认英文首页](README.md) · [完整索引](prompts/README.md) · [机器可读数据](data/prompts.json) · [更新日志](CHANGELOG.md) · [SEO 发布文案](docs/seo.md)
