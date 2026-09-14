# Generation log · 图片生成记录

139 original PNG files, including synthetic inputs, first attempts and refined outputs. All 103 recipes have at least one generated result. Images were generated with the Codex built-in image tool; all editing references are this project’s own generated assets.

Each record preserves the exact executed prompt, input order, dimensions, SHA-256 and visual review. Model ID, seed and quality settings were not exposed and are not inferred. These examples are not verified Flare/Sunburst comparisons.

实际执行提示词与可复用配方可能略有不同。以下记录保留输入关系、原始文件和目测发现；后续修改建议只有出现独立输出记录时才代表已执行。

[Browse results by recipe](gallery.md) · [Machine-readable manifest](../assets/manifest.json)

## cover · Library cover

- Recipe: `COVER` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/cover.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/cover.txt)
- SHA-256: `a1675f613b32c913a91332271cf11df4c4f6d0bc942eea28f97525719aae8774`
- Inputs: None

**Review:** Typography and objects visually reviewed; generated brand treatment is not an official logo file.

## tideline-lamp · Original campaign

- Recipe: `P001` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/tideline-lamp.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/tideline-lamp.txt)
- SHA-256: `6aeb821e89f195162fef5f0cbd32ff6aa6ba3d5cbbdb339ad545631d957edfbb`
- Inputs: None

**Review:** Headline and brand are readable. Material appearance is illustrative; recycled content cannot be verified visually.

## tideline-lamp-jade · Edit 1: base color

- Recipe: `P019` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/tideline-lamp-jade.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/tideline-lamp-jade.txt)
- SHA-256: `2843ef853af6a2639c4aedb33eb9643b3cb7bb25b758cef13caa8ab4a04333e2`
- Inputs: [1](../assets/images/tideline-lamp.png)

**Review:** Base becomes green. Main composition retained. The narrow stem also shifts green, slightly outside the requested cylindrical-base region.

## tideline-lamp-copy · Edit 2: headline

- Recipe: `P019` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/tideline-lamp-copy.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/tideline-lamp-copy.txt)
- SHA-256: `0aea19cb8f40be596e9ceca8ef098917e3f2d358061b2c2e3ab496d27e941832`
- Inputs: [1](../assets/images/tideline-lamp-jade.png)

**Review:** New headline and retained green base visually verified. Fine texture and highlights drift; not a pixel-identical edit.

## komorebi-bakery · Japanese bakery poster

- Recipe: `L003` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/komorebi-bakery.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/komorebi-bakery.txt)
- SHA-256: `e32844e8900fe27c92625e63b1941dde8dcc0f601aebc9e76f8dbca2ed4cd62e`
- Inputs: None

**Review:** Three requested text strings visually match. Portrait is 2:3. Native editorial review remains recommended.

## paper-moon-story · Wordless storyboard

- Recipe: `P037` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/paper-moon-story.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/paper-moon-story.txt)
- SHA-256: `e05d17c13228662d74257847ebd824eed78081a7137de8943d6add0a4b2f00ed`
- Inputs: None

**Review:** Six panels and recognizable robot retained. Panel three shows stitches before the dedicated stitching panel; medium is more dimensional than requested. Teaching example requiring continuity revision.

## reading-room · Reading-room concept

- Recipe: `P043` · Role: result · Date: 2026-09-09
- [Original PNG](../assets/images/reading-room.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/reading-room.txt)
- SHA-256: `050679d6aba9ef04df2fcbe97c237e50643ade6bffbb018482bd8f27ef7620a7`
- Inputs: None

**Review:** Main arrangement and four chairs visible. Added cup/vase and illegible book-spine marks; circulation and construction not validated.

## launch-dog-input · Terrier cape makeover — input

- Recipe: `P061` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-dog-input.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/launch-dog-input.txt)
- SHA-256: `a58f4c8d7151a23ea081b669284e2474e9c8b5a9cd68b6db33baad73335088ac`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. Inspect this input before editing.

## launch-dog-edit · Terrier cape makeover — edit

- Recipe: `P061` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-dog-edit.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/launch-dog-edit.txt)
- SHA-256: `416e047e608211d21a421ee906fb47904d90e6a86545abbd3f2f03e2ec980db5`
- Inputs: [1](../assets/images/launch-dog-input.png)

**Review:** Green cape and tie added; eye patch, ears and paws remain recognizable. Fine fur detail changes.

## launch-child-input · Synthetic child portrait wardrobe edit — input

- Recipe: `P062` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-child-input.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/launch-child-input.txt)
- SHA-256: `c783863a49c5ca2cf65dd65746437dd86a599e5b91997f2c7e8e0d25f1ce241b`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. The child is fully synthetic.

## launch-child-edit · Synthetic child portrait wardrobe edit — edit

- Recipe: `P062` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-child-edit.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/launch-child-edit.txt)
- SHA-256: `8e5b4ef923f98b0560f268a70dd7c19aa3c1611ff3efcd49ffc1ffa03283c84c`
- Inputs: [1](../assets/images/launch-child-input.png)

**Review:** Cardigan and cream shirt appear as requested; face, hands and pose remain visually similar. Fine texture is not identical. Subject is fully synthetic.

## launch-bed-input · Duvet pattern swap — input

- Recipe: `P063` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-bed-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/launch-bed-input.txt)
- SHA-256: `d8a6afb258a81239a3de3eefeb5f3baee73789599bf8b9e385f95a0923875ba5`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. Inspect this input before editing.

## launch-bed-edit · Duvet pattern swap — edit

- Recipe: `P063` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-bed-edit.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/launch-bed-edit.txt)
- SHA-256: `f2e253f57da09c5de0cd3186acc13745472a558dc83dfd1466e8ea1f8d7d4ac4`
- Inputs: [1](../assets/images/launch-bed-input.png)

**Review:** Striped duvet and two oatmeal pillows are present; room arrangement remains similar. Duvet folds drift slightly.

## launch-ticket-input · Souvenir city-name replacement — input

- Recipe: `P064` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-ticket-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/launch-ticket-input.txt)
- SHA-256: `04b59634b3119c0a383e989b67153fb9c074729cbb27cdf81c16bcd0cc9e045e`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. Inspect this input before editing.

## launch-ticket-edit · Souvenir city-name replacement — edit

- Recipe: `P064` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-ticket-edit.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/launch-ticket-edit.txt)
- SHA-256: `b9635545ed47cac69bf8920472877f76adb495b271d4ce89d093421ec1b9bfa4`
- Inputs: [1](../assets/images/launch-ticket-input.png)

**Review:** LISBON and the other required strings visually match. Illustration details drift slightly. This is a fictional souvenir, not a valid ticket.

## launch-cube-input · Symbol-marked cube rotation — input

- Recipe: `P065` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-cube-input.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/launch-cube-input.txt)
- SHA-256: `7b29e4516720b4888cc2de57849b7eca9bbcdd4d482ae99476f28b661e8ab805`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. Inspect this input before editing.

