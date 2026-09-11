# Awesome ChatGPT Images 2.5 Prompts

**A practical, multilingual prompt library for image generation and editing — product photos, ads, portraits, typography, UI concepts, infographics and storyboards.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Recipes: 97](https://img.shields.io/badge/Original_recipes-97-0f766e)](prompts/README.md)
[![Core: EN + Chinese](https://img.shields.io/badge/Core_prompts-EN_%2B_Chinese-f97316)](prompts/README.md)

**English** · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português (Brasil)](README_pt.md) · [Italiano](README_it.md) · [Русский](README_ru.md) · [العربية](README_ar.md) · [हिन्दी](README_hi.md) · [ไทย](README_th.md) · [Bahasa Indonesia](README_id.md) · [Tiếng Việt](README_vi.md)

![ChatGPT Images 2.5 prompt library by flaq.ai: Make ideas visible, with original tactile paper and ceramic objects](assets/images/cover.png)

> Created and maintained by the [flaq.ai](https://flaq.ai) team. Flaq.ai gives developers building AI agents and creative applications a unified API for image, video, music and language models.

[Start with a prompt](#quick-start) · [Browse use cases](#prompt-library) · [View examples](#featured-examples) · [Use the Flaq.ai API](#gpt-image-2-api-on-flaqai) · [Join the affiliate program](#flaqai-affiliate-program)

## Why this prompt library exists

A useful prompt says what the image must accomplish, which details can change, and what must survive the next edit. This collection turns everyday creative jobs into concrete briefs with composition, materials, exact copy, constraints, follow-up edits and review criteria.

**97 recipes across 14 packs:** 73 recipes with complete English and Simplified Chinese prompts, 12 English-only workflow recipes, and 12 language-specific briefs. 28 newly generated images include a library cover, six earlier examples, seven launch-inspired input/output pairs and seven customizable-studio outputs. Most recipes are authored templates awaiting rendering; individual entries disclose their status. Translations and follow-up edits are not counted as extra recipes.

The library is for independent brands, online shops, designers, creators, educators and small production teams. Start with a lamp campaign, repair a poster headline, preserve a pet’s distinctive features, or build a consistent illustrated story.

## What changes with Images 2.5?

The official documentation distinguishes **GPT Image 2.5 Flare** for fast everyday generation and **GPT Image 2.5 Sunburst** for workflows where editing precision matters most. Both accept text and image inputs. See the official [Flare model page](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) and [Sunburst model page](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst).

Our practical response is to include an explicit preserve list, an approved-image workflow and a focused revision for every core recipe. These are editorial recommendations, not measured success rates. The [version notes](docs/model-notes.md) separate documented capabilities from untested assumptions.

Explore the [Image 2 vs Images 2.5 comparison](docs/images-2-vs-2-5.md) and [10 practical creative workflows](docs/playbook.md) to choose a starting point.

## Quick start

1. Pick a [recipe](prompts/README.md), then copy either its English or Chinese block. Replace the fictional product, copy and colors with your own brief.
2. For an **edit**, upload the required images in their stated order. For a **generation**, no reference is required unless you add one.
3. Review the result, save the approved image, then apply the included follow-up. In a new conversation, upload that approved version again.

Try this original quick brief:

```text
Create a landscape 3:2 product campaign for a fictional portable lamp.
Use a midnight-blue cylindrical metal base, ivory disc shade and orange pull tab.
Place the lamp on a coral stepped plinth against navy; soft, believable shadows.
Reserve the left side for exact white text: "LIGHT, UNPLUGGED." and "TIDELINE".
Show natural material texture. One lamp, no extra copy or product claims.
```

Next turn, with the approved image attached:

```text
Change only the lamp base to muted jade green. Preserve its shape and metal texture.
Keep the shade, pull tab, typography, background, camera and plinth unchanged.
```

The [full recipe](prompts/01-product.md#p001) and [exact executed prompt](assets/generation/tideline-lamp.txt) offer more detail.

## Prompt library

| Prompt pack | What you can make | Recipes |
| --- | --- | --- |
| [Product photography & e-commerce](prompts/01-product.md) | Lamp ad, cup catalog, skincare still life, grinder cutaway, sneaker detail, gift box | 6 |
| [Ads, social & creator covers](prompts/02-social.md) | Repair flyer, video thumbnail, travel carousel, lunch ad, podcast cover, market campaign | 6 |
| [Portraits, fashion & pets](prompts/03-people-pets.md) | Natural headshot, pet portrait, jacket try-on, lifestyle photo, couple illustration, watercolor keepsake | 6 |
| [Precise image editing](prompts/04-editing.md) | Product recolor, removal, evening relight, text replacement, sketch-guided insertion, cutout | 6 |
| [Infographics & education](prompts/05-information.md) | Rain garden, tasting diagram, demo chart, illustrated map, plant cycle, workshop slide | 6 |
| [Brand identity & UI](prompts/06-brand-ui.md) | Wordmark, wayfinding, mobile app, landing-page concept, packaging family, dashboard | 6 |
| [Comics, characters & games](prompts/07-stories-games.md) | Six-panel story, turnaround, expressions, icons, isometric rooftop, pixel harbor | 6 |
| [Architecture & interiors](prompts/08-spaces.md) | Reading room, apartment refresh, guest room, pop-up store, courtyard, pavilion | 6 |
| [Publishing & illustration](prompts/09-publishing.md) | Book cover, cookbook spread, annual review, editorial metaphor, ink print, zine | 6 |
| [Series & production handoff](prompts/10-production.md) | Seasonal variants, aspect-ratio adaptation, localization, three-image composite, restoration, shot expansion | 6 |
| [Multilingual briefs](prompts/11-multilingual.md) | Script-aware posters in English, Chinese, Japanese, Korean, Spanish, French, German, Portuguese, Arabic, Hindi, Thai and Russian | 12 |
| [Launch-inspired editing examples](prompts/12-launch-examples.md) | Pet costume, child wardrobe, duvet pattern, souvenir text, cube rotation, itinerary revision, candle count | 7 |
| [Customizable studio briefs](prompts/13-customizable-studio.md) | Workshop portrait, pour-over poster, toy packaging, lighthouse miniature, keepsake card, editorial collage | 6 |
| [Sketch-to-story: English workflows](prompts/14-sketch-to-story.md) | Sketch interpretation, dense English layout, portrait revisions, branded apparel, action sheets, MV and narrative boards | 12 |

## Featured examples

| Product campaign | Japanese bakery poster |
| --- | --- |
| ![Original portable lamp product campaign on coral and navy](assets/images/tideline-lamp.png) | ![Japanese and English bakery poster with a croissant and readable headline](assets/images/komorebi-bakery.png) |
| [P001 · Product brief](prompts/01-product.md#p001) | [L003 · Japanese brief](prompts/11-multilingual.md#l003) |

| Wordless story | Architectural concept |
| --- | --- |
| ![Six-panel illustrated story of a robot repairing a paper moon](assets/images/paper-moon-story.png) | ![Original reading-room interior with terracotta seating and steel windows](assets/images/reading-room.png) |
| [P037 · Story brief](prompts/07-stories-games.md#p037) | [P043 · Interior brief](prompts/08-spaces.md#p043) |

These images were generated for this repository using Codex’s built-in image tool. Its underlying model ID was not returned, so they are **not verified Flare or Sunburst benchmarks**. The story has a visible continuity issue in panel three; the room contains extra styling objects. Read the [honest review notes](docs/generation-log.md) before using an example as a production reference.

## New: from a Chinese walkthrough to English workflows

Twelve English recipes, **P074–P085**, cover sketch exploration, layout-guided interiors, character styles, a detailed tea editorial page, precise text edits, portrait continuity, logo and apparel concepts, and 9- or 16-panel storyboards.

Each includes input requirements, a complete English prompt, a customization suggestion, a follow-up and review criteria. These are **unrendered adaptations**, with new fictional copy and scenarios. The [source-to-recipe guide](docs/sketch-to-story.md) distinguishes explicit article prompts from workflows described only in prose.

**[Copy the 12 English workflow prompts →](prompts/14-sketch-to-story.md)**

## New: customize a studio brief

Six new bilingual recipes, **P068–P073**, each include three adjustable details with defaults, alternatives and a preserve list. Use them for editorial portraits, coffee instructions, collectible packaging, handmade miniatures, greeting cards and a studio collage.

| Miniature island | Collectible packaging |
| --- | --- |
| ![Handmade lighthouse island with two ochre boats](assets/images/studio-lighthouse.png) | ![Original pocket tram collectible in clear packaging](assets/images/studio-tram.png) |
| [P071 · Edit one roof color](prompts/13-customizable-studio.md#p071) | [P070 · Customize colors and copy](prompts/13-customizable-studio.md#p070) |

**[Browse the six customizable recipes](prompts/13-customizable-studio.md)** · [See the real roof-color edit and source notes](docs/customizable-studio.md)

## New: seven launch-inspired before-and-after examples

Explore original adaptations of scenarios in [OpenAI’s Images 2.5 launch article](https://openai.com/index/introducing-chatgpt-images-2-5/), with bilingual recipes and 14 newly generated images.

| Before: three candles | After: five candles |
| --- | --- |
| ![Ivory birthday cake with three unlit orange candles](assets/images/launch-cake-input.png) | ![The cake edited to show five unlit orange candles](assets/images/launch-cake-edit.png) |

Try pet styling, a synthetic child’s outfit change, a duvet pattern swap, city-name replacement, cube rotation or a single-column itinerary edit. Each pair includes exact prompts and an honest review. The cube result has a geometry defect; none of these outputs is a verified model benchmark.

**[Browse all seven editing pairs →](docs/launch-examples.md)** · [Copy P061–P067](prompts/12-launch-examples.md)

## One campaign, two targeted edits

| 1 · Original | 2 · Change base color | 3 · Change headline |
| --- | --- | --- |
| ![Original navy lamp with LIGHT, UNPLUGGED headline](assets/images/tideline-lamp.png) | ![Jade lamp with original headline retained](assets/images/tideline-lamp-jade.png) | ![Jade lamp with revised YOUR EVENING, UPGRADED headline](assets/images/tideline-lamp-copy.png) |

The second edit uses the **green output** as its input. The earlier color decision carries forward while the headline changes. Fine texture still drifts, and the stem changes with the base: this is a useful creative sequence, not a promise of pixel-perfect preservation. [Follow the complete case study](docs/editing-case-study.md).

## Get better results with fewer vague instructions

- **Name the deliverable:** a catalog photo, poster, character sheet or architectural concept.
- **Provide exact copy:** quote text; give its location and hierarchy; forbid unrequested additions.
- **Define each reference:** base scene, product, identity, material or rough layout.
- **Lock approved decisions:** list shape, text, placement, identity and lighting that should remain.
- **Edit one variable:** color first, then copy, then crop; inspect between steps.
- **Review at the destination size:** a readable full-size image may fail as a small thumbnail.

Read the [prompting guide](docs/prompting-guide.md) for structured briefs, reference roles and troubleshooting.

## GPT Image 2 API on Flaq.ai

Bring a prompt into an application or creative pipeline with [Flaq.ai’s GPT Image 2 API](https://flaq.ai/models/openai/gpt-image-2/). The platform offers separate text-to-image and image-editing routes, with a playground for exploring inputs and model-specific documentation for integration.

| Your workflow | Flaq.ai entry point | Use with this library |
| --- | --- | --- |
| Generate from a text brief | [GPT Image 2 API](https://flaq.ai/models/openai/gpt-image-2/) | Product scenes, posters, covers and illustrations |
| Edit or combine reference images | [GPT Image 2 Edit API](https://flaq.ai/models/openai/gpt-image-2-edit/) | Product variations, localization and reference-led edits |
| Explore in the browser | [Free GPT Image 2 tool](https://flaq.ai/gpt-image-2/) | Try a creative direction before integration |
| Build an integration | [GPT Image 2 API reference](https://flaq.ai/docs/?page=api/gpt-image-2) | Check authentication, parameters and task results |

Start with an approved brief, test it in the playground, then follow the documented submit-and-poll workflow in your application. Check current pricing and supported parameters on the selected model page. See the [Flaq.ai documentation](https://flaq.ai/docs/) for integration details.

**Model distinction:** these Flaq.ai links introduce **GPT Image 2**. This repository focuses on **ChatGPT Images 2.5**; reusable prompts can be adapted, but outputs and supported parameters need checking for the selected model. For direct OpenAI Images 2.5 examples, use our separate [API guide](docs/api-guide.md).

## Multilingual prompting

**16 README language and regional versions** help readers get started in their preferred language. English remains the default; localized entry pages include a practical prompt, usage guidance and Flaq.ai resources. See the [language coverage table](docs/localization-guide.md#readme-language-coverage) for the exact scope.

The original 73 core recipes have complete English and Simplified Chinese versions. The new [sketch-to-story pack](prompts/14-sketch-to-story.md) adds 12 English-only workflow recipes adapted from a Chinese article. The [multilingual pack](prompts/11-multilingual.md) adds 12 language-specific briefs, including Japanese, Korean, Spanish, French, German, Portuguese, Arabic, Hindi, Thai and Russian alongside English and Chinese.

Separate the language of your instructions from the text printed in the image. Provide approved copy, preserve brand names deliberately, and allow appropriate line wrapping. The [localization guide](docs/localization-guide.md) covers script-aware checks. Localized README pages are entry points; they do not imply that every recipe has been translated into every language.

## Originality and example records

The flaq.ai team composed these briefs and generated the included images for this project. Each example links to its exact prompt, input relationships and review notes in the [generation log](docs/generation-log.md). Templates without a rendered example are explicitly marked.

See the [originality policy](docs/originality.md) for submission standards and provenance. This independent project is not affiliated with or endorsed by OpenAI.

## FAQ

### Are these prompts free to use?

The repository’s original material is offered under the [MIT License](LICENSE). Use your own authorized inputs and review any third-party rights in your final output. Fictional demonstration names are not trademark-clearance guarantees.

### Is this an official OpenAI prompt collection?

No. This is an independent open-source project created and maintained by the **flaq.ai team**, without OpenAI affiliation or endorsement.

### Are all 97 prompts tested on Images 2.5?

No. We publish authored templates alongside a small, explicitly logged set of newly generated examples. The built-in generation tool did not expose its model ID. There are no claimed model comparison scores or universal success rates.

### Which API model name should I use?

Use the documented `gpt-image-2.5-flare` or `gpt-image-2.5-sunburst` identifier, rather than assuming the collection title is an API ID. The [API guide](docs/api-guide.md) contains generation and editing examples.

### Will the image contain perfect text or a usable vector logo?

Text needs proofreading. Generated logo and UI images are raster concepts; vector artwork, interactive interfaces and print-ready typography require a separate production step. Data-critical charts also need numerical validation.

### How do I contribute?

Submit an original use case with a clear brief, constraints, a follow-up and review criteria. An example image must include the exact generation prompt and accurate provenance. Follow [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

Help expand the library with an original practical brief, a language correction or a documented image example. Include the intended use, constraints, a focused follow-up and observable review criteria. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

## About the Flaq.ai team

[Flaq.ai](https://flaq.ai) is a unified API platform for developers building AI agents, creative applications and repeatable production workflows. It brings image, video, music and language models into a shared platform, with a [model market](https://flaq.ai/model-market/) for discovery and [API documentation](https://flaq.ai/docs/) for integration.

For this library, the practical path is simple: choose a creative brief, try a model, inspect the result, then bring the approved workflow into your application. The GPT Image 2 generation and editing links above provide starting points on Flaq.ai; the Images 2.5 guide covers the separate direct OpenAI workflow.

The flaq.ai team creates and maintains this open-source collection so that prompts, examples and lessons from each edit can be reused and improved by the community. Contributions can add a practical use case, correct a translation or document a result with its exact prompt.

- [Explore Flaq.ai](https://flaq.ai)
- [Browse the model market](https://flaq.ai/model-market/)
- [Read the API documentation](https://flaq.ai/docs/)
- [Explore our GPT Image 2 prompt collection](https://github.com/flaqai/awesome-gpt-image-2-prompt)

## Flaq.ai affiliate program

Publish AI tutorials, model reviews, creative workflows or API integration guides? The [Flaq.ai Affiliate Program](https://flaq.ai/affiliate-program/) lets you earn commissions from eligible referrals while helping your audience discover the platform.

| Referral activity | Published commission |
| --- | --- |
| A referred user’s first valid paid order | **20%** |
| Following valid paid orders within 60 days after that user’s registration | **10%** |

Create or sign in to your Flaq.ai account, complete your affiliate profile, and generate a referral link. The affiliate workspace lets you manage links and review referral activity.

Eligibility and payouts follow the current [Affiliate Agreement](https://flaq.ai/affiliate-agreement/). Refunded, charged-back and otherwise ineligible orders do not qualify; disclose your affiliate relationship when promoting referral links. Terms checked on **2026-09-09** and may change.

**[Join the Flaq.ai Affiliate Program →](https://flaq.ai/affiliate-program/)**

## License

[MIT](LICENSE) © 2026 Flaq AI.

[Full index](prompts/README.md) · [Machine-readable prompts](data/prompts.json) · [Changelog](CHANGELOG.md) · [SEO publishing kit](docs/seo.md)
