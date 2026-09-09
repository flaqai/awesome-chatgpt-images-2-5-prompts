#!/usr/bin/env python3
"""Render bilingual Markdown and machine-readable full prompts from authored data."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def build():
    data = json.loads((ROOT/'data/catalog.json').read_text())
    manifest = json.loads((ROOT/'assets/manifest.json').read_text())
    examples = {}
    core_count = sum(len(pack['recipes']) for pack in data['packs'])
    for asset in manifest['assets']:
        examples.setdefault(asset['recipe_id'], []).append(asset)
    index = ['# Prompt index · 提示词索引', '', '[English](../README.md) · [简体中文](../README_zh.md)', '',
             f'{core_count} bilingual core recipes + 12 language-specific recipes. Translations and follow-ups are not counted as separate recipes.', '',
             f'{core_count} 条中英双语核心配方 + 12 条语言专用配方；翻译和后续修改不重复计数。', '',
             '| ID | English | 中文 | Mode | Ratio |', '| --- | --- | --- | --- | --- |']
    full=[]
    for pack in data['packs']:
        lines=[f'# {pack["title"]["en"]} · {pack["title"]["zh"]}', '', '[All recipes / 全部配方](README.md)', '',
               f'Images 2.5 workflow focus: **{pack["focus"]}**.', '',
               'Copy one language block. For edits, attach the images named in the prompt in that order. Requested ratios are creative targets; verify actual output dimensions.', '',
               '任选一种语言复制。编辑任务须按提示顺序附参考图；比例为创作目标，输出后核对实际尺寸。', '']
        if pack.get('source_url'):
            lines += [f'Scenario inspiration: [OpenAI launch article]({pack["source_url"]}). Original flaq.ai prompts and newly generated images; not copied official demonstrations. [Before/after guide](../docs/launch-examples.md).', '']
        lines += [f'- [{r["id"]} · {r["title"]["en"]}](#{r["id"].lower()})' for r in pack['recipes']]
        for r in pack['recipes']:
            index.append(f'| {r["id"]} | [{r["title"]["en"]}]({pack["slug"]}.md#{r["id"].lower()}) | {r["title"]["zh"]} | {r["mode"]} | {r["ratio"]} |')
            lines += ['', f'<a id="{r["id"].lower()}"></a>', f'## {r["id"]} · {r["title"]["en"]} / {r["title"]["zh"]}', '',
                      f'**Mode:** {r["mode"]} · **Target:** {r["ratio"]} · **Author:** flaq.ai team', '']
            if r['id'] in examples:
                lines += ['**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.', '']
                for a in examples[r['id']]:
                    lines += [f'![{a["alt"]}](../{a["path"]})', '', f'[{a["label"]}: exact prompt / 实际提示词](../{a["prompt_path"]})', '']
            else:
                lines += ['**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。', '']
            complete={}
            for lang,label in [('en','English'),('zh','简体中文')]:
                if lang=='en':
                    text=f'Asset: {r["title"][lang]}. Target aspect ratio: {r["ratio"]}. Mode: {r["mode"]}.\n'+r['brief'][lang]+'\nConstraints: '+r['constraints'][lang]+'\nRender only explicitly requested image text. Do not add unrelated logos, signatures or captions.'
                else:
                    text=f'交付物：{r["title"][lang]}。目标比例：{r["ratio"]}。模式：'+('新建' if r['mode']=='generate' else '编辑')+'。\n'+r['brief'][lang]+'\n约束：'+r['constraints'][lang]+'\n只渲染明确要求的图中文字，不添加无关标识、签名或说明。'
                complete[lang]=text
                lines += [f'### {label}', '', '```text',text,'```','']
            lines += ['### Next edit / 后续修改', '', '```text', r['revision']['en'], '```', '', '```text', r['revision']['zh'], '```', '',
                      '**Review / 验收：** '+r['review']['en']+' '+r['review']['zh'], '',
                      '[Back to index / 返回索引](README.md)', '']
            full.append({**r,'pack':pack['slug'],'prompt':complete,'examples':[a['path'] for a in examples.get(r['id'],[])]})
        (ROOT/'prompts'/f'{pack["slug"]}.md').write_text('\n'.join(lines)+'\n')
    locales=json.loads((ROOT/'data/locales.json').read_text())
    localized=['# Multilingual image prompts · 多语言图像提示词', '', '[All recipes / 全部配方](README.md)', '',
        '12 complete localized briefs. These are language-specific recipes, not full translations of the entire library. Language templates need fluent review; only L003 has a generated visual in this release.', '',
        '12 条完整本地语言创作简报，不代表全库已翻译为12种语言。公开使用前请熟练读者审校；当前仅 L003 配有生成示例。', '']
    for r in locales:
        index.append(f'| {r["id"]} | [{r["title"]}](11-multilingual.md#{r["id"].lower()}) | {r["language"]} | generate | 2:3 |')
        localized += [f'<a id="{r["id"].lower()}"></a>',f'## {r["id"]} · {r["title"]}', '', '```text',r['prompt'],'```','', '**Review:** '+r['review'],'']
        for a in examples.get(r['id'],[]):
            localized += [f'![{a["alt"]}](../{a["path"]})','',f'[Exact generation prompt / 实际生成提示词](../{a["prompt_path"]})','']
    (ROOT/'prompts/11-multilingual.md').write_text('\n'.join(localized)+'\n')
    (ROOT/'prompts/README.md').write_text('\n'.join(index)+'\n')
    (ROOT/'data/prompts.json').write_text(json.dumps({'core':full,'localized':locales},ensure_ascii=False,indent=2)+'\n')
    print(f'Rendered {len(full)} core recipes and {len(locales)} localized recipes.')
if __name__=='__main__':
    build()