## launch-cube-edit · Symbol-marked cube rotation — edit

- Recipe: `P065` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-cube-edit.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/launch-cube-edit.txt)
- SHA-256: `13f8b4e05e5d7bd7ea729d2f01a07d25e4e407249ed0cd759aabc5f6738f52a2`
- Inputs: [1](../assets/images/launch-cube-input.png)

**Review:** Partial result: face identities follow the intended arrangement, but a rigid 90-degree rotation is not established. The top outline has a visible kink. Do not use as validated geometry.

## launch-travel-input · One-column itinerary revision — input

- Recipe: `P066` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-travel-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/launch-travel-input.txt)
- SHA-256: `aaa761b7c96a972fde34795ffbed0d4969145cf4e1bac70e91d3e3daa15fcd5e`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. Inspect this input before editing.

## launch-travel-edit · One-column itinerary revision — edit

- Recipe: `P066` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-travel-edit.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/launch-travel-edit.txt)
- SHA-256: `8b1f2b6589d2b23b1321edd93ec789cb1056e6f10de010a0e21554c069f9e4a1`
- Inputs: [1](../assets/images/launch-travel-input.png)

**Review:** Middle time and heading match; three bowls appear on the workbench. Extra vessels appear on the shelf. Outer columns remain recognizable but fine illustration details drift.

## launch-cake-input · Birthday candle count edit — input

- Recipe: `P067` · Role: input · Date: 2026-09-09
- [Original PNG](../assets/images/launch-cake-input.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/launch-cake-input.txt)
- SHA-256: `3ccfe58184f73c8ececee50b4bd1f9228f93eaf679de826813b441a8ba5244d2`
- Inputs: None

**Review:** Newly generated fictional input; no official example image was supplied. Inspect this input before editing.

## launch-cake-edit · Birthday candle count edit — edit

- Recipe: `P067` · Role: edit · Date: 2026-09-09
- [Original PNG](../assets/images/launch-cake-edit.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/launch-cake-edit.txt)
- SHA-256: `24d7c809a3ada4a0816001a38ce7a0fe949e1b81fc9d54969f0e267b8327b5e0`
- Inputs: [1](../assets/images/launch-cake-input.png)

**Review:** Exactly five unlit orange candles are visible. Cake, plate and composition are similar; frosting texture changes slightly.

## studio-workshop · Repair collective editorial portrait — original generation

- Recipe: `P068` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-workshop.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/studio-workshop.txt)
- SHA-256: `090fcb276915dbd1bda075e6ce777a6b2f24d83c0078d966444a60de363a4c73`
- Inputs: None

**Review:** Subject, backpack seam and window light match the brief. Extra bowl and cloth appear on the foreground workbench; fingers and needle contact need close production review.

## studio-brew · Four-step pour-over poster — original generation

- Recipe: `P069` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-brew.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/studio-brew.txt)
- SHA-256: `0b6043327aca4771971569614f56deb6de64ca123c6a51019722b9da56b5281c`
- Inputs: None

**Review:** Four ordered columns and all requested labels are present. Kettles extend to panel edges; this is a simplified illustrated sequence, not a complete brewing procedure.

## studio-tram · Pocket tram collectible packaging — original generation

- Recipe: `P070` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-tram.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/studio-tram.txt)
- SHA-256: `d543374b916f4572e40186cb659d04571320c1ac7547fd1a489d76e504a1655f`
- Inputs: None

**Review:** All three text lines match. One tram and one suitcase are visible. Three large side windows plus a narrow end window appear, so strict window count needs refinement.

## studio-lighthouse · Handmade lighthouse island — original generation

- Recipe: `P071` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-lighthouse.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/studio-lighthouse.txt)
- SHA-256: `f2e5e233674e0c1185aa91b2298f93342f734a996b0bfe0363c0da069b27910e`
- Inputs: None

**Review:** Two boats, one lighthouse, one boathouse and the whole cork base are visible. Foliage looks more like model landscaping than clearly identifiable felt.

## studio-card · Knitted keepsake greeting card — original generation

- Recipe: `P072` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-card.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/studio-card.txt)
- SHA-256: `df1dc04cb726a06023e84e1e9c51cec95f09aabc4a0f05575ee863eec284982e`
- Inputs: None

**Review:** Both requested phrases, repaired ear and two button eyes are visible. The title uses a small-cap-like treatment; confirm case styling and print legibility for final artwork.

## studio-collage · Ceramics studio editorial collage — original generation

- Recipe: `P073` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-collage.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/studio-collage.txt)
- SHA-256: `b9a043cb61717e2188cd2f0420c8a376831c36e77e0d1049cb74f0a7f5728673`
- Inputs: None

**Review:** Exactly four bordered prints and both requested text lines are visible. Bowl colors remain related; extra kitchen styling appears in the finished-bowl photo.

## studio-lighthouse-edit · Handmade lighthouse island — roof-color edit

- Recipe: `P071` · Role: result · Date: 2026-09-11
- [Original PNG](../assets/images/studio-lighthouse-edit.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/studio-lighthouse-edit.txt)
- SHA-256: `a0226f310666ce832ba6d5853f92b0559ad5c116cf9749e3827ef8e9a6cac7df`
- Inputs: [1](../assets/images/studio-lighthouse.png)

**Review:** Lighthouse roof and finial changed to sage while the boathouse roof stayed terracotta. Both boats remain. Shrubs, rocks and water texture drift noticeably; preservation is not pixel-identical.

## P086 · Ingredient-built bakery lettering — generated example

- Recipe: `P086` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-p086.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p086.txt)
- SHA-256: `f91ab0d251caec296e2ef1ba2d79cf6dca44a6b419729cb7709d1e81c563c55a`
- Inputs: None

**Review:** The first result merges the W/I region, so the five-letter word is not reliably readable; a targeted correction is recorded separately.

## P087 · Six-frame fragrance launch board — generated example

- Recipe: `P087` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p087.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p087.txt)
- SHA-256: `2de8365c89de146f841ff736afabf6b0edcf6d3d2f295337f091e202db11195d`
- Inputs: None

**Review:** Six numbered panels and NORTH ROOM labels are visible; cap removal and mist sequence read clearly. Product continuity is conceptual, not pixel-exact.

## P088 · Editorial mobility concept poster — generated example

- Recipe: `P088` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p088.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p088.txt)
- SHA-256: `fb4fa4f7df0e6878c04acec70cec3cc6546519f06eac0a56d693db317d4d6371`
- Inputs: None

**Review:** CITY CARRY and DESIGN STUDY are readable; two wheels and a front cargo box are present. Mechanical connections remain concept art, not a buildable bicycle specification.

## P089 · Paper-window weekend destination card — generated example

