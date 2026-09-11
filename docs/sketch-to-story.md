# From sketch to storyboard: English prompt workflows

Twelve English workflow recipes, P074–P085, adapted and expanded by the [flaq.ai](https://flaq.ai) team from a Chinese practical article. All twelve are **unrendered templates** in this release. They do not add images to the generation log or establish model performance.

## Source and adaptation method

Source: [太上头了！从随手涂鸦到电影分镜，我把 GPT Images 2.5 测了一圈](https://mp.weixin.qq.com/s/mk3gp9wzmq93zV5EtD9rLQ), by 羊羊 / 羊羊AI视频, displayed publication date September 10, 2026. Read from the article page on September 11, 2026.

The article explores sketch interpretation, dense Chinese typography, region comments, successive portrait revisions, brand applications and storyboards. Some instructions appear as explicit text prompts; other workflows are described in prose or illustrated. The table below preserves that distinction. Our English recipes add concrete reference roles, constraints and review steps; they are adaptations, not verbatim translations of every article prompt.

The supplied English tea copy, fictional brands, alternative media and library sketchbook story are new editorial choices. We did not copy the article's photographs, character drawings, logos, generated results or videos. In-image wording has been localized into English, rather than merely translating the instructions around Chinese text.

## Article-to-recipe map

| Article workflow | Available source detail | English recipe | Main addition |
| --- | --- | --- | --- |
| Four interpretations of a curve | Explicit short prompt and narrative | [P074](../prompts/14-sketch-to-story.md#p074) | Four new object categories; shared curve anchors |
| Bedroom sketch to room concept | Narrative description | [P075](../prompts/14-sketch-to-story.md#p075) | Fixed openings, furniture footprints and a restricted add list |
| Doodle in four visual styles | Narrative description | [P076](../prompts/14-sketch-to-story.md#p076) | Five identity anchors across four new media |
| Dense tea-gift editorial page | Detailed text prompt | [P077](../prompts/14-sketch-to-story.md#p077) | New English copy, products and comparison data |
| Replace a page headline | Explicit edit instruction | [P078](../prompts/14-sketch-to-story.md#p078) | Defined old/new strings and handling for text that does not fit |
| Four portrait-region edits | Four explicit instructions | [P079](../prompts/14-sketch-to-story.md#p079) | Unbranded bag, identity constraints and independent checks |
| Continue editing the portrait | Narrative sequence | [P080](../prompts/14-sketch-to-story.md#p080) | Three separate approval stages and a preserve list |
| Logo redesign via a template | Narrative description | [P081](../prompts/14-sketch-to-story.md#p081) | Fictional brand brief and raster-output limits |
| Logo and person to apparel display | Narrative description | [P082](../prompts/14-sketch-to-story.md#p082) | Reference ordering and a defined merchandise layout |
| Sixteen cartoon action poses | Narrative description | [P083](../prompts/14-sketch-to-story.md#p083) | Explicit pose order, cell boundaries and alpha review |
| Nine-shot music-video board | Narrative description | [P084](../prompts/14-sketch-to-story.md#p084) | New conservatory location and notebook continuity |
| Sixteen-shot live-action story | Narrative description | [P085](../prompts/14-sketch-to-story.md#p085) | New library story, prop ownership and screen direction |

## Choose a practical route

### Explore a rough idea

Start with P074 when the drawing describes a shape but not a finished object. Use P075 when the sketch already specifies layout; creative interpretation should then respect the layout. Use P076 when a recognizable character is the most important constraint. After comparing alternatives, render the selected direction individually.

### Build and revise an editorial product page

P077 supplies all English copy in one brief, including matching product names across packaging, cards and a table. First check the three products and text hierarchy. Then inspect each string and table cell at the intended publishing size. Only after approving that page should P078 replace its headline. Keep final copy in a separate text document so a small generated typo is easy to detect.

The English tea example is fictional and substitutes a product-comparison table for brewing parameters. For a real product, provide approved descriptions, weights and instructions; do not ask the model to invent product facts.

### Correct a portrait, then iterate

P079 describes four bounded edits that can be assigned to visible image regions. Review each change and the surrounding face independently. P080 then demonstrates a staged workflow: hairstyle, color grade, background weather. Feed each approved output into the next revision. If identity drifts, return to the last acceptable image and narrow the request.

Image comments are a placement aid in the article's ChatGPT workflow. Where that interface is unavailable, attach the image and describe the region explicitly. Comment text is not an API parameter. These recipes do not require access to the author's account, images or characters.

### Carry a brand into merchandise

P081 starts with audience, desired impression, palette and usage sizes. Once a logo is approved, use it as an explicit reference in P082 alongside an authorized model image. Inspect every repeated logo and garment panel before publishing. If exact logo pixels are essential, apply the approved artwork in a design tool after generating the mockup.

### Prepare assets for motion work

P083 is an action-reference sheet; P084 and P085 are shot-planning boards. A sixteen-pose grid is not automatically a smooth animation, and a storyboard does not guarantee that a video tool will reproduce every panel.

1. Confirm cell count, character identity and scene order.
2. Regenerate weak panels individually using the character and approved board as references.
3. Export separate frames; verify actual transparency for sprite-like assets.
4. Prepare a shot list with action, camera, duration and continuity notes.
5. Supply selected keyframes and references to the chosen video workflow, then review motion separately.

Example handoff specification for the new library story:

| Shot | Intended action | Continuity to preserve | Review |
| --- | --- | --- | --- |
| 1 | Establish the shared table | Window position; A left, B right | Both characters readable |
| 8 | Reveal the architectural sketch | Ochre book remains in B's hands | No invented readable handwriting |
| 12 | Exchange the books | Ochre returns to A; slate returns to B | Hands and ownership stay clear |
| 16 | Both draw quietly | Correct books; same wardrobe and light | Ending matches the earlier geography |

Durations, camera moves and audio are production decisions to add after the board is reviewed. No video was generated for this release.

## What the article's examples do and do not establish

The author reports a clearer tea-layout result from Images 2.5 in one comparison, while noting different output dimensions. The portrait discussion also acknowledges changes in facial appearance and fine details. We preserve those limits: the article is a workflow reference, not a controlled benchmark or a guarantee that untouched pixels remain identical.

Our existing generated examples have separate [provenance and review records](generation-log.md). This English pack adds no measured success rates, model-routing claims or copied comparison images.

[Copy the English recipes](../prompts/14-sketch-to-story.md) · [Prompt index](../prompts/README.md) · [Customization guide](customizable-studio.md)
