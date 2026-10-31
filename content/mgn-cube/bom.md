---
title: BOM - BLV mgn Cube
description: BLV mgn Cube bill of materials - frame, motion system, electronics, hotends, screws, panels, tools - with the parts I tested and where to buy them.
---

# BOM - bill of materials

To build the printer you need mechanical and electrical parts prepared in advance, plus the parts I designed for the BLV mgn Cube. I bought the parts myself, tested them one by one and organized everything here so you know what you really need.

Before the list, two decisions. Each one changes what you buy.

## Decision 1: Metal Kit or printed parts?

A large part of the printer is printed. Printing the parts saves money but takes a long time and some skill. After the project came out I released the **[BLV Metal Kit](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube)** - an aluminum kit that replaces most of the printed parts and is stronger, more reliable and more accurate. **The Metal Kit is the recommended choice.**

| | BLV Metal Kit (recommended) | 3D print my own parts |
| --- | --- | --- |
| Pros | <span class="pro">Ready to install · 10× more rigid than printed parts · accurate</span> | <span class="pro">Cheap · ideal for remixing</span> |
| Cons | <span class="con">Costs more than printed parts · shipping time</span> | <span class="con">Needs post-processing · less rigid · elastic · printing takes a long time</span> |

## Decision 2: Full kit or parts separately?