- Recipe: `P089` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p089.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p089.txt)
- SHA-256: `2c88feb584a0020a7dd6c6499a2c7ebe26126970256d3f66aa0e087bf1c98fbf`
- Inputs: None

**Review:** Both requested text lines, three red cabins and a canoe are visible; layered paper depth reads clearly.

## P090 · Sketch-to-building concept reveal — generated example

- Recipe: `P090` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p090.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p090.txt)
- SHA-256: `ddef52032c2bfcbdf2f653ae46d1d7e1662cfaead7c16115476677f2da87f226`
- Inputs: None

**Review:** Sketch, wireframe and timber facade form one coherent scene. The roof reads as repeated pitched bays rather than a clearly stepped roof; treat it as an exploratory visualization.

## P091 · Community picnic announcement — generated example

- Recipe: `P091` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p091.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p091.txt)
- SHA-256: `87104dae45639f764006ad5b595da4dbfb739f868191b62b95b13464c2578298`
- Inputs: None

**Review:** All three invitation lines are readable and the central mat remains clear; the food and napkin are partly cropped at the edges as a poster treatment.

## P003 · Skincare ingredient still life — generated example

- Recipe: `P003` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p003.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p003.txt)
- SHA-256: `60ccba6af1f4f8f1c946b419886126816ebd87e7a0ff57a23c2030909916d031`
- Inputs: None

**Review:** Amber bottle, linen and two leaves are present; MOSS HOUR and FACE OIL are readable with calm upper space.

## P004 · Mechanical coffee grinder cutaway — generated example

- Recipe: `P004` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p004.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p004.txt)
- SHA-256: `af3b1522de45f8048ff2f12407c83afff1e3a8f6d0c348442b15f224d5a50731`
- Inputs: None

**Review:** Five requested labels and CONCEPT are readable and leaders are separated. The mechanism is a conceptual exploded illustration, not validated engineering.

## P006 · Gift box unboxing flat lay — generated example

- Recipe: `P006` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p006.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p006.txt)
- SHA-256: `37ecfa8ff694441e9260c49199d4643d8553a0343b28021eaba041a5d4824438`
- Inputs: None

**Review:** Four-item overhead arrangement and STILL POST label match the brief; card remains blank.

## P007 · Repair café event poster — generated example

- Recipe: `P007` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p007.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p007.txt)
- SHA-256: `9cc53030c6de022b568c9dde3267eac9694f3caeffba116805a18d8f86926cc5`
- Inputs: None

**Review:** Headline, date, time and venue are readable; repaired mug and tools form a coherent print illustration.

## P008 · Creator thumbnail with one idea — generated example

- Recipe: `P008` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p008.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p008.txt)
- SHA-256: `9e950324cde579f6ad919f441a519007c0b8a58f43029387cfdd26e846949ca2`
- Inputs: None

**Review:** Headline and sanding block are clear with the chair centered. The restored section is subtle rather than a sharply demarcated before/after.

## P009 · Carousel cover for slow travel — generated example

- Recipe: `P009` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p009.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p009.txt)
- SHA-256: `e933479169a648eb76fc1bf43e19d4f3ab70b008b46b1c5fb320dfc5982eda60`
- Inputs: None

**Review:** Headline and slide number are legible; the red train follows a coherent curve through the landscape.

## P010 · Neighborhood lunch special — generated example

- Recipe: `P010` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p010.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p010.txt)
- SHA-256: `debf7c90e70be712df2b99e20f34dd3e405dafa257df391bb09623545fc99001`
- Inputs: None

**Review:** Both copy lines are readable and the bowl ingredients are identifiable. Additional background foliage and cutlery appear, so the result is less minimal than the brief.

## P011 · Podcast editorial cover — generated example

- Recipe: `P011` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p011.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p011.txt)
- SHA-256: `d9e48fef5a881003dfe4465dbf42fece43c3944240e3155d2c6d80dc3974f2b7`
- Inputs: None

**Review:** Paper chair, long shadow and all requested lettering read clearly.

## P012 · Seasonal market campaign — generated example

- Recipe: `P012` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p012.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p012.txt)
- SHA-256: `2d0885edcc4b0ac5a2abc95869c90844e02dd506220c0029e3cc58f13affec91`
- Inputs: None

**Review:** Market miniatures have distinct paper and textile surfaces; the headline and market label are readable.

## P016 · Analog weekend portrait — generated example

- Recipe: `P016` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p016.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p016.txt)
- SHA-256: `042240e15acbb07e0ecff3f91a360d16a0d771886a3d8fdc8fd4def20ed8e504`
- Inputs: None

**Review:** Two adults share a plausible tea-pouring moment with subdued light and grain; hands and cup contact were visually inspected.

## P025 · Three-stage rain garden explainer — generated example

- Recipe: `P025` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p025.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p025.txt)
- SHA-256: `927214767d381d434fed7294cc15488e16dbe993fa0508ffc7e1c801628b5b35`
- Inputs: None

**Review:** Three panels, labels and directional water arrows are readable; classroom concept rather than a site-specific drainage design.

## P026 · Coffee tasting wheel for beginners — generated example

- Recipe: `P026` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p026.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p026.txt)
- SHA-256: `7c54fe7c2a13cda1e0396c2d8c9722ff16d0644d0190a621c58cb61d5573a649`
- Inputs: None

**Review:** Three sectors, four text labels and matching ingredient illustrations are clear; not a comprehensive sensory wheel.

## P027 · Transparent demo-data bar chart — generated example

- Recipe: `P027` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-p027.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p027.txt)
- SHA-256: `101e6faf9a1f2619e32a7f4abdf93500de2c8b9d7fe0ebd5849be4636ece41a6`
- Inputs: None

**Review:** Bar values and approximate 1:1.5:2 heights are visible, but the first result has an unintended transparent/dark background. A correction is recorded separately.

## P028 · Fictional neighborhood walking map — generated example

- Recipe: `P028` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p028.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p028.txt)
- SHA-256: `e9f7c97837b44a3cace335b7436381c65f037156ad203497ab69c98e68b7a4be`
- Inputs: None

**Review:** Station, central park, north library and east cafe are placed coherently; the dotted path is interrupted through the park and should not be used as real navigation.

## P029 · Plant life-cycle classroom card — generated example

- Recipe: `P029` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p029.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p029.txt)
- SHA-256: `4905c959a44a3d0d7b01a8c422476eeeb793e18b21644e061927b53a826885da`
- Inputs: None

**Review:** Four labeled growth stages are recognizable. Direction arrows connect each row but omit the wrap between rows; botanical detail needs educator review.

## P030 · Workshop process slide — generated example

- Recipe: `P030` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p030.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p030.txt)
- SHA-256: `ca9de1b133ce4a522dd279710b9d93ac5f30c6e53180806e0737fcc4e435d864`
- Inputs: None

**Review:** Four equal cards, labeled stages and three connecting arrows form a clear sequence.

