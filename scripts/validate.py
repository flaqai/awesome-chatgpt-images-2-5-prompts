#!/usr/bin/env python3
"""Validate recipe records, local Markdown links, exact-prompt records and images."""
import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)
def read_json(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))
def anchors(path):
    content=path.read_text(encoding='utf-8')
    found=set(re.findall(r'<a\s+id="([^"]+)"',content))
    counts={}
    for heading in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
        heading=re.sub(r'[^\w\- ]','',heading.strip().lower()).replace(' ','-')
        n=counts.get(heading,0); counts[heading]=n+1
        found.add(heading if n==0 else f'{heading}-{n}')
    return found

def main():
    catalog=read_json('data/catalog.json')
    locales=read_json('data/locales.json')
    exported=read_json('data/prompts.json')
    manifest=read_json('assets/manifest.json')['assets']
    recipes=[r for p in catalog['packs'] for r in p['recipes']]
    ids=[r['id'] for r in recipes+locales]
    require(len(ids)==len(set(ids)), 'Duplicate recipe IDs')
    require(len(recipes)==85 and len(locales)==12, 'Update documented recipe totals for this release')
    require(sum(r.get('languages')==['en'] for r in recipes)==12, 'Expected 12 English-only workflow recipes')
    require(len(catalog['packs'])==13, 'Expected 13 core packs')
    require(len({r['language'] for r in locales})==12, 'Expected 12 language briefs')
    require(len(exported['core'])==len(recipes), 'Exported core count mismatch')
    require(exported['localized']==locales, 'Stale localized export: rebuild catalog')
    byid={r['id']:r for r in exported['core']}
    for r in recipes:
        languages = r.get('languages', ['en','zh'])
        require(languages in [['en'], ['en','zh']], f'{r["id"]}: unsupported recipe languages')
        for field in ['title','brief','constraints','revision','review']:
            require(set(r[field])==set(languages),f'{r["id"]}: missing translation in {field}')
            require(all(r[field].values()),f'{r["id"]}: empty {field}')
        require(r['mode'] in ['edit','generate'],f'{r["id"]}: invalid mode')
        require(re.fullmatch(r'\d+:\d+',r['ratio']) is not None,f'{r["id"]}: invalid ratio')
        require(len(r['brief']['en'].split())>=35,f'{r["id"]}: brief too short')
        require('{{' not in r['brief']['en'],f'{r["id"]}: unresolved example placeholder')
        exported_r=byid.get(r['id'],{})
        for field in r:
            require(exported_r.get(field)==r[field],f'{r["id"]}: stale exported {field}')
        for lang in languages:
            require(r['brief'][lang] in exported_r.get('prompt',{}).get(lang,''),f'{r["id"]}: missing full prompt')
    require(len(manifest)==28,'Expected 28 recorded images')
    require(len({a['path'] for a in manifest})==len(manifest),'Duplicate image records')
    for a in manifest:
        path=ROOT/a['path']
        require(path.is_file(),f'Missing image: {path}')
        if not path.is_file(): continue
        data=path.read_bytes()
        require(data.startswith(b'\x89PNG\r\n\x1a\n'),f'Invalid PNG: {path}')
        require(struct.unpack('>II',data[16:24])==(a['width'],a['height']),f'Dimension mismatch: {path}')
        require(hashlib.sha256(data).hexdigest()==a['sha256'],f'Hash mismatch: {path}')
        require(a['recipe_id'] in ids+['COVER'],f'Unknown recipe: {a["recipe_id"]}')
        prompt=ROOT/a['prompt_path']
        require(prompt.is_file() and prompt.stat().st_size>100,f'Missing exact prompt: {prompt}')
        require(bool(a['review']),f'Missing review: {path}')
        require(a['model_id'] is None, f'Unexpected model claim: {path}')
        for source in a['input_images']:
            require((ROOT/source).is_file(),f'Missing image input: {source}')
    files=list(ROOT.rglob('*.md'))
    link_count=0
    for path in files:
        if '.git' in path.parts: continue
        content=path.read_text(encoding='utf-8')
        require(content.count('```')%2==0,f'Unclosed code fence: {path}')
        # Remove fenced examples before checking document links.
        content=re.sub(r'```.*?```','',content,flags=re.S)
        for match in re.finditer(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',content):
            target=match.group(1).strip('<>')
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc: continue
            link_count+=1
            dest=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            require(dest.exists(),f'Broken link in {path.relative_to(ROOT)}: {target}')
            if dest.is_file() and dest.suffix=='.md' and parsed.fragment:
                require(unquote(parsed.fragment) in anchors(dest),f'Broken anchor in {path.relative_to(ROOT)}: {target}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(ids)} recipes, 12 languages, {len(manifest)} PNGs, {len(files)} Markdown files, {link_count} local links.')

if __name__=='__main__':
    main()