The rest of the electronics and mechanics are in the [list below](#bom), all personally tested. Buying the parts separately is cheaper, but shipping can take long. Because of the project's popularity two stores made full kits: the first by Blurolls, and later an [improved kit by FYSETC](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit), which I reviewed. The new step-by-step assembly guide is based on the FYSETC kit.

| | Full kit | Parts separately |
| --- | --- | --- |
| Pros | <span class="pro">Saves a lot of time · fast shipping · contains all parts</span> | <span class="pro">Cheaper</span> |
| Cons | <span class="con">Costs more</span> | <span class="con">Parts don't arrive together · long delivery time</span> |

### Which kit?

After testing both kits, the [FYSETC kit](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit) became my favorite: many important upgrades, good support and high-quality parts. Both kits include the new Blind Joints frame (fast assembly). Only the Blurolls kit includes the Metal Kit.

=== "FYSETC full kit (recommended)"

    [![FYSETC](../assets/img/fysetc-70c91355.png){ width="120" .no-lightbox }](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit)

    - <span class="pro">Cheaper (USA and Spain warehouses)</span>
    - <span class="pro">Many great upgrades</span> - [check my review](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit)
    - <span class="pro">Support (GitHub + full firmware)</span>
    - <span class="pro">Superior Mean Well 600W PSU</span>
    - <span class="pro">Upgraded 5" PanelDue LCD v3.0</span>
    - <span class="pro">Unique BLV Neopixel PCB system</span>
    - <span class="pro">Faster assembly · tools included · convenient wiring system</span>
    - <span class="con">Metal Kit not included</span>

    [FYSETC full kit](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit){ .md-button .md-button--primary }

=== "Blurolls kit"

    ![Blurolls](../assets/img/blutolls-fd95b05c.png){ width="100" .no-lightbox }

    - <span class="pro">HIWIN linear rails</span>
    - <span class="pro">Cheaper light kit version</span> (not supported)
    - <span class="pro">Metal Kit included</span>
    - <span class="con">Costs more</span>
    - <span class="con">Duet WiFi 2 v1.03 (v1.04 recommended)</span>
    - <span class="con">Mid-quality hotend</span>
    - Ask the seller to upgrade to the metal bed

    [Full kit](http://s.click.aliexpress.com/e/cmcYPkdE){ .md-button .md-button--primary }
    [Light kit](http://s.click.aliexpress.com/e/rEgD8U0C){ .md-button }

Got a full kit? [Skip to the optional parts](#optional).

## BOM

[Frame](#frame) · [Motion system](#motion-system) · [Main electronics](#main-electronics) · [Mechanics](#mechanics-and-more) · [Screws](#screws) · [Panels](#panels) · [Optional](#optional) · [Tools](#tools) · [Useful links](#useful-links)

!!! note "Sizes"
    The BOM is for a **365 mm Z height**. For a different size, use the calculator Excel file **BLV_mgn_Cube-Frame_calculator.xlsx** in the project ZIP.

## Frame

Buying the extrusions from a local store is usually cheaper. But I also released an upgraded **BLV Blind Joints** frame, available online, that saves 70% of the assembly time and is more stable and accurate ([demo video](https://www.youtube.com/watch?v=ueniUWrUcjE)).

| | Blind Joints frame kit | Local store |
| --- | --- | --- |
| Pros | <span class="pro">Saves 70% of assembly time · easy assembly ([my review](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit)) · much more accurate and stable · bracket-free build</span> | <span class="pro">Cheaper · faster shipping</span> |
| Cons | <span class="con">Costs more · ships from China / EU / USA warehouses</span> | <span class="con">Long assembly time · not as accurate</span> |
| Where | [FYSETC Blind Joints frame kit](http://s.click.aliexpress.com/e/bdOdV8RO) · [Blurolls frame kit](https://www.aliexpress.com/item/1005001591680638.html) · included in both BLV full kits | Your local supplier |

![Frame calculator](../assets/img/calculator-6fc8118b.jpg){ width="520" }

### Extrusions

- 9 × [2040 aluminum extrusion](https://s.click.aliexpress.com/e/_DlQnxlh) 496 mm (wide beams)
- 3 × [2020 aluminum extrusion](https://s.click.aliexpress.com/e/_DlQnxlh) 576 mm (aux wide beams)
- 4 × [2040 aluminum extrusion](https://s.click.aliexpress.com/e/_DlQnxlh) 560 mm (4 corner height beams)
- 2 × [2040 aluminum extrusion](https://s.click.aliexpress.com/e/_9J8l7c) 442 mm (Z axis)
- 2 × [2040 aluminum extrusion](https://s.click.aliexpress.com/e/_9J8l7c) 405 mm (bed frame)
- 2 × [2020 aluminum extrusion](https://s.click.aliexpress.com/e/_DlQnxlh), length by bed:
    - [CR-10](https://s.click.aliexpress.com/e/_DlQnxlh) bed: **173 mm**
    - [Anet](https://s.click.aliexpress.com/e/_DlQnxlh) bed: **142 mm**
    - [E3D high temp](https://s.click.aliexpress.com/e/_DlQnxlh) (314 × 314) bed: **240 mm**
    - [Ender 3](https://s.click.aliexpress.com/e/_DlQnxlh) bed: **106 mm**

**X axis - choose one:**

- 1 × [2020 aluminum extrusion](https://s.click.aliexpress.com/e/_DlQnxlh) 460 mm
- 1 × [**upgraded** lightweight **carbon fiber** X-axis](https://s.click.aliexpress.com/e/_DD2c4YF)
- 1 × [**upgraded** aluminium alloy CNC cut X-axis tube 460 mm](https://s.click.aliexpress.com/e/_DDJPdlv)

<div class="gallery" markdown>
![Frame measurements](../assets/img/img-4e8e86fd.jpg)
![Frame reinforcement](../assets/img/reinforcement-402b0a1e.jpg)
</div>

**Optional - frame reinforcement for taller Z builds (465 mm+):**

- 1 × [2020 aluminum extrusion](https://s.click.aliexpress.com/e/_DlQnxlh) 496 mm
- 4 × [aluminum 2020 brackets](https://s.click.aliexpress.com/e/_DD1V16j) 20×20 / 20×17

**Triple Z magnetic system:** based on the work of BLV community member [Druce Taylor](https://www.thingiverse.com/thing:4611244) - a non-official [add-on for triple Z](https://www.thingiverse.com/thing:4611244).

- [3-point bed leveling (triple Z) - MJF + embedded parts](https://s.click.aliexpress.com/e/_DFj5VlD)

**Other:**

- 2 × [T-shape bracket 60×60](http://s.click.aliexpress.com/e/3RhFdTa) (supports the Z rail extrusions)
- 14 × [corner 90° angle bracket](https://s.click.aliexpress.com/e/_AbriPg) for 2020/2040
- 100 × [aluminum 2020 brackets](https://s.click.aliexpress.com/e/_A2p4Tg) 20×20 / 20×17

**Frame kit** (you may find the extrusions much cheaper locally):

- [FYSETC aluminum profiles set / full frame kit - **Blind Joints frame**](https://s.click.aliexpress.com/e/_DlQnxlh)
- [Frame kit on AliExpress](https://www.aliexpress.com/item/1005001993105814.html)

**Screws and bracket kits:**

- [FYSETC brackets, corners, T-nut and M5 screw kit](http://s.click.aliexpress.com/e/puvPpze)
- [Second source for the hardware kit](https://s.click.aliexpress.com/e/_DDRafbH)

!!! warning "Frame notes"
    - Be precise and use the correct extrusions, no shortcuts - using 2020 instead of 2040 reduces the frame rigidity.
    - Use regular European extrusions with MGN rails, not the V-slot type.

[![Extrusions](../assets/img/extrusions-58025380.jpg){ width="520" }](https://s.click.aliexpress.com/e/_DlQnxlh)

## Motion system

### Rails

- 5 × [MGN12H carriage + 400 mm rails](https://s.click.aliexpress.com/e/_DmEozrH) from the [CNA store](http://s.click.aliexpress.com/e/b4ZT5JAu) (use the frame calculator for other Z sizes)
- [Set of cheaper rails, $17 each](https://s.click.aliexpress.com/e/_DmEozrH) - I bought these first; choose 400 mm + MGN12H
- [Set of HIWIN rails - the best rails on earth](http://s.click.aliexpress.com/e/cTl59jr2) or a [single HIWIN rail](http://s.click.aliexpress.com/e/bOWLVhhO). One of the biggest AliExpress stores is an authorized HIWIN dealer and offers a full HIWIN kit at a good price; locally one rail costs about $80. If you can afford it, that's a steal - even E3D uses HIWIN rails. (HIWIN rails should be tested with a load on the carriage.)

!!! tip
    For high precision rail installation, [use this adapter](https://s.click.aliexpress.com/e/_DBqJqer).

!yt HQoGXPk7drw | Genuine HIWIN MGN rails for the BLV mgn Cube 3D printer

### Stepper motors

- 2 × X/Y [Nema 17 stepper 42STH48 2504AC 48 mm 2.5 A - **updated version**](https://s.click.aliexpress.com/e/_DdPNBjz)
- 2 × Z [Nema 17 stepper 42STH48 2504AC 48 mm 2.5 A - **updated version**](https://s.click.aliexpress.com/e/_DdPNBjz)
- 1 × extruder stepper - not needed, it comes with the extruder
- 2 × [high quality GT2 pulley 16 teeth](http://s.click.aliexpress.com/e/cLqfXLpQ) (for the X/Y steppers)

**Stepper kits** - the [**42STH48 2504AC**](https://s.click.aliexpress.com/e/_DdPNBjz) is preferred; these are older kits:

- [LDO motor kit for BLV mgn Cube](https://www.aliexpress.com/item/1005002090721056.html)
- Moon motors kit for BLV project
- [Stepper kit for BLV mgn Cube - StepperOnline store](http://s.click.aliexpress.com/e/b0T6TI9a) (not tested)
- [Stepper motors kit from the Blurolls store](http://s.click.aliexpress.com/e/cS4usW5a)

### Belt system

See the [assembly page](assembly.md#belt-system) for the belt path.

- 24 × [F623ZZ flange ball bearings - **get only option 3**](http://s.click.aliexpress.com/e/WJXxClE). I recommend flipping the belts at the rear (see the belt system image). Don't use the geared GT2 16T.

!!! warning
    An Amazon seller sells low-quality 623ZZ bearings for triple the price. They are loose and will ruin your printing experience.

### Belts and threaded rods

- 1 × [4 m Gates 6 mm GT2 fiberglass reinforced belt](http://s.click.aliexpress.com/e/bvgA8Jbi) / [4 m Gates 6 mm GT2 - tested](http://s.click.aliexpress.com/e/lMixbe0) / [4 m 6 mm GT2 reinforced belt (6mm-LL-2GT RF) - high quality](https://s.click.aliexpress.com/e/_Am6zMq)
- 2 × [upgraded Teflon PTFE 8 mm leadscrew, 400 mm](https://s.click.aliexpress.com/e/_DCOm5Sx) (choose "lead8mm 400")
- 2 × [Mellow NF Oldham coupling for the Z rods](https://s.click.aliexpress.com/e/_DdsqySP)

## Main electronics

First choose your firmware: **RepRap** or **Klipper**.

=== "Klipper (recommended - faster, advanced features)"

    **Board** - one of:

    - [BIGTREETECH Octopus V1.1](https://s.click.aliexpress.com/e/_DlHZzxd) (board only, without drivers)
    - [FYSETC Spider V2.2 32-bit motherboard](https://s.click.aliexpress.com/e/_DkG4XUJ) (board only, without drivers) - **the board I use**

    **Drivers** - the board needs them:

    - 6 × [Mellow Fly 24V/48V HV TMC5160 Pro V1.2 drivers](https://s.click.aliexpress.com/e/_DliqsiP) (recommended)
    - **or** 6 × [FYSETC TMC5160 QHV 60V stepstick](https://s.click.aliexpress.com/e/_DCY9Ugb)

    **Raspberry Pi** to control the board:

    - [Raspberry Pi 4 4/8 GB Model B](https://s.click.aliexpress.com/e/_DEpa46f) - get the cooled case kit option
    - **or** cheaper: [BIGTREETECH Pi4B adapter + CB1 core board](https://s.click.aliexpress.com/e/_DDEt6yb) - or use an [original Raspberry CM4](https://s.click.aliexpress.com/e/_DcwmgVd) instead of the CB1

=== "RepRap"

    - 1 × [Duet WiFi 32-bit mainboard](http://s.click.aliexpress.com/e/_dZhVdmB) - the best board for your printer
    - **or** 1 × [Duet 3 6HC 32-bit motherboard](https://s.click.aliexpress.com/e/_DkObfYr) - powerful, built-in drivers
    - 1 × [PanelDue 5" screen (not the "5i")](http://s.click.aliexpress.com/e/bwwzkkpK) - or save $80 and use your phone / tablet

**Z offset sensor - choose only one:**

- [Mini differential IR auto leveling sensor](http://s.click.aliexpress.com/e/coEOOhKC) (not for glass)
- [BLTouch auto leveling sensor](https://s.click.aliexpress.com/e/_DdLRlVv)
- [Super PINDA sensor 5V](https://s.click.aliexpress.com/e/_DFlNxe3) - **I use it and it's great**

**Power, wiring and fans:**

- 1 × [Mean Well LRS-350-24 (24V)](https://s.click.aliexpress.com/e/_DnBS6k7) **and** 1 × [Mean Well LRS-350-48 (48V)](https://s.click.aliexpress.com/e/_DnBS6k7) - the 48V HV TMC5160 setup needs [both PSUs, 24V + 48V](https://www.aliexpress.com/store/product/BLV-MGN-Cube-3d-printer-good-quality-power-supply-Geniune-Meanwell-PSU-SE-450-24-24V18/2808029_32988813396.html)
- 2 × [3-pin endstop switch KW11-3Z](http://s.click.aliexpress.com/e/xaJ9E2y)
- 1 × [heat insulation 300 mm for the bed](http://s.click.aliexpress.com/e/HdBbxLw)
- 3 × [NeoPixel ring **16 LEDs** WS2812 module](https://s.click.aliexpress.com/e/_Dd3f9GJ) (black)
- 1 × [5 m silicone wire 14AWG, black/red](http://s.click.aliexpress.com/e/c5ts2wZS)
- 1 × [22AWG wire, 4/5 wires, 5 m](http://s.click.aliexpress.com/e/btaHHrm0)
- 1 × [16 mm momentary switch with LED, 110/220V (wall voltage) - power icon](http://s.click.aliexpress.com/e/cOgjjw4g)
- 2 × [16 mm momentary / latching switch with LED 12/24V](http://s.click.aliexpress.com/e/b1i9Fkha) - optional
- 3 × [4010 24V fan, 2-pin, dual ball bearing](http://s.click.aliexpress.com/e/bjuRTQJe) or a [cheap 24V fan](http://s.click.aliexpress.com/e/bNQ2C3C8) - add 4 for the small air scrubber
- 1 × [5015 blower fan 24V, ball bearings](http://s.click.aliexpress.com/e/cTnlOmKc)
- 2 × [4010 blower fans 24V (dual ball bearings)](http://s.click.aliexpress.com/e/bR84eKyo) - only for the new twin blower shield
- 1 × [24V to 12V 15A step-down converter](http://s.click.aliexpress.com/e/cs6KZwJI) - only with the Anet E12 bed
- 2 × [120 mm fan 24V, ball bearings, 3000 RPM](http://s.click.aliexpress.com/e/bJjclu56) - for the bigger air scrubber

### Hotend - choose one

1. **Mellow lightweight NF-Sunrise V1.1 dual drive extruder** (it has its own section). Add the [Mellow Fly-SHT board](https://s.click.aliexpress.com/e/_DE7tSZl).
2. [Trianglelab TCHC TD6 high flow 24V](https://s.click.aliexpress.com/e/_DBsqqZd) + [BIQU Orbiter extruder V2.0](https://s.click.aliexpress.com/e/_DCS2FPN) + [Mellow Fly-SHT board](https://s.click.aliexpress.com/e/_DE7tSZl)
3. **[BIQU / BigTreeTech](https://s.click.aliexpress.com/e/_DCeiYqr) H2** - a lightweight extruder + hotend in one. I use the [H2 V2S Lite](https://s.click.aliexpress.com/e/_DBCLutV) with the 48V setup and it's amazing (25K accel / 1250 mm/s). A carriage for the H2 series was published in a post long ago.
    1. [BIQU H2 V2S Revo](https://s.click.aliexpress.com/e/_DCFWy8T)
    2. [BIQU H2 V2S Lite](https://s.click.aliexpress.com/e/_DBCLutV) - **only 180 g, preferred**
    3. [BIQU H2 V2.0](https://s.click.aliexpress.com/e/_DdT9ymP)
4. **Trianglelab Matrix series:**
    1. [Trianglelab Matrix](https://s.click.aliexpress.com/e/_DeZtOPD)
    2. [Trianglelab Matrix LC Lite](https://s.click.aliexpress.com/e/_DEfkeiB) + [water cooling system](https://www.aliexpress.com/item/32850217541.html) (24turn12v option) + [thermal fluid](https://s.click.aliexpress.com/e/_DBuSiTv)

!!! note "Trianglelab hotend on RepRap"
    Change the M305 line in `config.g` to: `M305 P1 T100000 B4725 C0.0000000706 R4700`

**Tool changer (advanced users):** [E3D toolhead clone by Funssor for MGN12H](https://s.click.aliexpress.com/e/_Dm5VvUX)

**Hotend upgrades:**

- [**A must-have nozzle upgrade: CHT clone for high flow printing**](https://s.click.aliexpress.com/e/_DlRJk15) (get the 0.4)
- Spare thermistors: [Semitec 104GT-2](http://s.click.aliexpress.com/e/b3YkgynA) / [thermistor + connector](http://s.click.aliexpress.com/e/c2IGfgLA) / [regular thermistor](https://s.click.aliexpress.com/e/_DBgg7GB)
- [Phaetus **tungsten carbide** nozzle](https://s.click.aliexpress.com/e/_DEAzwrv) - super wear resistant (carbon, wood...)
- [Hardened steel A2 nozzle](https://s.click.aliexpress.com/e/_DepZDr9) for abrasive materials

### Heated bed (8 mm bed)

- [High quality 8 mm 310 × 310 mm aluminium 7075 bed for BLV / Voron](https://s.click.aliexpress.com/e/_Dmsq70n)
- [Silicone heater pad 310 × 310, 750W + adhesive](https://s.click.aliexpress.com/e/_DD6ifvp) (choose 220V / 120V / 24V)
- [Thumb dial wheels](http://s.click.aliexpress.com/e/bKMV1NCy) - choose M4
- [PEI spring steel PET system](https://s.click.aliexpress.com/e/_DCVXv3H) (choose 310, no magnetic base)
- [Silicone solid stand-offs](https://s.click.aliexpress.com/e/_Dn3AjbV) - replace the bed springs

## Mechanics and more

- 1 × [BMG extruder](https://s.click.aliexpress.com/e/_DnclLVh) - for old school users
- 1 × [1 m Capricorn clone PTFE tube, 1.9 or 2 mm ID](http://s.click.aliexpress.com/e/c0Bjxidi)
- 2 × [635ZZ ball bearing for aligning the stepper shaft](http://s.click.aliexpress.com/e/bdteVkks) - optional
- 5 × [high quality silicone sock](https://s.click.aliexpress.com/e/_Dl41fjN) - keeps the nozzle temperature steady

## Screws

Screws are usually sold in bulk, so the quantities are rounded. You can also get the [full screws, nuts, brackets and corners kit](https://s.click.aliexpress.com/e/_DFv3oaJ).

| Qty | Part | Note |
| ---: | --- | --- |
| 300 | [M5 10 mm button head socket cap screw](http://s.click.aliexpress.com/e/cpnplQQc) | buy at least 300-350 |
| 2 | [M5 16 mm button head socket cap screw](http://s.click.aliexpress.com/e/bPEOlP9A) | |
| 4 | [M5 35 mm button head socket cap screw](http://s.click.aliexpress.com/e/bPEOlP9A) | |
| 200 | [M5 washers](https://s.click.aliexpress.com/e/_DmLXgTt) | |
| 283 | [**Upgraded** M5 roll-in spring T-nut](https://s.click.aliexpress.com/e/_Dc8Guzd) | get at least 300 |
| 4 | [M4 40 mm flat head machine screw](https://s.click.aliexpress.com/e/_DlbxgCT) | for the bed |
| 2 | [M4 30 mm hexagon head](http://s.click.aliexpress.com/e/OI2rlP6) | |
| 2 | [M4 nut](https://s.click.aliexpress.com/e/_Dme4c6n) | |
| 78 | [M3 8 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | buy at least 100 |
| 2 | [M3 10 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 8 | [M3 12 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 1 | [M3 16 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 5 | [M3 16 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | only if NOT using the block cover |
| 8 | [M3 18 mm socket head cap screw](http://s.click.aliexpress.com/e/c0dWFb9m) | only with the block cover |
| 8 | [M3 22 mm socket head cap screw](http://s.click.aliexpress.com/e/c0dWFb9m) | |
| 3 | [M3 25 mm socket head cap screw](http://s.click.aliexpress.com/e/c0dWFb9m) | |
| 2 | [M3 30 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 13 | [M3 35 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 4 | [M3 40 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 2 | [M3 50 mm socket head cap screw](https://s.click.aliexpress.com/e/_DdxB7EL) | |
| 11 | [M3 14 mm Phillips round head](https://s.click.aliexpress.com/e/_DEbeJuP) | |
| 2 | [M3 18 mm Phillips round head](https://s.click.aliexpress.com/e/_DEbeJuP) | |
| 1 | [M3 22 mm Phillips round head](https://s.click.aliexpress.com/e/_DEbeJuP) | |
| 3 | [M3 25 mm Phillips round head](https://s.click.aliexpress.com/e/_DEbeJuP) | |
| 40 | [**Upgraded** M3 roll-in spring T-nut](https://s.click.aliexpress.com/e/_Dc8Guzd) | |
| 62 | [M3 0.5 mm washer](http://s.click.aliexpress.com/e/ZTKSC40) | 2 × 0.5 mm or one 1 mm washer; buy at least 100 |
| 26 | [M3 nut](http://s.click.aliexpress.com/e/c2TqLSnI) | buy at least 50 |
| 16 | [M3 Nyloc](http://s.click.aliexpress.com/e/h5iPrs4) | |
| 4 | [M2.5 12 mm flat head machine screw](http://s.click.aliexpress.com/e/c0dWFb9m) | |

## Panels

How I made the walls / semi-enclosure - cheap and very easy. Choose a board:

- 4 mm cardboard sheets (cheap)
- KAPA foam boards (cheap)
- Aluminum composite panel
- 4 mm plywood sheets

Then apply this [carbon fiber vinyl](https://s.click.aliexpress.com/e/_DBgNjFN) to the board, and secure it to the frame with M3 / M5 screws.

![BLV mgn Cube panels / walls dimensions](../assets/img/blv-mgn-cube-panels-walls-dimensions-ae561374.jpg)

## Optional

- [Easy fast wire connectors](http://s.click.aliexpress.com/e/cq30k5Yk)
- [1 m corrugated tube](http://s.click.aliexpress.com/e/VAVZHrw)
- [Mayitr black braided cable sleeve, like Prusa](http://s.click.aliexpress.com/e/c4TGFoTe)
- [Solid state relay SSR-25DA](http://s.click.aliexpress.com/e/c9BSvYtK) to turn the printer on with a button + [SSR heatsink](http://s.click.aliexpress.com/e/bC2PgQK4)
- [Wago compact wiring connector](http://s.click.aliexpress.com/e/cpmjKbk8)
- [Activated carbon filter](http://s.click.aliexpress.com/e/5gNEcdn6) (for the bigger air scrubber)
- [500 pcs 3/32" G10 hardened steel balls for MGN12H rails](http://s.click.aliexpress.com/e/bNxC5T6s) (replacement)
- [100K NTC 3950 thermistors](http://s.click.aliexpress.com/e/bPgML85K) (replacement if broken)
- [HEPA filter for iLife vacuum robots](http://s.click.aliexpress.com/e/b0PPT4Co) - for the smaller air scrubber
- [HEPA filter for Eufy RoboVac 11c](http://s.click.aliexpress.com/e/BpDoZAo) - for the bigger air scrubber
- [Soundproofing acoustic foam tiles](https://s.click.aliexpress.com/e/_DC5Z6wn)

**Filaments I used for the project:**

- [1 kg PETG transparent green / black / blue](https://s.click.aliexpress.com/e/_9RCwpL)
- [Dual color PLA 250 g](https://s.click.aliexpress.com/e/_DFzLWwf) (test prints)
- [Rainbow silk PLA, high tolerance](https://s.click.aliexpress.com/e/_DC8xPcn) (test prints)
- [NOULEI silk filaments](http://s.click.aliexpress.com/e/l3V3Lymy) | [link 2](http://s.click.aliexpress.com/e/dAY2Eky0) (test prints)
- [1 kg PLA silver](http://s.click.aliexpress.com/e/0QZwKnO) (test prints)

**Filament dryer box:**

- [SUNLU S2 filament dryer](https://s.click.aliexpress.com/e/_DeOjZ9t) - amazing dryer
- [eSUN eBOX Lite filament dryer](https://s.click.aliexpress.com/e/_DkgEZjz) (cheaper)

## Tools

- [**Must have:** new 90° corner aluminum clamps](https://s.click.aliexpress.com/e/_DneF1GX) for a good frame assembly
- [Cable cutter](http://s.click.aliexpress.com/e/IacurE0)
- [SN-28B Dupont crimping tool](http://s.click.aliexpress.com/e/ctVlu2Gs)
- [Tapping kit](https://s.click.aliexpress.com/e/_DCKRUM7) - mainly for the corner holes
- [PTFE tube cutter](http://s.click.aliexpress.com/e/c5dDYfHW)
- [Wire copper terminal set](http://s.click.aliexpress.com/e/tAR0say)
- [10 pairs JST plug male/female connectors](http://s.click.aliexpress.com/e/bcEVk7rK) for Dupont wires
- [Dupont wire jumper pin header connector housing kit](http://s.click.aliexpress.com/e/chftfcwG)
- [Dehumidifier (moisture absorber) for your dry box](https://s.click.aliexpress.com/e/_DeihM7v) - the best I tested
- [Mitutoyo 500-196-20 digital caliper](https://s.click.aliexpress.com/e/_DD8IAqf)
- [Cable organizer](https://s.click.aliexpress.com/e/_DnCWVdh)
- [Pine64 BB2 Pinecil soldering iron](https://s.click.aliexpress.com/e/_DlzKPjH)
- [Belt tension meter - 3D printed tool](https://www.thingiverse.com/thing:2230598)

## Useful links

- [Full screws kit for the BLV mgn Cube from Blurolls](http://s.click.aliexpress.com/e/c0dWFb9m)
- [440 pcs set of M3 socket cap head DIN912 screws](http://s.click.aliexpress.com/e/bEBhHo8s)