## P031 · Independent ceramics wordmark — generated example

- Recipe: `P031` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-p031.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p031.txt)
- SHA-256: `d38c54e89e9cb255d42d61cd9c73e1872d3b264a7ca12eb3c3bb13813fdaadd7`
- Inputs: None

**Review:** Both wordmarks are present but the first image uses an unintended dark/transparent background with glow. A flat opaque-background correction is recorded separately.

## P032 · Museum wayfinding family — generated example

- Recipe: `P032` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p032.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p032.txt)
- SHA-256: `454efd2544a0c05544a25b1bbb6ee65083a7364311b6838e6fa6c659e7be9b8f`
- Inputs: None

**Review:** Three signs, readable labels and correct arrow directions are present; the matching square motif is more decorative than a plain square.

## P033 · Book-club mobile app concept — generated example

- Recipe: `P033` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p033.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p033.txt)
- SHA-256: `a9e1d0872fdaa595067489282096ed3e903235b618f133c9be8d7a148e5e5bc0`
- Inputs: None

**Review:** All requested labels and the primary button are readable; this is a raster UI concept with no implemented interaction.

## P034 · Workshop booking landing page — generated example

- Recipe: `P034` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p034.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p034.txt)
- SHA-256: `ceb4f05fcd4bd1b8f584f1e89c647118d545506d2cb55e63841b1b09ac2064a4`
- Inputs: None

**Review:** Headline, supporting copy, navigation and button are readable; stool looks completed rather than half-built.

## cup-input · Synthetic input: cup-input

- Recipe: `P002` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/cup-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/cup-input.txt)
- SHA-256: `138b517ccf0a67207c5a5d016763dc939b9ebc24d98c04ddd9accd6610758db0`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## shoe-input · Synthetic input: shoe-input

- Recipe: `P005` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/shoe-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/shoe-input.txt)
- SHA-256: `5213b3e26b3ac3251cfdeb40b6f9a7b0ab70d3103141905e1728c4ae2cf85061`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## adult-input · Synthetic input: adult-input

- Recipe: `P013` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/adult-input.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/adult-input.txt)
- SHA-256: `32e10cd8a7ad51376aa7efcbaa62ca17ec0d5486c2a7cec28bf3d9d8a71f1681`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## pet-input · Synthetic input: pet-input

- Recipe: `P014` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/pet-input.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/pet-input.txt)
- SHA-256: `acd786896c9df2cabead372235d86f430c1e88301325c0eb33fa146135f0cad4`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## couple-input · Synthetic input: couple-input

- Recipe: `P017` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/couple-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/couple-input.txt)
- SHA-256: `abebb2264f494ef15ac432f9bcbd0c8a89d3973da468cc7f57c4ea107a2c659f`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## room-input · Synthetic input: room-input

- Recipe: `P020` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/room-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/room-input.txt)
- SHA-256: `28b8a2530e56862bfaf5149eeebd6696ef313e5bbc89340e8c9959c786f2ecc1`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## linen-input · Synthetic input: linen-input

- Recipe: `P058` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/linen-input.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/linen-input.txt)
- SHA-256: `f6ae164b33b2f7cdba7ef2976e5abdac0ed5fc6c23e07938635048e862cd6ec9`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## planter-sketch · Synthetic input: planter-sketch

- Recipe: `P023` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/planter-sketch.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/planter-sketch.txt)
- SHA-256: `589c370b9a6746d687476b312eae89fe7e0a4f2a15a433193b572a6fe43f2d04`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## pavilion-sketch · Synthetic input: pavilion-sketch

- Recipe: `P048` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/pavilion-sketch.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/pavilion-sketch.txt)
- SHA-256: `67fd37325457703655bba5124ec8e54276075618c10e2d07e95926f2251c4c21`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## curve-input · Synthetic input: curve-input

- Recipe: `P074` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/curve-input.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/curve-input.txt)
- SHA-256: `4bf5513235735edc2007cbe89be45a13d82c273db1358a88d5509273b8a6cc2d`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## bedroom-plan · Synthetic input: bedroom-plan

- Recipe: `P075` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/bedroom-plan.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/bedroom-plan.txt)
- SHA-256: `926f806d8582111d20d6f58d1e4620bc26b7d1fd012c6c6c19da38242a2609b0`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## character-input · Synthetic input: character-input

- Recipe: `P076` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/character-input.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/character-input.txt)
- SHA-256: `fd023936db7aba1c807f43461c8769286bc6eb7553eb7dc04cea6c569becb370`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## logo-input · Synthetic input: logo-input

- Recipe: `P081` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/logo-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/logo-input.txt)
- SHA-256: `0eb6a73b055e53fe720e1c1dc14b02a114d661a5dd163e61a33d548109cf4665`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## singer-input · Synthetic input: singer-input

- Recipe: `P084` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/singer-input.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/singer-input.txt)
- SHA-256: `c9bcb0cd329acfcc127bdbe33c9ec9a487fd259d964beb94780b956c3314cd6f`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## person-a-input · Synthetic input: person-a-input

- Recipe: `P085` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/person-a-input.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/person-a-input.txt)
- SHA-256: `ee47f5f3a9f573300d290a1dd63c114fc5fd5ca5421964adf0a832786502afba`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## person-b-input · Synthetic input: person-b-input

- Recipe: `P085` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/person-b-input.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/person-b-input.txt)
- SHA-256: `12b6d17ab18403179f9e78a08e4d177980347970c0ee276312637fed30befb36`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## vintage-input · Synthetic input: vintage-input

- Recipe: `P059` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/vintage-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/vintage-input.txt)
- SHA-256: `7f88ef5a6f8fde9de5d8246e865f8d8fad23ba52891463b5cbaa4d0d752da88b`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## terrace-input · Synthetic input: terrace-input

- Recipe: `P023` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/terrace-input.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/terrace-input.txt)
- SHA-256: `fae072d31ba92cc6d7c48a4162ff3226be0fbd5b92b59d23fae98c2dd9b7262a`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## P035 · Tea packaging family — generated example

- Recipe: `P035` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p035.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p035.txt)
- SHA-256: `c28468385da6a46f373f17eb22880a97b430bc9a65b41f1cc18225bc5bbde66b`
- Inputs: None

**Review:** Three cartons and requested variant names are legible. Extra TEA and SMALL LEAVES BIG CONVERSATIONS copy was generated; remove or approve this before production.

## P036 · Creator dashboard concept — generated example

- Recipe: `P036` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p036.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p036.txt)
- SHA-256: `bf862836f5d3721887f3b390355f8ed6d796af962ceaa339a34c9bff78ae11dd`
- Inputs: None

**Review:** Sidebar, three project cards and review time are readable; spacing is coherent for a dashboard concept.

## P038 · Character turnaround sheet — generated example

