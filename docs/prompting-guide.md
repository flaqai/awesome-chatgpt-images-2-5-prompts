# Practical image prompting · 实用提示词方法

This is the flaq.ai team’s working method for this collection. The [official image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting) is the reference for model guidance; the briefs and examples here are independently composed.

Choose a complete scenario in the [10-workflow playbook](playbook.md), or review the [model upgrade comparison](images-2-vs-2-5.md).

## Write a brief that can be reviewed

A useful brief establishes a visible goal. “A product photo that leaves room for a headline” is more actionable than a string of quality adjectives. Describe the object’s shape, real materials, position, light and relationship to the text.

```text
Deliverable: {{ASSET}}, intended for {{DESTINATION}}; target ratio {{RATIO}}.
Primary subject: {{SUBJECT_AND_DISTINCTIVE_DETAILS}}.
Environment: {{SCENE_AND_MATERIALS}}.
Layout: {{SUBJECT_POSITION}}, {{TEXT_AREA}}, {{MARGINS}}.
Lighting: {{DIRECTION_AND_SOFTNESS}}.
Exact image text: {{APPROVED_COPY}}. No other text.
References: Image 1 = {{ROLE}}; Image 2 = {{ROLE}}.
Locked details: {{PRESERVE_LIST}}.
Allowed changes: {{CHANGE_LIST}}.
```

Remove unused lines. Replace every placeholder before generating. Ratios are layout intentions, not guaranteed dimensions; inspect the saved image. For image editing, describe the actual input instead of adding a new scene that conflicts with it.

## Make each instruction observable

| Vague instruction | Reviewable replacement |
| --- | --- |
| Make it premium | Brushed metal, controlled glass reflections, one object, generous margins |
| Keep it consistent | Keep amber eye, teal apron, round cream head and orange seam |
| Better typography | Quote the exact headline, its alignment, maximum lines and clear background |
| Add realistic light | One large soft source above left; coherent contact shadows |
| Make it commercial | Identify the placement, target audience and text safe area |
| Don’t change anything | Name the features that matter, then compare the output to the input |

## Use an approval sequence

1. Generate a base composition and select one version.
2. Check the most expensive mistake first: identity, geometry or factual content.
3. Save the approved output under a new filename.
4. Change one variable: copy, color, material, light or crop.
5. Compare against the approved input. If it drifts, retry from that input rather than accumulating repairs.

An instruction to preserve details is an objective, not a promise. Small shifts can appear outside the intended region. The [lamp example](editing-case-study.md) illustrates both useful continuity and visible drift.

## Reference-image roles

| Role | What to extract | What not to assume |
| --- | --- | --- |
| Identity reference | Face, coat markings, distinctive features | Automatic permission to use a person |
| Product reference | Shape, proportions, label, material | Hidden construction or specifications |
| Base scene | Camera, layout, environment | Permission to move everything |
| Material reference | Texture and finish | Its object shape or background |
| Sketch | Position, silhouette, rough composition | Final materials or engineering accuracy |

Keep the role list short and ordered. For three-image composites, verify the tool received all three images before interpreting a failed output as a prompt problem.

## Text and multilingual design

Lock the final copy before generating. Provide the exact string rather than asking the image model to invent a translation and render it simultaneously. Keep long copy out of textured areas. For legal text, long documents or final typography, create the illustration first and typeset separately.

## Troubleshooting

| Symptom | Try next |
| --- | --- |
| Product shape changes | Use the approved source and explicitly list the silhouette, proportions and label as fixed |
| Headline is misspelled | Edit only the text region with the exact complete string |
| Layout is crowded | Remove secondary objects; reduce copy before shrinking text |
| Character drifts | Repeat signature traits and attach the character sheet |
| Multi-panel action is out of order | State each panel’s precondition; fix the affected panel only |
| Data graphic is wrong | Verify numbers and geometry; use deterministic chart tools for final publication |
| Cutout has a checkerboard | Request actual transparency and inspect the alpha channel |
| Generated UI looks good but cannot be used | Treat it as a reference for implementation, not exported application code |

## 中文速查

先写用途，再写主体、场景、构图、光线和准确文案。编辑时明确“只改什么”和“保留什么”，每次使用最近确认稿，并在每轮后检查差异。不要同时要求换风格、换背景、换字、换姿势，再期望人物或商品完全不动。

关键错误优先检查：人像看眼距、鼻子、发际线；商品看轮廓、接口、标贴；分镜看动作发生顺序；信息图看数值和关系；本地化看字符、方向和标点。无法确定的图像细节应留待审校，不写成已验证事实。
