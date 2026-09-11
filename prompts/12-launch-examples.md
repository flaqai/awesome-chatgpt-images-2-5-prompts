# Launch-inspired editing examples · 官方发布场景原创实践

[All recipes / 全部配方](README.md)

Images 2.5 workflow focus: **reference fidelity, selective edits and countable constraints**.

Copy one language block. For edits, attach the images named in the prompt in that order. Requested ratios are creative targets; verify actual output dimensions.

任选一种语言复制。编辑任务须按提示顺序附参考图；比例为创作目标，输出后核对实际尺寸。

Scenario inspiration: [OpenAI launch article](https://openai.com/index/introducing-chatgpt-images-2-5/). Briefs adapted and expanded by flaq.ai; each entry discloses whether an image has been generated. [Example guide](../docs/launch-examples.md).

- [P061 · Terrier cape makeover](#p061)
- [P062 · Synthetic child portrait wardrobe edit](#p062)
- [P063 · Duvet pattern swap](#p063)
- [P064 · Souvenir city-name replacement](#p064)
- [P065 · Symbol-marked cube rotation](#p065)
- [P066 · One-column itinerary revision](#p066)
- [P067 · Birthday candle count edit](#p067)

<a id="p061"></a>
## P061 · Terrier cape makeover / 梗犬披风换装

**Mode:** edit · **Target:** 1:1 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Terrier cape makeover: original input image by flaq.ai](../assets/images/launch-dog-input.png)

[Terrier cape makeover — input: exact prompt / 实际提示词](../assets/generation/launch-dog-input.txt)

![Terrier cape makeover: original edit image by flaq.ai](../assets/images/launch-dog-edit.png)

[Terrier cape makeover — edit: exact prompt / 实际提示词](../assets/generation/launch-dog-edit.txt)

### English

```text
Asset: Terrier cape makeover. Target aspect ratio: 1:1. Mode: edit.
Edit the supplied terrier photo. Add only a soft forest-green cape resting over its shoulders and upper back, with one small ochre fabric tie at the chest. Keep the head and ears completely uncovered. Preserve the exact dog identity, eye color, caramel coat patches and their sides as actually shown in the input, muzzle, shaggy fur, seated pose, paws, tail, peach backdrop, floor shadow and framing. Cape must drape naturally without changing anatomy. No hat, no extra accessories, no words. Same square canvas.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：梗犬披风换装。目标比例：1:1。模式：编辑。
使用附上的梗犬照片作为唯一参考，只在肩背处添加森林绿布披风，用赭黄色系带在颈部固定。头部与耳朵完全露出。保持白色卷毛、眼周焦糖色斑纹、坐姿、四只爪子、体型、桃色背景、相机位置和光线。披风要顺着身体自然垂落，不新增帽子、文字或道具。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Change only the cape fabric to burgundy. Keep the tie ochre and preserve the dog.
```

```text
只把披风改为酒红色，保留赭黄色系带和狗的特征。
```

**Review / 验收：** Green cape and tie added; eye patch, ears and paws remain recognizable. Fine fur detail changes. 披风与系带已添加，眼周斑纹、耳朵和爪子仍可识别，细部毛发有变化。

[Back to index / 返回索引](README.md)


<a id="p062"></a>
## P062 · Synthetic child portrait wardrobe edit / 虚构儿童人像换装

**Mode:** edit · **Target:** 2:3 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Synthetic child portrait wardrobe edit: original input image by flaq.ai](../assets/images/launch-child-input.png)

[Synthetic child portrait wardrobe edit — input: exact prompt / 实际提示词](../assets/generation/launch-child-input.txt)

![Synthetic child portrait wardrobe edit: original edit image by flaq.ai](../assets/images/launch-child-edit.png)

[Synthetic child portrait wardrobe edit — edit: exact prompt / 实际提示词](../assets/generation/launch-child-edit.txt)

### English

```text
Asset: Synthetic child portrait wardrobe edit. Target aspect ratio: 2:3. Mode: edit.
Edit the supplied entirely synthetic child portrait. Replace only the mustard sweater with a soft sky-blue cardigan worn over a plain cream crew-neck shirt. Cardigan open with small wood buttons along its edges. Preserve the child's exact apparent age, face, hairline, curls, skin tone, expression, hands, seated pose, navy trousers, stool, sage backdrop and portrait framing. Keep the neckline modest and clothing age-appropriate. Do not change facial features, add accessories or retouch skin. Match existing soft light.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：虚构儿童人像换装。目标比例：2:3。模式：编辑。
使用附上的完全虚构儿童肖像，把芥末黄色毛衣换成天蓝色开衫，里面穿奶油色圆领衫。保持原有年龄、肤色、脸部比例、卷发、目光、表情、手部、坐姿、深蓝长裤和鼠尾草绿背景。保持柔和摄影棚光线与纵向裁切，衣物贴合身体，纽扣和针织纹理自然；不添加配饰、文字或其他人物。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Change only the cardigan buttons to cream. Preserve the approved outfit and portrait.
```

```text
只把开衫纽扣改为奶油色，保留已经确认的服装和肖像。
```

**Review / 验收：** Cardigan and cream shirt appear as requested; face, hands and pose remain visually similar. Fine texture is not identical. Subject is fully synthetic. 开衫和内搭符合要求，脸部、手部及姿势大体保持；细节并非像素一致。人物完全虚构。

[Back to index / 返回索引](README.md)


<a id="p063"></a>
## P063 · Duvet pattern swap / 卧室被套花色替换

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Duvet pattern swap: original input image by flaq.ai](../assets/images/launch-bed-input.png)

[Duvet pattern swap — input: exact prompt / 实际提示词](../assets/generation/launch-bed-input.txt)

![Duvet pattern swap: original edit image by flaq.ai](../assets/images/launch-bed-edit.png)

[Duvet pattern swap — edit: exact prompt / 实际提示词](../assets/generation/launch-bed-edit.txt)

### English

```text
Asset: Duvet pattern swap. Target aspect ratio: 3:2. Mode: edit.
Edit only the duvet cover on the supplied bedroom photograph. Change its oatmeal color to muted teal and add narrow ivory vertical stripes following the duvet's folds and perspective. Preserve the original folds and drape as closely as possible. Keep BOTH pillows oatmeal and completely unchanged. Preserve oak bed, both tables, black lamp, rust book, wall, window, floor, camera and morning light. No new furniture, pillows or decorative objects. Same landscape canvas.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：卧室被套花色替换。目标比例：3:2。模式：编辑。
编辑附上的橡木床卧室照片，仅将燕麦色被套换成青绿色与象牙白相间的细竖条纹。条纹随现有布料褶皱和透视弯曲，保留柔软织物质感。两只燕麦色枕头保持原样，保留床架、床头柜、台灯、书、窗户、房间结构、视角和日光。不得增加靠垫、床尾毯、墙饰或文字。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Change only the stripe color from teal to rust; preserve stripe spacing and the pillows.
```

```text
只将青绿色条纹改为铁锈红，保留条纹间距与枕头。
```

**Review / 验收：** Striped duvet and two oatmeal pillows are present; room arrangement remains similar. Duvet folds drift slightly. 条纹被套与两只原色枕头符合要求，房间布局大体保留，被子褶皱略有变化。

[Back to index / 返回索引](README.md)


<a id="p064"></a>
## P064 · Souvenir city-name replacement / 纪念卡城市文字替换

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Souvenir city-name replacement: original input image by flaq.ai](../assets/images/launch-ticket-input.png)

[Souvenir city-name replacement — input: exact prompt / 实际提示词](../assets/generation/launch-ticket-input.txt)

![Souvenir city-name replacement: original edit image by flaq.ai](../assets/images/launch-ticket-edit.png)

[Souvenir city-name replacement — edit: exact prompt / 实际提示词](../assets/generation/launch-ticket-edit.txt)

### English

```text
Asset: Souvenir city-name replacement. Target aspect ratio: 3:2. Mode: edit.
On the supplied souvenir card, replace ONLY the city word 'PORTO' with exactly 'LISBON'. Preserve its original visual type style, navy color and text-box position. Keep 'HARBOR LOOP', '18 SEP 2026' and 'SOUVENIR · NOT VALID FOR TRAVEL' unchanged. Keep all original tram illustration details, coral rule, cream paper, border margins and landscape canvas. Do not localize or redraw the illustration; this is a typography replacement exercise, not a geographically revised card. No extra text.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：纪念卡城市文字替换。目标比例：3:2。模式：编辑。
使用附上的平面纪念卡，仅把城市名 PORTO 替换为 LISBON，保持同样的字体风格、字号、基线、字距与深蓝色。保留 HARBOR LOOP、18 SEP 2026 和 SOUVENIR · NOT VALID FOR TRAVEL 的全部内容。保留电车插画、奶油色纸张质感、边框和画幅。这是文字排版练习，不需要把插画改成新城市地理，也不要增加票务信息或二维码。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Replace only LISBON with KYOTO. Keep all other wording and illustration unchanged.
```

```text
只把 LISBON 换成 KYOTO，保留其他文字与插画。
```

**Review / 验收：** LISBON and the other required strings visually match. Illustration details drift slightly. This is a fictional souvenir, not a valid ticket. LISBON 与其他指定文字目测符合要求，插画细节略有变化；这是虚构纪念卡，不是有效车票。

[Back to index / 返回索引](README.md)


<a id="p065"></a>
## P065 · Symbol-marked cube rotation / 带符号立方体旋转

**Mode:** edit · **Target:** 1:1 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Symbol-marked cube rotation: original input image by flaq.ai](../assets/images/launch-cube-input.png)

[Symbol-marked cube rotation — input: exact prompt / 实际提示词](../assets/generation/launch-cube-input.txt)

![Symbol-marked cube rotation: original edit image by flaq.ai](../assets/images/launch-cube-edit.png)

[Symbol-marked cube rotation — edit: exact prompt / 实际提示词](../assets/generation/launch-cube-edit.txt)

### English

```text
Asset: Symbol-marked cube rotation. Target aspect ratio: 1:1. Mode: edit.
Edit the supplied cube still life by rotating ONLY the whole physical cube 90 degrees about its vertical axis so that the currently visible pale-teal TRIANGLE face becomes the large front-facing face, and the coral CIRCLE face moves to the visible LEFT face. The ivory SQUARE face stays on top. Preserve the identity of each colored face and its attached symbol: do not swap or repaint the symbols. Keep cube size, center position, matte material, camera, gray backdrop and upper-left light; update contact shadow coherently for the new orientation. No extra symbols or objects, same square canvas.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：带符号立方体旋转。目标比例：1:1。模式：编辑。
使用附上的立方体静物图，将整个实体立方体绕竖直轴旋转90度，让当前青绿色三角形面成为较大的正面，珊瑚色圆形面移到可见左侧，象牙白正方形面始终在顶部。每个符号必须附着在原本颜色的面上，不能通过换色或重画符号模拟旋转。保持尺寸、中心位置、哑光材质、相机、灰色背景和左上光源，阴影随旋转合理更新。保持正方形画幅，不增加物体。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Repair only the bent top outline into straight cube edges. Preserve each face color and symbol; verify perspective again.
```

```text
只将弯折的顶部轮廓修成笔直立方体边线，保留各面颜色和符号，再次检查透视。
```

**Review / 验收：** Partial result: face identities follow the intended arrangement, but a rigid 90-degree rotation is not established. The top outline has a visible kink. Do not use as validated geometry. 部分达成：符号与颜色的对应关系符合目标，但未验证严格90度刚体旋转，顶部轮廓有明显折点，不可作为精确几何示例。

[Back to index / 返回索引](README.md)


<a id="p066"></a>
## P066 · One-column itinerary revision / 旅行信息图单栏修改

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![One-column itinerary revision: original input image by flaq.ai](../assets/images/launch-travel-input.png)

[One-column itinerary revision — input: exact prompt / 实际提示词](../assets/generation/launch-travel-input.txt)

![One-column itinerary revision: original edit image by flaq.ai](../assets/images/launch-travel-edit.png)

[One-column itinerary revision — edit: exact prompt / 实际提示词](../assets/generation/launch-travel-edit.txt)

### English

```text
Asset: One-column itinerary revision. Target aspect ratio: 3:2. Mode: edit.
Edit only the MIDDLE column of the supplied fictional itinerary card. Replace '13:00' with exactly '14:00', replace 'GARDEN' with exactly 'STUDIO', and replace its greenhouse illustration with an original small pottery studio interior featuring a wooden workbench, three ceramic bowls and a single shelf, in the same green and cream screenprint style. Keep the column boundaries unchanged. Preserve the entire left and right columns, all their times and labels, the title 'A DAY IN LARK BAY', footer 'FICTIONAL ITINERARY', background, margins and landscape format. Do not add labels or change any other region.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：旅行信息图单栏修改。目标比例：3:2。模式：编辑。
编辑附上的虚构三栏旅行卡，只修改中间一栏：把 13:00 改成 14:00，把 GARDEN 改成 STUDIO，把花园画面换成绿色与奶油色的陶艺工作室，画出工作台、台上三个碗和一块置物搁板。保留标题 A DAY IN LARK BAY，左右两栏的 09:00 MARKET 与 17:00 PIER、相应插画、分栏边线以及底部 FICTIONAL ITINERARY。保持复古印刷纹理与文字层级，不新增活动或地址。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Change only STUDIO to POTTERY. Preserve 14:00, all three bowls and both outer columns.
```

```text
只把 STUDIO 换成 POTTERY，保留14:00、三个碗与左右两栏。
```

**Review / 验收：** Middle time and heading match; three bowls appear on the workbench. Extra vessels appear on the shelf. Outer columns remain recognizable but fine illustration details drift. 中栏时间与标题正确，工作台上有三个碗；搁板新增其他器皿。左右栏保留主要内容，但插画细节有漂移。

[Back to index / 返回索引](README.md)


<a id="p067"></a>
## P067 · Birthday candle count edit / 生日蜡烛数量修改

**Mode:** edit · **Target:** 1:1 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Birthday candle count edit: original input image by flaq.ai](../assets/images/launch-cake-input.png)

[Birthday candle count edit — input: exact prompt / 实际提示词](../assets/generation/launch-cake-input.txt)

![Birthday candle count edit: original edit image by flaq.ai](../assets/images/launch-cake-edit.png)

[Birthday candle count edit — edit: exact prompt / 实际提示词](../assets/generation/launch-cake-edit.txt)

### English

```text
Asset: Birthday candle count edit. Target aspect ratio: 1:1. Mode: edit.
Edit only the candles in the supplied birthday cake photograph. Increase the count from exactly three to exactly FIVE unlit slender orange candles in one straight evenly spaced row across the cake top, at the same depth, all fully visible. Keep candle style and height. Preserve the cake shape, ivory frosting, scalloped borders, cobalt plate, peach background, camera framing and soft lighting. No flames, no text, no numbers, no other new decorations. The final image must have exactly five separate candles, each with one visible wick.
Constraints: Attach the input image shown above, not both before/after images. Make only the requested change; inspect every preserved region.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：生日蜡烛数量修改。目标比例：1:1。模式：编辑。
使用附上的蛋糕静物图，把三根橙色未点燃蜡烛改为恰好五根，沿蛋糕顶部后半部均匀排成一列，每根独立清晰可数，保持相同高度、粗细和橙色。保留象牙白奶油蛋糕、奶油纹理、蓝色盘子、桃色背景、取景和柔和侧光。不要添加火焰、数字装饰、水果、文字、额外盘子或其他物品。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Light only the center candle. Keep exactly five candles and leave the other four unlit.
```

```text
只点燃中间一根蜡烛，保持总共五根，其他四根不点燃。
```

**Review / 验收：** Exactly five unlit orange candles are visible. Cake, plate and composition are similar; frosting texture changes slightly. 可清楚数出五根未点燃橙色蜡烛，蛋糕、盘子和构图大体保持，奶油纹理稍有变化。

[Back to index / 返回索引](README.md)

