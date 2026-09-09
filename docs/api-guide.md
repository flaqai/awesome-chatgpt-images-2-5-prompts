# GPT Image 2.5 API guide

These are **documentation examples, not executed API tests**. They use OpenAI’s API directly. They do not claim compatibility with a third-party endpoint or demonstrate that flaq.ai currently serves the same model IDs.

For **GPT Image 2 through Flaq.ai**, see the [README integration introduction](../README.md#gpt-image-2-api-on-flaqai), [generation API](https://flaq.ai/models/openai/gpt-image-2/), [editing API](https://flaq.ai/models/openai/gpt-image-2-edit/) and [Flaq.ai API reference](https://flaq.ai/docs/?page=api/gpt-image-2). Those are separate provider routes from the direct OpenAI Images 2.5 examples below.

Consult the official [image generation guide](https://developers.openai.com/api/docs/guides/image-generation) and [model notes](model-notes.md) before use. Set `OPENAI_API_KEY` in your environment; never commit credentials. Install the current `openai` Python package in your own environment.

## Generate from an exact repository prompt

Run from the repository root. This writes a new file under `output/`; change the name for each approved version.

```python
import base64
from pathlib import Path
from openai import OpenAI

client = OpenAI()
prompt = Path("assets/generation/tideline-lamp.txt").read_text(encoding="utf-8")
result = client.images.generate(
    model="gpt-image-2.5-flare",
    prompt=prompt,
    size="1536x1024",
    quality="medium",
    output_format="png",
)
output = Path("output/lamp-flare-v1.png")
output.parent.mkdir(parents=True, exist_ok=True)
with output.open("xb") as image_file:
    image_file.write(base64.b64decode(result.data[0].b64_json))
```

## Edit the approved output

The source image is the state of the creative work. A filename mentioned only inside prompt text does not upload the image.

```python
import base64
from pathlib import Path
from openai import OpenAI

client = OpenAI()
prompt = Path("assets/generation/tideline-lamp-jade.txt").read_text(encoding="utf-8")
with Path("output/lamp-flare-v1.png").open("rb") as source:
    result = client.images.edit(
        model="gpt-image-2.5-sunburst",
        image=source,
        prompt=prompt,
        size="1536x1024",
        quality="high",
        output_format="png",
    )
with Path("output/lamp-jade-sunburst-v1.png").open("xb") as destination:
    destination.write(base64.b64decode(result.data[0].b64_json))
```

For the next headline change, pass the **newly approved green image** as the source and use [this exact edit prompt](../assets/generation/tideline-lamp-copy.txt). Do not restart from the blue original if you want the green color to persist.

## Common configuration decisions

| Need | Practical starting point |
| --- | --- |
| Normal landscape example | `size="1536x1024"` |
| Vertical poster | `size="1024x1536"` |
| Square composition | `size="1024x1024"` |
| Everyday generation | Test `gpt-image-2.5-flare` |
| Demanding editing | Test `gpt-image-2.5-sunburst` |
| Transparent cutout | `background="transparent"`, `output_format="png"`; inspect alpha |
| Reliable reproduction records | Save exact prompt, input files, model ID, parameters and output hash |

These are starting points, not validated optimum settings. Preserve the same inputs when comparing model quality. A transparent checkerboard drawn into RGB pixels is not an alpha channel.

## 中文使用提示

上方示例直接连接OpenAI，未实际执行计费调用，不代表第三方平台接口兼容。环境变量中设置密钥，不要写入仓库。编辑必须真正上传图片，不能只在提示词里写本地路径。第二轮应使用第一轮确认图，保存不同版本以便回退。

若API拒绝参数，核对当前官方文档和已安装SDK版本；不要静默切换到另一个模型并沿用原模型名称。输出文字、材质、人物与透明通道仍需检查。