- Recipe: `P038` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p038.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p038.txt)
- SHA-256: `f259258b304ba964a91158c0a2c27de955191accd07180d4b7dade5f3c98a214`
- Inputs: None

**Review:** Three equal-scale front, side and back views share a baseline; satchel placement and costume folds should be reconciled before production modeling.

## P039 · Four-expression mascot sheet — generated example

- Recipe: `P039` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-p039.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p039.txt)
- SHA-256: `36755490ae758957f5955dc131100011f8919c31d4d9d654c24613204446fa5b`
- Inputs: None

**Review:** Four distinct expressions are present; first output has unintended transparency and edge artifacts. A cream-background correction is recorded separately.

## P040 · Cozy game inventory icons — generated example

- Recipe: `P040` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-p040.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p040.txt)
- SHA-256: `1c96023bb9198c30dc6b9e2b3da893fd75a2a558a93c5afd49a17d9b3fa52b4a`
- Inputs: None

**Review:** Nine requested icons are present in a 3-by-3 grid; first output has unintended transparency and fringe artifacts. A correction is recorded separately.

## P041 · Isometric rooftop garden — generated example

- Recipe: `P041` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p041.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p041.txt)
- SHA-256: `f66bd37b2a77f4f5b906e528ee5b1a32019f6cd4e4249d243cf0a2e04fcdac1f`
- Inputs: None

**Review:** Greenhouse, three main raised beds and a barrel are present with visible walkway; extra small planters were added.

## P042 · Pixel-art harbor background — generated example

- Recipe: `P042` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p042.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p042.txt)
- SHA-256: `c5abb413404c5b4ab4e25e2d98bfbb3dcb9ca0dbe5064e1eccfc820502154220`
- Inputs: None

**Review:** Harbor layout and dusk palette match the brief; pixel-art appearance is illustrative rather than an enforced fixed pixel grid.

## P045 · Boutique guest-room styling — generated example

- Recipe: `P045` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p045.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p045.txt)
- SHA-256: `8fd323fe9558f1289495b8b56829225bb63343d9c1d8a29301022143457b83e4`
- Inputs: None

**Review:** Doorway view, oak bed and linen are coherent; the reading niche is rendered as a small illuminated wall recess.

## P046 · Pop-up refill store — generated example

- Recipe: `P046` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p046.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p046.txt)
- SHA-256: `33438d0116127a94df16aec34e2b3f0698eeb23c4566e55d8d9c4233d14e0603`
- Inputs: None

**Review:** Three dispensers and REFILL CORNER lettering are clear; the scene includes customers and a venue instead of an abstract empty backdrop.

## P047 · Courtyard planting concept — generated example

- Recipe: `P047` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p047.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p047.txt)
- SHA-256: `9a09ae3a60c00d28469ba30ce706c243c5cf5e63d9f72cef62e56d2440bf3b4c`
- Inputs: None

**Review:** Top-down courtyard has one tree, oval gravel field, straight stepping stones and a bench. Tree canopy obscures the center of the path.

## P049 · Quiet orchard book cover — generated example

- Recipe: `P049` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p049.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p049.txt)
- SHA-256: `92bcbce29b743ccad1bd3c3db39a923daef02d159f2a1eca2f07ec9580710943`
- Inputs: None

**Review:** Title and author are readable; pear tree and oversized shadow follow the concept. Cream-on-peach title contrast is modest.

## P050 · Recipe editorial spread — generated example

- Recipe: `P050` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p050.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p050.txt)
- SHA-256: `0ba6329b86d6baaaacb1e696dd8cc7adf3a9b84df5d7f5679e10b433f08cd4fd`
- Inputs: None

**Review:** Title and three steps are readable; the spread uses realistic book curvature and adds step numbers 1–3.

## P051 · Annual review cover — generated example

- Recipe: `P051` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-p051.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p051.txt)
- SHA-256: `f93f3daf985d95022cd11f7b7c1d7d0259f9446b3b0f41fbee2516ee97a44fb9`
- Inputs: None

**Review:** Requested cover text and paper stack are present, but the first output has unintended transparency/fringes. A correction is recorded separately.

## P052 · Editorial attention metaphor — generated example

- Recipe: `P052` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p052.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p052.txt)
- SHA-256: `54aa6881ff88ce72797adfc61fa0f14390e728d845eb4fa7152fa78aece70e95`
- Inputs: None

**Review:** One orange focal flower and a wall separating the notification field are clear; no readable text is added.

## P053 · Botanical ink print — generated example

- Recipe: `P053` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p053.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p053.txt)
- SHA-256: `9e533b1e1a6ea1f8a8b5fa0b0d37fa9b6cf8036ad7a880c3a1288ef37bf92377`
- Inputs: None

**Review:** Three main reed stems and vermilion sun are visible; the scene expands into a distant landscape beyond the requested small pool.

## P054 · Risograph neighborhood zine — generated example

- Recipe: `P054` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p054.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p054.txt)
- SHA-256: `7ee2beb953943bafe639f1c0a137de7554177b9814a983fc2fc157b287b6423e`
- Inputs: None

**Review:** Title is legible; bicycle, window, plant and awning form a cohesive two-ink-style collage.

## P077 · English tea collection editorial sheet — generated example

- Recipe: `P077` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p077.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/example-p077.txt)
- SHA-256: `f8abac622a9db5ae13e34c6a1c0650b72f36e5bf39d2354142177b116f601d56`
- Inputs: None

**Review:** Dense copy, three tins, three tasting cards and four-column table are readable at inspection size. Botanical drawings use more than a single ink color; copy still needs a final editorial proof.

## L001 · English · Repair workshop flyer — generated example

- Recipe: `L001` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l001.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l001.txt)
- SHA-256: `dc06676d319fd5d02e8a79e6c6aeec49ebeb4fc12c26322fa2abe7118e4a18bd`
- Inputs: None

**Review:** All three English lines are readable; blue repaired mug and orange thread match the initial generation brief.

## L002 · 简体中文 · 城市慢生活海报 — generated example

- Recipe: `L002` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l002.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l002.txt)
- SHA-256: `def3db1d061e868c5c9429e8b1abc912d5428fba716c852bf92732aefd888a0c`
- Inputs: None

**Review:** Three Chinese lines are readable; extra full stops appear after the supporting line and footer, and a blanket/book/cup were added. Review exact punctuation before reuse.

## L004 · 한국어 · 독립 서점 포스터 — generated example

- Recipe: `L004` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l004.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l004.txt)
- SHA-256: `553b690e85c4687ab14c818f9767d8ca4eebec3e98e6e1e7bb61a14ed3fe878f`
- Inputs: None

**Review:** Three Korean lines and navy mug are visible; additional tiny book text and background decor appear. Native-language proofread remains recommended.

## L005 · Español · Cartel de café — generated example

- Recipe: `L005` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l005.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l005.txt)
- SHA-256: `d4c37386044b3272959ca8e637653115ecd466cadbf924d443fabed3aa4b0ff6`
- Inputs: None

