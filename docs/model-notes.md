# Images 2.5 model notes · 版本核对

Checked: **2026-09-09**. This page records the documentation consulted for this release; it is not an availability or performance guarantee.

## Documented API names

| Model ID | Documented positioning | Source |
| --- | --- | --- |
| `gpt-image-2.5-flare` | Fast everyday image generation | [Official model page](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) |
| `gpt-image-2.5-sunburst` | Image generation and editing where precision matters most | [Official model page](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) |

Both model pages list `low`, `medium`, `high`, `xhigh`, `max` and `auto` quality settings. Do not assume the bare name `gpt-image-2.5` is a documented endpoint identifier.

The official [image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting) recommends testing Flare when speed is the priority and Sunburst for demanding quality requirements. It documents transparent-background workflows for both.

For dimensions and output parameters, use the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation). Custom dimensions must be multiples of 16, within a 1:3 to 3:1 ratio, with neither edge above 3840 pixels and total pixels from 655,360 to 8,294,400. Resolutions above 2560×1440 are described as experimental. Transparent outputs use PNG or WebP. Ratios in the recipes describe creative framing; they are not API parameter strings.

## Upgrade comparison

See the [Image 2 vs Images 2.5 comparison](images-2-vs-2-5.md) for baseline capabilities, documented positioning, migration paths and an empty evaluation worksheet. The [playbook](playbook.md) connects these decisions to existing recipes.

## Our editorial recommendations

Use the same source images and acceptance criteria when trying models. Start with a moderate quality setting, inspect the result, then decide whether changing quality is justified. Do not assume a higher setting fixes unclear wording or wrong source data.

For edits, we recommend naming the target region, the desired change and the preserved details. Approve each result before moving to the next change. These practices make the task easier to evaluate; they do not guarantee unchanged pixels.

## What this release does not establish

- Built-in example generation did not expose a model ID, quality setting or seed. The manifest records these limits rather than guessing.
- No latency, cost, accuracy, model-comparison or language-success benchmark was run.
- No assumption is made about a particular account’s rollout, quota or UI controls.
- No claim is made that flaq.ai currently offers these exact endpoints. Check provider documentation before configuring an integration.
- API snippets were reviewed against the documentation but not executed against a billed endpoint.

## 中文说明

已核对的API名称为 `gpt-image-2.5-flare` 与 `gpt-image-2.5-sunburst`，不要把项目标题当作模型ID。本文不承诺账户可用性、价格、限额或速度。

本库针对2.5的细化主要体现在：把参考图角色说清、将局部修改和保持项分开、逐轮使用确认稿、检查系列一致性。内置生图示例未返回底层型号，因此不能标注为指定型号测评。精确尺寸、透明输出及质量参数请以上方官方文档为准。
