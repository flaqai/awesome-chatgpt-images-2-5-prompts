# Precise edits & multi-turn workflows · 精准修改与多轮工作流

[All recipes / 全部配方](README.md)

Images 2.5 workflow focus: **Change one thing / 单变量修改**.

Copy one language block. For edits, attach the images named in the prompt in that order. Requested ratios are creative targets; verify actual output dimensions.

任选一种语言复制。编辑任务须按提示顺序附参考图；比例为创作目标，输出后核对实际尺寸。

- [P019 · Product colorway edit](#p019)
- [P020 · Remove a tabletop distraction](#p020)
- [P021 · Window-light evening relight](#p021)
- [P022 · Poster text replacement](#p022)
- [P023 · Sketch-guided planter placement](#p023)
- [P024 · Clean product cutout](#p024)

<a id="p019"></a>
## P019 · Product colorway edit / 商品配色局部修改

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.

![Jade-green lamp base with original campaign typography](../assets/images/tideline-lamp-jade.png)

[Edit 1: base color: exact prompt / 实际提示词](../assets/generation/tideline-lamp-jade.txt)

![Jade-green lamp with YOUR EVENING, UPGRADED headline](../assets/images/tideline-lamp-copy.png)

[Edit 2: headline: exact prompt / 实际提示词](../assets/generation/tideline-lamp-copy.txt)

### English

```text
Asset: Product colorway edit. Target aspect ratio: 3:2. Mode: edit.
Image 1 is an approved product ad. Change only the lamp’s cylindrical base from midnight blue to muted jade green. Keep the original anodized texture and physically plausible highlight gradient. Do not recolor the ivory shade or orange pull tab. Treat the surrounding campaign as locked artwork.
Constraints: Preserve all copy, positions, scale, camera, background and shadows as closely as possible.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：商品配色局部修改。目标比例：3:2。模式：编辑。
图1为已确认商品广告。只将台灯圆柱底座由午夜蓝改为低饱和玉绿色，保持原阳极金属纹理和可信高光渐变，不改象牙白灯罩或橙色拉环，将周围广告视为锁定稿。
约束：尽量保持全部文字、位置、比例、镜头、背景和阴影。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
On this approved green version, change only "LIGHT, UNPLUGGED." to "YOUR EVENING, UPGRADED."; retain green.
```

```text
在已确认绿色版本上，仅将“LIGHT, UNPLUGGED.”改为“YOUR EVENING, UPGRADED.”，保留绿色。
```

**Review / 验收：** Compare base edges, metal sheen, pull tab and typography across all versions. 比较各版本底座边缘、金属光泽、拉环和排版。

[Back to index / 返回索引](README.md)


<a id="p020"></a>
## P020 · Remove a tabletop distraction / 去除桌面杂物

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。

### English

```text
Asset: Remove a tabletop distraction. Target aspect ratio: 3:2. Mode: edit.
Image 1 is the source room photograph. Remove only the empty plastic bottle at the front-right corner of the table. Reconstruct the small exposed tabletop area with continuous wood grain, matching perspective, natural illumination and contact shading from nearby objects.
Constraints: Keep table outline, chairs, books, windows and crop unchanged; retain all unrelated objects.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：去除桌面杂物。目标比例：3:2。模式：编辑。
图1为房间原照。只去掉桌子右前角的空塑料瓶，用连续木纹补全露出的桌面小区域，匹配透视、自然照明和旁边物件的接触阴影。
约束：保留桌子轮廓、椅子、书、窗和裁切，其他物件均不动。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Correct only any remaining bottle-shaped reflection, keeping the repaired wood grain.
```

```text
仅修正残留瓶形反光，保留已修复木纹。
```

**Review / 验收：** Look for repeating texture, soft patches and altered nearby edges. 检查重复纹理、模糊补丁和被改变的邻近边缘。

[Back to index / 返回索引](README.md)


<a id="p021"></a>
## P021 · Window-light evening relight / 室内窗光转傍晚

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。

### English

```text
Asset: Window-light evening relight. Target aspect ratio: 3:2. Mode: edit.
Use Image 1 as the exact room layout. Change the lighting from midday to early evening: cooler dim light outside the window and warm light from the existing desk lamp. Adjust only illumination, associated shadows and reflections. Maintain realistic exposure without turning the room orange.
Constraints: Do not move furniture, create new light fixtures, change materials or widen the room.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：室内窗光转傍晚。目标比例：3:2。模式：编辑。
以图1为准确房间布局，将正午光改成傍晚：窗外较暗冷光，室内原有台灯暖光。只改照明及相应阴影、反射，保持真实曝光，避免整间房泛橙。
约束：不移动家具、不新建灯具、不改材料、不扩大空间。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Lower only the lamp brightness slightly while preserving the cooler window light.
```

```text
只略微降低台灯亮度，保留窗外冷光。
```

**Review / 验收：** Check shadow directions and whether all surfaces share the same lighting logic. 检查阴影方向及所有表面的光照逻辑是否一致。

[Back to index / 返回索引](README.md)


<a id="p022"></a>
## P022 · Poster text replacement / 海报文案定点替换

**Mode:** edit · **Target:** 2:3 · **Author:** flaq.ai team

**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。

### English

```text
Asset: Poster text replacement. Target aspect ratio: 2:3. Mode: edit.
Image 1 is the approved poster. Replace only the headline with "A SLOWER SATURDAY". Keep its original type style, visual weight and alignment; permit an extra line within the existing headline box if required. Match paper texture behind removed letters.
Constraints: Do not change date, venue, image, colors or layout outside the title box; do not leave old letter fragments.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：海报文案定点替换。目标比例：2:3。模式：编辑。
图1为确认版海报。仅将标题替换为“A SLOWER SATURDAY”，保持原字体风格、字重与对齐；如有需要可在原标题框内增加一行。清除旧字后补回一致纸纹。
约束：不改日期、场地、图片、颜色或标题框外版式，不残留旧字碎片。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Fix only a misspelled headline character; repeat the exact approved headline.
```

```text
仅修复标题中的错字，重复完整确认标题。
```

**Review / 验收：** Read all text, including untouched small print, against the original. 对照原图阅读所有文字，包括未修改小字。

[Back to index / 返回索引](README.md)


<a id="p023"></a>
## P023 · Sketch-guided planter placement / 草图引导添加花盆

**Mode:** edit · **Target:** 3:2 · **Author:** flaq.ai team

**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。

### English

```text
Asset: Sketch-guided planter placement. Target aspect ratio: 3:2. Mode: edit.
Image 1 is the terrace photo; Image 2 is a rough sketch showing a planter along the left parapet. Use the sketch only for location and approximate silhouette. Add one low rectangular terracotta planter with three rosemary plants, consistent with the photo’s perspective and sun direction.
Constraints: Remove sketch strokes from the result; preserve parapet, floor tiles, sky and camera angle.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：草图引导添加花盆。目标比例：3:2。模式：编辑。
图1为露台照片，图2为左侧矮墙边花盆草图。草图只指导位置和大致轮廓。添加一个低矩形陶土花盆，种三株迷迭香，匹配照片透视和阳光方向。
约束：成图不保留草图笔迹，保留矮墙、地砖、天空和镜头角度。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Shorten only the planter width by 10%, keeping its left edge anchored.
```

```text
仅缩短花盆宽度10%，左边缘固定。
```

**Review / 验收：** Check floor contact, parapet occlusion and that there is only one planter. 检查落地接触、矮墙遮挡关系及花盆数量。

[Back to index / 返回索引](README.md)


<a id="p024"></a>
## P024 · Clean product cutout / 干净商品抠图

**Mode:** edit · **Target:** 1:1 · **Author:** flaq.ai team

**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。

### English

```text
Asset: Clean product cutout. Target aspect ratio: 1:1. Mode: edit.
Isolate the exact product in Image 1 on a genuinely transparent background. Preserve fine edges, interior openings, translucent material behavior and the full silhouette. Keep original product color, proportions and surface detail; do not redraw a simplified substitute.
Constraints: No painted checkerboard, white rectangle, drop shadow or cropped edges.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

### 简体中文

```text
交付物：干净商品抠图。目标比例：1:1。模式：编辑。
将图1中准确商品抠到真正透明背景，保留细小边缘、内部开孔、半透明材质特征和完整轮廓。保持原色、比例和表面细节，不重画简化替代品。
约束：不绘制棋盘格、不加白矩形、投影、不裁断边缘。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

### Next edit / 后续修改

```text
Remove only any remaining edge halo without eroding thin details.
```

```text
只移除残留边缘光晕，不侵蚀细节。
```

**Review / 验收：** Inspect actual alpha on light and dark backgrounds; reject simulated transparency. 在明暗底色上检查实际透明通道，拒绝假透明。

[Back to index / 返回索引](README.md)

