---
title: Print & assemble - BLV mgn12 mod
description: BLV mgn12 mod - which parts to print from this project and from the AM8, material, infill, orientation, assembly steps, extras and rail tips.
---

# Print & assemble

## What to print

**From this [BLV mgn12 mod](https://www.thingiverse.com/thing:2567757) project** - print everything except these optional parts:

- **Y motor mount** - only if you don't have the AM8 Y motor mount
- **Top Z holders** (anti Z-wobble) - they may limit the Z height and aren't really needed
- **Caliper holder** - only if you have a digital metal caliper
- **LCD case and brackets** - only with a RepRap Discount LCD 12864; otherwise use the original AM8 LCD case and brackets

**From the [AM8](https://www.thingiverse.com/thing:2263216):**

| Qty | Part | Note |
| ---: | --- | --- |
| 1 | 1_LCD_Base_Left | only with the original Anet A8 LCD |
| 1 | 1_LCD_Base_Right | only with the original Anet A8 LCD |
| 1 | 1_LCD_Case_Top | only with the original Anet A8 LCD |
| 1 | 1_PSU_Mount | for the original Anet PSU |
| 1 | 1_Wire_Holder | |
| 2 | 2_Bottom_Tee_Plate | |
| 2 | 2_Top_Corner_Plate | |
| 4 | 4_Bottom_Corner_Plate | |
| 1 | Anet_Board_Mount__With_Fan **or** Anet_Board_Mount_No_Fan | skip if you use the electronics box |

### Material and infill

The PDF **BLV mgn12 mod.pdf** in the project ZIP has the full spec of every part: name, material and infill percentage.

### Orientation

Highly important: print orientation contributes to the strength of the parts. The 4 pictures show how to orient each part.

!!! warning
    Make sure your printer is calibrated before printing - dimensional precision is crucial.

<div class="gallery" markdown>
![Printing orientation](../assets/img/img-1ec2fa2c.jpg)
![Printing orientation](../assets/img/img-ea10f166.jpg)
</div>

## Assembly

1. **Frame** - assemble the frame extrusions according to Pheneeny's [AM8 mod files](https://www.thingiverse.com/thing:2263216), which also include his perfect assembly guide.
2. **BLV mgn12 mod** - follow the assembly instructions in the project ZIP: **BLV mgn12 mod.pdf** has a sketch with all the main parts.
3. **Video** - my [assembly video](https://youtu.be/inuvmbNgY5Y) shows the bed adapters, X-axis components, Cube carriage and V6 carriage. In the video I mention a 5010 blower fan - I was wrong, it's a **5015** fan.

!yt inuvmbNgY5Y | BLV mgn12 mod - assembly

!!! note
    You may need to re-center the hotend / bed coordinates in the Marlin configuration.

<div class="gallery" markdown>
![Assembly](../assets/img/img-b8496b40.jpg)
![Assembly](../assets/img/img-dc6eaa67.jpg)
![Assembly](../assets/img/img-0d72dfb3.jpg)
</div>

## More info

- [Greg's geared extruder](https://www.thingiverse.com/thing:18379)
- [Build plate of this project for Simplify3D](https://www.thingiverse.com/thing:2598588)
- [Radial fan fang (including sensor adapters)](https://www.thingiverse.com/thing:2175956)
- [CPT_Spekkie AM8 electronics case](https://www.thingiverse.com/thing:2330654)
- [Devin's knob with a fine-tuning dial](https://www.myminifactory.com/object/44169)
- [PapaJohn88's mount for the Anet A6 LCD](https://www.thingiverse.com/thing:2382917) (recommended by artistebot)
- [Handle for AM8](https://www.thingiverse.com/thing:2409747)
- Green PVC electrical tube for the extruder wires, 13 mm (1/2") - from any electrical shop, also called "split wire loom" - [online here](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20180712230700&SearchText=Split+Wire+Loom) [or here](https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dtools&field-keywords=Split+Wire+Loom&tag=tv-auto-20)

## Rail tips

I used [cheap Chinese MGN12H rails from AliExpress](http://s.click.aliexpress.com/e/b4ZT5JAu) at $18 each. After buying from 4 different sellers, I found [the best rails at the "CNA Mechanical Parts Store"](http://s.click.aliexpress.com/e/b4ZT5JAu). I didn't even need to clean them - the blocks slide smoothly. Wonderful rails, highly recommended!

!!! danger "Stores to avoid"
    Don't buy rails from **"RDC Official Store"** or **"linkcnc Store"** on AliExpress. linkcnc sold me a used, damaged rail, shorter than ordered - it stayed stuck even after cleaning and lubricating. RDC started shipping MGN blocks in non-standard sizes.

**Cleaning and lubricating.** New rails won't be as smooth as they should be: they're coated at the factory with a protective oil that must be cleaned off (YouTube has videos on cleaning the carriage with WD-40). Then lubricate the rails and carriages with sewing machine oil or Teflon silicone grease - not thick grease, these are miniature rails. Ignore the "tilt the rail" smoothness test - it's wrong. You want them smooth, but not too smooth.

**[Cleaning an MGN12H carriage - video](http://www.youtube.com/watch?v=c53sa46C1qQ)** - a pretty good one. **Use a container so you don't lose the steel balls.** After reassembly there will be an empty space of one ball; that's normal.

Fixing the MGN rails can be very frustrating: they must be perfectly aligned and straight, or you'll get headaches. Don't start this project without tons of patience.
