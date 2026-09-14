#!/usr/bin/env python3
"""Build the visual index and exact-generation log from reviewed asset records."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def build():
    assets=json.loads((ROOT/'assets/manifest.json').read_text())['assets']
    catalog=json.loads((ROOT/'data/catalog.json').read_text())
    locales=json.loads((ROOT/'data/locales.json').read_text())
    latest={a['recipe_id']:a for a in assets if a.get('role') not in ('input','draft') and a['recipe_id']!='COVER'}
    lines=['# Visual prompt gallery', '', '[English README](../README.md) · [Prompt index](../prompts/README.md) · [Generation log](generation-log.md)', '',
           f'Browse {len(latest)} illustrated recipes by use case. Click an image to open its complete prompt, input references, customization options and review notes.', '',
           'These are original generated demonstrations. Follow-up suggestions are separate steps; only recorded outputs have been executed. Model IDs were not exposed by the generation tool. Examples can contain the limitations documented in their reviews.', '']
    packs=[(p['title']['en'],p['slug'],p['recipes']) for p in catalog['packs']]+[('Multilingual posters','11-multilingual',locales)]
    for title,slug,recipes in packs:
        lines += ['## '+title,'','| | | |','| --- | --- | --- |']
        cells=[]
        for r in recipes:
            a=latest[r['id']];name=r['title']['en'] if isinstance(r['title'],dict) else r['title'];link=f'../prompts/{slug}.md#{r["id"].lower()}'
            cells.append(f'[![{a["alt"]}](../{a["path"]})]({link})<br>**[{r["id"]} · {name}]({link})**')
        for i in range(0,len(cells),3):lines.append('| '+' | '.join((cells[i:i+3]+['']*3)[:3])+' |')
        lines+=['']
    (ROOT/'docs/gallery.md').write_text('\n'.join(lines).rstrip()+'\n')
    lines=['# Generation log · 图片生成记录','',f'{len(assets)} original PNG files, including synthetic inputs, first attempts and refined outputs. All 103 recipes have at least one generated result. Images were generated with the Codex built-in image tool; all editing references are this project’s own generated assets.','',
           'Each record preserves the exact executed prompt, input order, dimensions, SHA-256 and visual review. Model ID, seed and quality settings were not exposed and are not inferred. These examples are not verified Flare/Sunburst comparisons.','',
           '实际执行提示词与可复用配方可能略有不同。以下记录保留输入关系、原始文件和目测发现；后续修改建议只有出现独立输出记录时才代表已执行。','',
           '[Browse results by recipe](gallery.md) · [Machine-readable manifest](../assets/manifest.json)','']
    for a in assets:
        lines += ['## '+a['id']+' · '+a['label'],'',f'- Recipe: `{a["recipe_id"]}` · Role: {a.get("role","result")} · Date: {a["created"]}',f'- [Original PNG](../{a["path"]}) · {a["width"]} × {a["height"]}',f'- [Exact executed prompt](../{a["prompt_path"]})',f'- SHA-256: `{a["sha256"]}`','- Inputs: '+(' → '.join(f'[{i+1}](../{p})' for i,p in enumerate(a['input_images'])) or 'None'),'',f'**Review:** {a["review"]}','']
    (ROOT/'docs/generation-log.md').write_text('\n'.join(lines).rstrip()+'\n')
    print(f'Built gallery: {len(latest)} recipes; generation log: {len(assets)} assets.')
if __name__=='__main__':build()
