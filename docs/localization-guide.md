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

## README language coverage

The project has **16 README language and regional versions**. English is the default. English and Simplified Chinese contain the full project overview; the other versions are localized entry pages with a sample prompt, usage guidance, example limitations and Flaq.ai links. Linked guides and recipes retain their own languages.

README availability, recipe translation and on-image text quality are separate concerns. There are 73 bilingual recipes in English and Simplified Chinese, 12 English-only workflow recipes and 12 additional language-specific recipes. New Italian, Indonesian, Vietnamese and Traditional Chinese README examples adapt existing recipes; they do not increase the 97-recipe total and have not been rendered. Independent native-language editorial review has not been recorded.

| README | Locale | Scope |
| --- | --- | --- |
| [English](../README.md) | `en` | Full project overview |
| [简体中文](../README_zh.md) | `zh-Hans` | Full project overview |
| [繁體中文](../README_tw.md) | `zh-Hant` | Localized entry page + sample prompt |
| [日本語](../README_ja.md) | `ja` | Localized entry page + sample prompt |
| [한국어](../README_ko.md) | `ko` | Localized entry page + sample prompt |
| [Español](../README_es.md) | `es` | Localized entry page + sample prompt |
| [Français](../README_fr.md) | `fr` | Localized entry page + sample prompt |
| [Deutsch](../README_de.md) | `de` | Localized entry page + sample prompt |
| [Português (Brasil)](../README_pt.md) | `pt-BR` | Localized entry page + sample prompt |
| [Italiano](../README_it.md) | `it` | Localized entry page + sample prompt |
| [Русский](../README_ru.md) | `ru` | Localized entry page + sample prompt |
| [العربية](../README_ar.md) | `ar` | Localized entry page + sample prompt |
| [हिन्दी](../README_hi.md) | `hi` | Localized entry page + sample prompt |
| [ไทย](../README_th.md) | `th` | Localized entry page + sample prompt |
| [Bahasa Indonesia](../README_id.md) | `id` | Localized entry page + sample prompt |
| [Tiếng Việt](../README_vi.md) | `vi` | Localized entry page + sample prompt |

For translation contributions, preserve recipe counts and model distinctions, verify every local link, and request fluent editorial review before labeling a version as reviewed. Do not count a translated README example as a new recipe.