**Review:** Headline accent and comma are retained; three Spanish text elements read correctly at inspection size.

## L006 · Français · Affiche de marché — generated example

- Recipe: `L006` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l006.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l006.txt)
- SHA-256: `e1958c16e531d6a264b09481353682653d6ac61fd7675bd4f9e7a880f5d771c0`
- Inputs: None

**Review:** Three pears, blue bag and the three French text strings are visible; accents and punctuation read correctly at inspection size.

## L007 · Deutsch · Werkstattplakat — generated example

- Recipe: `L007` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l007.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l007.txt)
- SHA-256: `8987049789775936cf7692eb1f1e126f55096602f105b4e24594a0c01832d680`
- Inputs: None

**Review:** Long German headline remains intact across two lines; umlauts and supporting copy are visible.

## L008 · Português · Cartaz de padaria — generated example

- Recipe: `L008` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l008.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l008.txt)
- SHA-256: `4e3a9432f8e312b91f2d1d64bd73648f4e1667d366c9af589df8cd739ff2eafd`
- Inputs: None

**Review:** PÃO retains its tilde; all three Portuguese lines are readable and bread/linen textures are coherent.

## L009 · العربية · ملصق مقهى — generated example

- Recipe: `L009` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l009.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l009.txt)
- SHA-256: `8954a5bcdcf3fce372f9eb7a8419c27eccead5c1e544f9f49fa607872f19ea72`
- Inputs: None

**Review:** Three connected right-to-left Arabic text areas are visible with wide spacing; native-language proofreading remains recommended.

## L010 · हिन्दी · पुस्तकालय पोस्टर — generated example

- Recipe: `L010` · Role: draft · Date: 2026-09-14
- [Original PNG](../assets/images/example-l010.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l010.txt)
- SHA-256: `ad9892c8698e75d5b278c119fa17dbffe6a7331a75750a5707d2716e5ac1aefa`
- Inputs: None

**Review:** The three requested Hindi lines are prominent, but extra generated lettering appears on props and the wall. Remove that extra lettering and obtain fluent Hindi review before publication.

## L011 · ไทย · โปสเตอร์ร้านชา — generated example

- Recipe: `L011` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l011.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l011.txt)
- SHA-256: `a38edc319708c30d5df1306d4132506d93f730dd73258253c6244d3855b002b6`
- Inputs: None

**Review:** Three Thai text blocks and a quiet tea composition are present. Fluent Thai proofreading is still required before publication.

## L012 · Русский · Афиша мастерской — generated example

- Recipe: `L012` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l012.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l012.txt)
- SHA-256: `49345797bcdf8a63edfde6b9418e5f38e13ea254e16cdeab6ad824045e8eb295`
- Inputs: None

**Review:** Cyrillic headline, subtitle and footer are clearly separated. Obtain fluent Russian proofreading before publication.

## P002 · Ceramic cup catalog — generated example

- Recipe: `P002` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p002.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p002.txt)
- SHA-256: `c6a36b4405e90fbe24c42bebd175b10de605af83dfd91d4b20ed2d4a80ef7f46`
- Inputs: [1](../assets/images/cup-input.png)

**Review:** The mug is isolated on white with a soft contact shadow. Glaze speckles and proportions vary slightly; this is a generated listing concept, not a pixel-exact cutout.

## P005 · Sneaker texture detail — generated example

- Recipe: `P005` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p005.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p005.txt)
- SHA-256: `d7bdb7bfa6a3cf8f75eb06d3a3a2c857b08e1d411e5a805d2e8594a7926fffc8`
- Inputs: [1](../assets/images/shoe-input.png)

**Review:** Woven upper and sole texture are visible in the close-up. Fine stitch patterns are reconstructed rather than copied pixel for pixel.

## P013 · Natural professional portrait — generated example

- Recipe: `P013` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p013.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p013.txt)
- SHA-256: `d32bd291ba669c3024ce269c89067024e3340b2f2206c8494502c1c926ba9be2`
- Inputs: [1](../assets/images/adult-input.png)

**Review:** Portrait retains the fictional subject’s recognizable features and skin texture. Clothing, framing and lighting change for the portrait brief.

## P014 · Pet explorer portrait — generated example

- Recipe: `P014` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p014.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p014.txt)
- SHA-256: `f77e46a26c31b22623293cecce1dbd8d9874e87204102ddbae323e1c5a908194`
- Inputs: [1](../assets/images/pet-input.png)

**Review:** Terrier, mustard scarf and backpack read clearly. The distinctive eye patch is retained with some fur-pattern variation.

## P017 · Couple illustration keepsake — generated example

- Recipe: `P017` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p017.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p017.txt)
- SHA-256: `8e49a46fff7a8c0d84f8aba5509f5ac0c45e9de231a9a09e12acc12ade233164`
- Inputs: [1](../assets/images/couple-input.png)

**Review:** Two fictional adults remain distinct in the pencil illustration; clothes, bench and riverside setting are coherent.

## P018 · Pet remembrance watercolor — generated example

- Recipe: `P018` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p018.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p018.txt)
- SHA-256: `47f87c24625f962179d6b8e66809085e0c8d0c492913eb477519864e13be3bd8`
- Inputs: [1](../assets/images/pet-input.png)

**Review:** Pet eye patch and pose remain recognizable in watercolor; flower decoration and paper texture are newly interpreted.

## P020 · Remove a tabletop distraction — generated example

- Recipe: `P020` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p020.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p020.txt)
- SHA-256: `0c0e11ee35bbf461502b6d3afcda1c63b59b374bac98d2582a19dda78776053f`
- Inputs: [1](../assets/images/room-input.png)

**Review:** Plastic bottle is removed while mug, runner and room layout remain. Table grain is reconstructed in the removed area.

## P021 · Window-light evening relight — generated example

- Recipe: `P021` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p021.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p021.txt)
- SHA-256: `2c23bb2f5cfc06f046c74500178f4788378de79f1964af72b33a9e3e63ab6422`
- Inputs: [1](../assets/images/room-input.png)

**Review:** Blue-hour exterior and warm desk lamp are coherent. The bottle remains because this edit starts from the original room input, not P020.

## P022 · Poster text replacement — generated example

- Recipe: `P022` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p022.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p022.txt)
- SHA-256: `fca702f2d8eec0f84a64426c3ce6fb415af4ad4e5a8b83295676e41099f1720e`
- Inputs: [1](../assets/images/example-p007.png)

**Review:** New headline A SLOWER SATURDAY is readable; event details and repair objects remain. Minor texture changes occur outside the headline.

## P023 · Sketch-guided planter placement — generated example

- Recipe: `P023` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p023.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p023.txt)
- SHA-256: `ea1b8e6dece8972bef8550dec62e4c8486c65399d2c680a4688c8301116dd492`
- Inputs: [1](../assets/images/terrace-input.png) → [2](../assets/images/planter-sketch.png)

