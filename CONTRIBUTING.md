# Contributing to the flaq.ai prompt library

We welcome original practical recipes, language corrections and honestly documented examples. Keep contributions useful to someone with a real creative task.

## Add a recipe

Edit [data/catalog.json](data/catalog.json) for bilingual core entries or [data/locales.json](data/locales.json) for language-specific entries. Use the next available stable ID; do not renumber existing recipes.

Include:

- A concrete deliverable and target aspect ratio.
- A complete brief with subject, composition, material/light and exact copy when needed.
- Input-image roles for editing tasks.
- Explicit constraints, one follow-up edit and observable review criteria.
- Accurate rendering status. A suggested prompt is not a tested example.

Regenerate the Markdown and exported prompt data:

```sh
python3 scripts/build_catalog.py
python3 scripts/validate.py
```

The scripts use Python’s standard library. Do not edit generated prompt Markdown as the only source of a change. Update counts and the changelog when adding entries; the checker verifies the documented totals.

## Add an image

Use material you have the right to share. Store the full exact prompt in `assets/generation/`, the image in `assets/images/`, and its record in `assets/manifest.json`. Record the recipe ID, actual creation date, input images, output dimensions, SHA-256 hash, generation method and visible limitations. If the model ID is unavailable, use `null`; never infer a specific model from the interface’s product name.

Keep existing images and create a new version for revisions. Preserve provenance metadata. Include a short review of typography, subject fidelity, composition and any known errors. Do not present benchmark claims without reproducible evidence.

## Originality and language review

Read [the originality policy](docs/originality.md). A contribution must have independently written creative direction or appropriate third-party notices. Avoid copying a distinctive composition together with its text and prompt structure. Mark translations that have not received fluent review. Do not replace unfamiliar script characters with look-alike glyphs.

Contributions are submitted under the repository’s [MIT License](LICENSE), subject to any clearly identified third-party rights. Do not add secrets, private portraits without permission or unsupported endorsements.

## 中文投稿要求

在数据文件中新增或修改配方，写清用途、参考图角色、约束、追问和验收。配图需要真实生成记录，不知道模型ID就填空，不把模板标成已实测。运行生成与校验脚本，更新数量和日志。欢迎语言审校，说明是否经过熟练读者检查。
