# Multilingual design · 多语言排版

The core library has full English and Simplified Chinese prompts. The [language pack](../prompts/11-multilingual.md) adds 12 complete local-language briefs. Japanese, Spanish, French and Arabic READMEs are localized entry pages, not full-library translations. No native-review certification is claimed.

## Separate instruction language from image copy

You can write instructions in English while quoting Japanese image text. You can also give the whole brief in Japanese. Pick the form your reviewer can verify; do not mix several versions of the same headline without explaining which one to render.

```text
Edit the supplied approved poster.
Replace only the headline with exactly "把夜晚留给自己".
Keep the brand name "TIDELINE" in Latin letters.
Reflow within the existing text box, using readable Simplified Chinese typography.
Preserve the product, lighting, background, palette and all other copy.
```

## Script-aware review

| Language/script | Specific review task |
| --- | --- |
| English | Apostrophes, title spelling, punctuation and accidental extra words |
| Simplified Chinese | Wrong or substituted characters; spacing and punctuation |
| Japanese | Kana/kanji accuracy, full glyphs and punctuation; avoid arbitrary mixed vertical flow |
| Korean | Complete Hangul syllable blocks, final consonants and natural spacing |
| Spanish | Accents and ñ; retain inverted punctuation when supplied |
| French | Accents, apostrophes and punctuation spacing appropriate to the locale |
| German | Umlauts, ß and long compound-word wrapping |
| Portuguese | Tildes, cedillas and the specified regional wording |
| Arabic | Right-to-left reading order, joined letters and Latin brand placement |
| Hindi | Devanagari vowel marks, conjuncts and headline continuity |
| Thai | Vowel/tone marks above and below letters; line spacing and meaningful wraps |
| Russian | Genuine Cyrillic letters rather than visually similar Latin substitutions |

## Localization handoff

Prepare an approved text table outside the image. Record locale, headline, subtitle, brand, date and number format. Supply one locale per generation or edit. Allow text-box reflow while preserving the surrounding design. Ask a fluent reader to check the output at actual display size.

Do not use an image model to determine current prices, event details or translations of regulated claims. Provide the approved wording yourself. For exact publication copy, use a design tool to typeset over a clean generated image.

## 中文说明

指令语言和图中文字语言是两件事。先确定译文，再要求渲染；品牌可保持原文，正文按目标语言重排。不要强行沿用英文换行导致中文挤压或阿拉伯文方向错误。每种语言单独生成和审校，未审校的版本不要标成母语校对完成。