**Review:** Planter is placed against the terrace wall with plausible shadows. Plant spacing and object scale are illustrative, not measured construction guidance.

## P024 · Clean product cutout — generated example

- Recipe: `P024` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p024.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p024.txt)
- SHA-256: `dce3c0a9b863fc0f2974194baf75309066dc65b24b2cf696ded6f44cf7334a92`
- Inputs: [1](../assets/images/cup-input.png)

**Review:** Transparent cutout retains the mug and handle opening. Fine colored fringes remain along parts of the edge; inspect against the intended background.

## P044 · Small apartment material refresh — generated example

- Recipe: `P044` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p044.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p044.txt)
- SHA-256: `0df7c94804c51b8d2d4481074a96c379f3d77d15170ca7db67eb605d7915266e`
- Inputs: [1](../assets/images/room-input.png)

**Review:** Sideboard fronts change to light oak while the room remains recognizable. This is a material visualization rather than an exact finish specification.

## P048 · Sketch to small pavilion — generated example

- Recipe: `P048` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p048.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p048.txt)
- SHA-256: `99d00e43ed527bfbc366d7222c1150a05a1a03589fecf29d188553532074ca96`
- Inputs: [1](../assets/images/pavilion-sketch.png)

**Review:** Sketch becomes a timber pavilion with translucent panels. Structure and proportions are conceptual, not verified engineering.

## P074 · One sketch, four concept directions — generated example

- Recipe: `P074` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p074.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p074.txt)
- SHA-256: `5e16f01a0c19c7d15e1db8f4d267b5dbd74cd9e6ea66262037af15d8b7b4d1c3`
- Inputs: [1](../assets/images/curve-input.png)

**Review:** Four concept panels translate the curved line into a chair, vessel, pavilion and lamp. The common silhouette is approximate, not a geometric trace.

## P075 · Bedroom plan to interior concept — generated example

- Recipe: `P075` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p075.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p075.txt)
- SHA-256: `eb5d2f836eeaa1d012e8a47e997b2d0ce26d22a6980e1cb82e7cbb2aad74b1d9`
- Inputs: [1](../assets/images/bedroom-plan.png)

**Review:** Bed, desk, window and wardrobe follow the plan’s broad arrangement. An extra plan inset is included; dimensions and clearances are not certified.

## P076 · Doodle character across four media — generated example

- Recipe: `P076` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p076.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p076.txt)
- SHA-256: `12a588d986e9889f5010627471944cdca4d84dc28b8d56408d6a99eb854a2cd1`
- Inputs: [1](../assets/images/character-input.png)

**Review:** Four material/style variants retain coat, satchel and boots. The input has four visible buttons, and this variation propagates into the sheet.

## P079 · Four-region portrait correction brief — generated example

- Recipe: `P079` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p079.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p079.txt)
- SHA-256: `a884e23806e6a833b4100b4498488a9501f7bce6a9ee8c0e2dd34771068a3bab`
- Inputs: [1](../assets/images/adult-input.png)

**Review:** Earrings removed, eyes made hazel, strand moved off the eye and brown satchel added. Shirt folds/buttons and hand position also shift slightly, so preservation is not pixel-exact.

## P081 · Logo redesign with an explicit brand brief — generated example

- Recipe: `P081` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p081.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p081.txt)
- SHA-256: `f69631053463d7c59dfdd517ef87eb0d155fc8f16d80f160da7ed65cc6eb9171`
- Inputs: [1](../assets/images/logo-input.png)

**Review:** Readable navy NORTH SIGNAL wordmark and lilac circle on white. The result largely retains the input geometry instead of exploring a substantially different symbol.

## P083 · Sixteen-pose action reference sheet — generated example

- Recipe: `P083` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p083.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p083.txt)
- SHA-256: `18059bd49211ae6df01a7ce90b8dea1a411e92385bf3761d35c6172dde74e17f`
- Inputs: [1](../assets/images/character-input.png)

**Review:** Sixteen action poses appear in a 4×4 transparent sheet. Baselines and character size need alignment before animation; edge fringes remain.

## P084 · Nine-shot music-video concept board — generated example

- Recipe: `P084` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p084.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p084.txt)
- SHA-256: `ac5a06d7bbde6d4d1ad103ee8f12f86a028200cea3535b1ad35c1d193111e869`
- Inputs: [1](../assets/images/singer-input.png)

**Review:** Nine cinematic shots maintain the fictional performer’s outfit and notebook. Eye close-up and notebook handling require continuity review before production.

## jacket-input · Synthetic input: jacket-input

- Recipe: `P015` · Role: input · Date: 2026-09-14
- [Original PNG](../assets/images/jacket-input.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/jacket-input.txt)
- SHA-256: `a42a75027aa2f8f2b0c725588f837fd47f87f1912b1d70c891e4c62540bd9c7f`
- Inputs: None

**Review:** Original synthetic reference, visually inspected before use. It is demonstration input rather than an output of the linked recipe.

## P055 · Seasonal product series — generated example

- Recipe: `P055` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p055.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p055.txt)
- SHA-256: `7104bfff42e9ac2b43c47fdcdfa8b6429bc076f14a0fd2f3c87307478d3cb4ee`
- Inputs: [1](../assets/images/tideline-lamp.png)

**Review:** Autumn leaves and knitted fabric support the campaign; headline and lamp stay recognizable. Composition is rearranged for the new square frame.

## P056 · Portrait ad reframe — generated example

- Recipe: `P056` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p056.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p056.txt)
- SHA-256: `c25394647faf8b35142822d41ba512b779fc163fe096ba557e571001cd72d07a`
- Inputs: [1](../assets/images/tideline-lamp.png)

**Review:** Portrait campaign layout has clear copy and breathing room. Lamp and plinth proportions shift slightly in the reformatted composition.

## P057 · Localized campaign master — generated example

- Recipe: `P057` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p057.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p057.txt)
- SHA-256: `6c01a08f8df37ab6e02ddfc59ccae32e6394981926370efd2c939379d49f7bab`
- Inputs: [1](../assets/images/tideline-lamp.png)

**Review:** Chinese headline 把夜晚留给自己 is readable and TIDELINE remains. Minor product texture and framing changes accompany the text edit.

## P058 · Three-reference product composite — generated example

- Recipe: `P058` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p058.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p058.txt)
- SHA-256: `648a4ab05c4dcf08bad5778db96773967a38967ced58e1aeb107eb234d375f48`
- Inputs: [1](../assets/images/room-input.png) → [2](../assets/images/tideline-lamp.png) → [3](../assets/images/linen-input.png)

**Review:** Lamp and striped linen are combined with the room reference. Sideboard accessories move to accommodate the lamp, so preservation is not pixel exact.

## P059 · Vintage-photo gentle restoration — generated example

