# พรอมป์ต์สำหรับ ChatGPT Images 2.5 — flaq.ai

โครงการโอเพนซอร์สอิสระที่จัดทำและดูแลโดยทีม [flaq.ai](https://flaq.ai) สำหรับภาพสินค้า การแก้ไขเฉพาะจุด ภาพบุคคล โฆษณา อินโฟกราฟิก และสตอรีบอร์ด

[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português (Brasil)](README_pt.md) · [Italiano](README_it.md) · [Русский](README_ru.md) · [العربية](README_ar.md) · [हिन्दी](README_hi.md) · **ไทย** · [Bahasa Indonesia](README_id.md) · [Tiếng Việt](README_vi.md)

![flaq.ai — ChatGPT Images 2.5](assets/images/cover.png)

มีพรอมป์ต์ 103 ชุดใน 15 หมวด และภาพที่สร้างขึ้นใหม่ 139 ภาพ โดย 73 ชุดหลักมีทั้งภาษาอังกฤษและจีนตัวย่อ อีก 12 ชุดเขียนสำหรับแต่ละภาษา README มี 16 ฉบับตามภาษาและภูมิภาค หน้านี้เป็นบทนำภาษาไทย ไม่ใช่คำแปลพรอมป์ต์ทั้งหมด นอกจากนี้ยังมีพรอมป์ต์เวิร์กโฟลว์ใหม่อีก 18 ชุดที่เป็นภาษาอังกฤษเท่านั้น


**[แกลเลอรีภาพสำหรับพรอมป์ต์ทั้ง 103 ชุด](docs/gallery.md)**

## เริ่มต้นใช้งาน

เลือกพรอมป์ต์จาก[สารบัญ](prompts/README.md) หากต้องการแก้ไขภาพ ให้แนบภาพอ้างอิงตามที่ระบุ แยกสิ่งที่ต้องเปลี่ยนออกจากสิ่งที่ต้องคงไว้ ตรวจผลลัพธ์แล้วใช้ภาพที่ผ่านการตรวจเป็นข้อมูลสำหรับการแก้ไขครั้งถัดไป

## ลองใช้พรอมป์ต์ภาษาไทย

[↗ L011](prompts/11-multilingual.md#l011)

```text
สร้างโปสเตอร์แนวตั้งอัตราส่วน 2:3 สำหรับร้านชาสมมติ ใช้พื้นหลังกระดาษสีครีม วางถ้วยเซรามิกสีน้ำเงินกับใบชาสองใบในครึ่งล่าง ให้แสงเช้าที่นุ่มนวลแสดงผิวสัมผัสของถ้วยอย่างเป็นธรรมชาติ ด้านบนเขียนตรงตามนี้ว่า “พักสักนิด” ใต้หัวเรื่องเขียน “จิบชาอย่างช้า ๆ” และด้านล่างเขียน “ร้านชาเล็ก ๆ” ใช้ตัวอักษรไทยที่อ่านง่าย เว้นระยะบรรทัดให้สระและวรรณยุกต์ไม่ชนกัน ไม่เพิ่มราคา ที่อยู่ หรือข้อความอื่น ในการแก้ไขครั้งถัดไป เปลี่ยนเฉพาะสีถ้วยเป็นสีเขียวมะกอก โดยคงข้อความและแสงเดิมไว้
```

ตรวจสระ วรรณยุกต์ ช่องว่าง และเครื่องหมาย ๆ กับผู้อ่านภาษาไทยที่คล่องแคล่ว

## เครื่องมือ AI GPT Image 2.5 ฟรี ไม่ต้องสมัครสมาชิก

เครื่องมือ 12 รายการสำหรับลองพรอมป์ต์ด้วยข้อความหรือภาพอ้างอิงหนึ่งภาพ

| เครื่องมือ | คำแนะนำ | พรอมป์ต์ที่เกี่ยวข้อง |
| --- | --- | --- |
| [Flaq.ai free gpt image 2.5](https://flaq.ai/free-chatgpt-images-2-5/) | เหมาะกับภาพสินค้า โปสเตอร์ และฉากสมจริง พร้อมลิงก์ไปยังเครื่องมือสร้างสรรค์และ API ของ Flaq.ai | [P001](prompts/01-product.md#p001) |
| [UGC Maker free gpt image 2.5](https://ugcmaker.org/free-chatgpt-images-2-5/) | เหมาะกับแนวคิดโฆษณา UGC เรื่องราวสินค้า และภาพสำหรับโซเชียลมีเดีย | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/02-social.md) |
| [Best Image AI free gpt image 2.5](https://bestimage.ai/free-chatgpt-images-2-5/) | เหมาะกับอีคอมเมิร์ซ โปสเตอร์ และแนวคิดภาพในรูปแบบจัตุรัส แนวตั้ง หรือแนวนอน | [P070](prompts/13-customizable-studio.md#p070) |
| [HeyDream free gpt image 2.5](https://heydream.im/free-chatgpt-images-2-5/) | เหมาะกับฉากสมจริง การเปลี่ยนสไตล์ภาพถ่าย และพื้นหลัง มีลิงก์เครื่องมือแปลงภาพเป็นวิดีโอแยกต่างหาก | [P071](prompts/13-customizable-studio.md#p071) |
| [AITryOn free gpt image 2.5](https://aitryon.art/free-chatgpt-images-2-5/) | เหมาะกับแนวคิดเสื้อผ้า ภาพแฟชั่น เครื่องประดับ และสินค้า ควรระบุวัสดุ ท่าทาง และพื้นหลัง | [P079](prompts/14-sketch-to-story.md#p079) |
| [Flyne AI free gpt image 2.5](https://flyne.ai/free-gpt-image-2-5/) | เหมาะกับภาพเปิดตัวสินค้า กราฟิกโซเชียล สตอรีบอร์ด และมู้ดบอร์ด หน้าเว็บระบุอัตราส่วนภาพเก้าแบบ | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/01-product.md) |
| [VideoWeb AI free gpt image 2.5](https://videoweb.ai/free-gpt-image-2-5/) | เหมาะกับฉากเปิดภาพยนตร์ ภาพอ้างอิงการเปลี่ยนฉาก แคมเปญ และสถานที่ ควรระบุมุมกล้องและแสง | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/07-stories-games.md) |
| [Sea Imagine AI free gpt image 2.5](https://seaimagine.com/free-gpt-image-2-5/) | เหมาะกับองค์ประกอบศิลป์ พื้นที่สถาปัตยกรรม เลย์เอาต์โปสเตอร์ และการทดลองชุดสี | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/08-spaces.md) |
| [Fylia AI free gpt image 2.5](https://fylia.ai/free-gpt-image-2-5/) | เหมาะกับภาพบุคคลแบบวาด โลกนิทานขนาดจิ๋ว ฉากชีวิตประจำวัน และงานศิลปะกระดาษ | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/03-people-pets.md) |
| [SeeVido AI free gpt image 2.5](https://seevido.com/free-gpt-image-2-5/) | เหมาะกับฉากตัวละคร ภาพเรียกน้ำย่อยสินค้า ภาพประกอบการเดินทาง และโพสต์ตามฤดูกาล | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/02-social.md) |
| [VO4 AI free gpt image 2.5](https://vo4.org/free-gpt-image-2-5/) | เหมาะกับฉากแบบภาพยนตร์ ภาพอ้างอิงท่าทาง โลกไซไฟ และการศึกษามุมกล้อง | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/14-sketch-to-story.md) |
| [Chat 4O AI free gpt image 2.5](https://chat4o.ai/free-gpt-image-2-5/) | เหมาะกับภาพพรีเซนเทชัน ภาพการเรียนรู้ มู้ดบอร์ด และภาพเล่าเรื่อง ควรเว้นพื้นที่สำหรับข้อความ | [พรอมป์ต์ที่เกี่ยวข้อง](prompts/05-information.md) |

คัดลอกพรอมป์ต์และเปลี่ยนรายละเอียดสมมติ หากแก้ไขภาพ ให้แนบภาพอ้างอิงและระบุสิ่งที่ต้องคงไว้ หน้าเว็บระบุว่าใช้ฟรีโดยไม่ต้องสมัคร แต่เครื่องมือที่เพิ่มใหม่ต้องผ่านการยืนยันก่อนสร้างภาพ ตรวจสอบคำอธิบายวันที่ 14 และ 16 กันยายน 2026 โดยไม่ได้ทดลองสร้างภาพ ฟีเจอร์ขั้นสูง วิดีโอ และ API อาจมีค่าใช้จ่ายตามเงื่อนไขแต่ละเว็บไซต์

## สถานะของตัวอย่าง

พรอมป์ต์ด้านล่างยังไม่มีภาพผลลัพธ์ ภาพในโครงการสร้างด้วยเครื่องมือใน Codex ซึ่งไม่ได้ระบุรหัสโมเดล จึงไม่ใช่ผลเปรียบเทียบ Flare กับ Sunburst ที่ยืนยันแล้ว ก่อนเผยแพร่ให้ตรวจข้อความ จำนวนวัตถุ และรูปทรง

## เกี่ยวกับ flaq.ai

[flaq.ai](https://flaq.ai) ให้บริการ API รวมสำหรับโมเดลภาพ วิดีโอ ดนตรี และภาษา เพื่อผู้พัฒนาเอเจนต์ AI และแอปพลิเคชัน ทีมงานเผยแพร่คลังนี้เพื่อแบ่งปันพรอมป์ต์ที่นำกลับมาใช้ได้ พร้อมบันทึกการตรวจผลลัพธ์

ลิงก์ Flaq.ai ด้านล่างใช้กับ GPT Image 2 หากต้องการใช้ Images 2.5 ผ่าน OpenAI โดยตรง โปรดดู[คู่มือ API](docs/api-guide.md)

[GPT Image 2 API](https://flaq.ai/models/openai/gpt-image-2/) · [GPT Image 2 Edit API](https://flaq.ai/models/openai/gpt-image-2-edit/) · [API docs](https://flaq.ai/docs/) · [Model market](https://flaq.ai/model-market/) · [Affiliate program](https://flaq.ai/affiliate-program/)

## คู่มือและการมีส่วนร่วม

[103 prompts](prompts/README.md) · [Before / after](docs/launch-examples.md) · [Generation log](docs/generation-log.md) · [OpenAI API guide](docs/api-guide.md) · [Contributing](CONTRIBUTING.md)

โครงการนี้ไม่มีความเกี่ยวข้องกับ OpenAI และไม่ได้รับการรับรองจาก OpenAI [MIT License](LICENSE) © 2026 Flaq AI.

[X community: 6 English prompts, original posts and source image previews](prompts/15-x-community.md)