- Recipe: `P059` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p059.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p059.txt)
- SHA-256: `4ff95272d67d720a42dc0a49fdba9938c6727074cfaa377ec0bba6b2a02a0d17`
- Inputs: [1](../assets/images/vintage-input.png)

**Review:** Major scratches are repaired and monochrome grain remains. Facial and foliage details are inferred; this synthetic exercise is not historical evidence.

## P060 · Approved storyboard shot expansion — generated example

- Recipe: `P060` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p060.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p060.txt)
- SHA-256: `643e90cc8f1bbf64605240345713948828081dc946b8cb13192825b6ecf3fa63`
- Inputs: [1](../assets/images/paper-moon-story.png)

**Review:** A coherent follow-on scene shows the robot, sleeping cat and repaired glowing moon. Scene geometry is reinterpreted across the story.

## P078 · Headline replacement without layout drift — generated example

- Recipe: `P078` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p078.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/example-p078.txt)
- SHA-256: `7fb899c01e6c40d74a38e7c34d8cf5b9b5643aa265287352034ad66d86ac83da`
- Inputs: [1](../assets/images/example-p077.png)

**Review:** The requested shorter headline is readable while the tea comparison content remains. Small typography and illustration details shift across the edit.

## P080 · Portrait continuity through three revisions — generated example

- Recipe: `P080` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p080.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-p080.txt)
- SHA-256: `0a19f200c65e97e00317e69c1e7b25aaa4ecbba9aadaa841b9f709648dece9e6`
- Inputs: [1](../assets/images/example-p079.png)

**Review:** The brown leather bag carries over and the person remains recognizable. Small shirt and pose details vary; compare with the linked prior result.

## P082 · Reference-led branded apparel presentation — generated example

- Recipe: `P082` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p082.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/example-p082.txt)
- SHA-256: `8be9a091b6f950809cac4ffa952496556682cbe2a4409e3b23b1377a82f94590`
- Inputs: [1](../assets/images/adult-input.png) → [2](../assets/images/example-p081.png)

**Review:** Five panels show model, two shirt colors, print close-up and packaging. NORTH SIGNAL is readable; logo size and proportions vary across surfaces.

## P085 · Sixteen-shot two-character narrative board — generated example

- Recipe: `P085` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p085.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p085.txt)
- SHA-256: `83c490caf9707f619a6cf753420375689442fd6e690f8aa3c6dead9b6162e806`
- Inputs: [1](../assets/images/person-a-input.png) → [2](../assets/images/person-b-input.png)

**Review:** Sixteen library shots distinguish both adults and two notebooks. Book ownership changes across shots; review the intended swap and return sequence.

## P086-v2 · Ingredient-built bakery lettering — refined result

- Recipe: `P086` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p086-v2.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p086-v2.txt)
- SHA-256: `0ca5fbeec0622e4686c79449b49c7fd79dfdf08c6c4703dde064262c0a3f6c9e`
- Inputs: [1](../assets/images/example-p086.png)

**Review:** The follow-up separates all five letters in TWIST and retains SATURDAY BAKES. Bread shapes and tray details are slightly reinterpreted.

## P027-v2 · Transparent demo-data bar chart — refined result

- Recipe: `P027` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p027-v2.png) · 1672 × 941
- [Exact executed prompt](../assets/generation/example-p027-v2.txt)
- SHA-256: `d1f3007e6f381baee599df76cbd74f648cbf2e028d04ec6898a613368276efc0`
- Inputs: [1](../assets/images/example-p027.png)

**Review:** Cream background and readable labels are restored. Bars visually approximate the 20:30:40 relationship; use a charting tool for exact quantitative publication.

## P031-v2 · Independent ceramics wordmark — refined result

- Recipe: `P031` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p031-v2.png) · 1536 × 1024
- [Exact executed prompt](../assets/generation/example-p031-v2.txt)
- SHA-256: `2ff842d0b360c2c7f4e5f8122178c89a62cc25f0a06d715a2901a4d20bd6e0d1`
- Inputs: [1](../assets/images/example-p031.png)

**Review:** Black wordmark and cream reverse lettering on clay are readable on an opaque light background. This is raster concept artwork, not a vector logo.

## P039-v2 · Four-expression mascot sheet — refined result

- Recipe: `P039` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p039-v2.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p039-v2.txt)
- SHA-256: `4760617b0814dce31b8f9ca6abc36334ca5fafcf5f1b031d195e1ffcb08cdaca`
- Inputs: [1](../assets/images/example-p039.png)

**Review:** Four distinct expressions are visible on cream without the previous transparent background. Leaf placement and pebble texture remain coherent.

## P040-v2 · Cozy game inventory icons — refined result

- Recipe: `P040` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p040-v2.png) · 1254 × 1254
- [Exact executed prompt](../assets/generation/example-p040-v2.txt)
- SHA-256: `a9b7eaeabc7c346a7c0ee1db1adaba480f4db72aee800c144695db243175e877`
- Inputs: [1](../assets/images/example-p040.png)

**Review:** Nine distinct game objects are visible on cream without the previous transparent background. This is a concept sheet requiring slicing for production.

## P051-v2 · Annual review cover — refined result

- Recipe: `P051` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p051-v2.png) · 1122 × 1402
- [Exact executed prompt](../assets/generation/example-p051-v2.txt)
- SHA-256: `b6b2270f6d3fc2f0cfb45768c06aab3e18bf499b77cf9d90d33d6063df31e002`
- Inputs: [1](../assets/images/example-p051.png)

**Review:** Title and 2026 REVIEW are legible on cream. Five translucent paper shapes remain an illustrative composition, not a data visualization.

## P015 · Linen jacket virtual styling — generated example

- Recipe: `P015` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-p015.png) · 1086 × 1448
- [Exact executed prompt](../assets/generation/example-p015.txt)
- SHA-256: `c692e1ecc5e9792df582a565d1bbc6f0e8256a0633988dafb878e1828cb426fe`
- Inputs: [1](../assets/images/adult-input.png) → [2](../assets/images/jacket-input.png)

**Review:** Sage linen jacket, three buttons and pockets are recognizable. Sleeves are rolled rather than matching the full-length garment reference; shirt folds and hand details also vary.

## L010-v2 · हिन्दी · पुस्तकालय पोस्टर — refined result

- Recipe: `L010` · Role: result · Date: 2026-09-14
- [Original PNG](../assets/images/example-l010-v2.png) · 1024 × 1536
- [Exact executed prompt](../assets/generation/example-l010-v2.txt)
- SHA-256: `b0593a05b068f07e07616a78f38a50f2220ad98cdf9771f72a50eb5c9ac39017`
- Inputs: [1](../assets/images/example-l010.png)

**Review:** Extra lettering on wall, mug and closed book spines is removed. Main Hindi text remains prominent; fine simulated print persists on the open book. Fluent Hindi proofreading is required.
