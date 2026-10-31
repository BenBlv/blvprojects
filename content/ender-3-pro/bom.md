---
title: BOM - BLV Ender 3 Pro
description: BLV Ender 3 Pro upgrade bill of materials - kit, board, rails, hotend, Z axis options, screws, tools and filaments.
---

# BOM - bill of materials

## Full kit

The easiest way is the full BLV Ender 3 Pro kit: all the aluminum parts, screws and belts.

<div class="grid cards" markdown>

-   [**Full kits**](https://s.click.aliexpress.com/e/_AllpeZ)

    ---

    [![BLV Ender 3 Pro aluminum kit](../assets/img/14-96487860.jpg)](https://s.click.aliexpress.com/e/_AllpeZ)

-   [**Buy the full kit**](https://s.click.aliexpress.com/e/_AllpeZ)

    ---

    [![BLV Ender 3 Pro](../assets/img/ender-with-shadow-7033575a.png){ .no-lightbox }](http://s.click.aliexpress.com/e/dC4nTB6C)

</div>

## General

- 1 × [BLV Ender 3 Pro kit](https://s.click.aliexpress.com/e/_AllpeZ)
    - Have the regular Ender 3 (**not the Pro**) and still want it? Ask the seller to send it without the Y axis, with a discount.
- 1 × [SKR Mini E3 v1.2 board](https://s.click.aliexpress.com/e/_AXmVBT) - highly recommended upgrade ([installation guide](https://www.youtube.com/watch?v=VxCBDyvFSgA))
- 1 × [BLTouch auto-leveling sensor](http://s.click.aliexpress.com/e/qBBPL8Yo) / [original BLTouch with bracket](https://s.click.aliexpress.com/e/_Afq0W5)
- 1 × [transparent BMG extruder](https://s.click.aliexpress.com/e/_A3OmVx) / [Orbiter V2 HQ](https://s.click.aliexpress.com/e/_Aru69x) / [Trianglelab BMG](https://s.click.aliexpress.com/e/_99fl7j) / [DriveKit](https://www.aliexpress.com/item/32904209624.html)
- Filament sensor:
    - [SKR smart filament sensor](http://s.click.aliexpress.com/e/4FrAxFZW) - fantastic! Only with an SKR board ([why](extras.md#smart-filament-sensor))
    - [Simple switch filament sensor](http://s.click.aliexpress.com/e/sdxvnjU8)
- 1 × [heated bed insulation sticker 235 × 235](http://s.click.aliexpress.com/e/oRLzRr3w) - goes under the bed
- 1 × [high quality PTFE tube](http://s.click.aliexpress.com/e/c0Bjxidi) - replaces the stock tube
- 1 × [4 pcs anti-vibration pads](http://s.click.aliexpress.com/e/kmCfLBuU) - under the printer
- 1 × [5V LED strip](http://s.click.aliexpress.com/e/E4GMRYsg) - choose 1 m, 60 LEDs, IP30 non-waterproof; slim and can be cut to fit
- 1 × [high quality aluminium handle](http://s.click.aliexpress.com/e/BWIJ2ykg) - choose the 90 mm aluminum alloy option
- 1 × [yellow strong Creality CR-10 bed springs](http://s.click.aliexpress.com/e/YFNHPjE) - replace the stock springs
- 1 × [high quality silicone sock for the hotend block](http://s.click.aliexpress.com/e/2CsvqM0s) - spare
- 1 × [22AWG wire, 4/5 wires, 5 m](http://s.click.aliexpress.com/e/btaHHrm0) - for the LEDs
- 1 × [Energetic powder coated PEI sheet](http://s.click.aliexpress.com/e/2lEwXoPO) / [Trianglelab powder coated PEI sheet](http://s.click.aliexpress.com/e/FqxxpVYy)
- [SKR touch LCD screen for the Ender 3 Pro](http://s.click.aliexpress.com/e/k6bTgdas) - optional

!!! note "Using the original Z endstop?"
    If you use the original Z endstop and NOT a BLTouch or another leveling sensor, use [this adapter for the Z endstop](https://www.thingiverse.com/thing:4058533).

[![Aluminium kit](../assets/img/aluminium-kit-bar-1f80712e.jpg)](http://s.click.aliexpress.com/e/dC4nTB6C)

## Rails

- 4 × [MGN12H carriage + 300 mm rails](http://s.click.aliexpress.com/e/b4ZT5JAu) (use the frame calculator for other Z sizes)

*Already have the Blurolls kit with rails included? Skip the rails.*

Two options:

- [Set of cheaper rails, $14.6 each - RDBB type](http://s.click.aliexpress.com/e/b4ZT5JAu)
- [Set of HIWIN rails - the best rails on earth - with the BLV upgrade kit](http://s.click.aliexpress.com/e/dC4nTB6C). One of the biggest AliExpress stores is an authorized HIWIN dealer and offers the BLV Ender 3 Pro upgrade with a full set of HIWIN rails. Locally, one rail sells for $68 - if you can afford it, that's a steal. Even E3D uses HIWIN rails.

!!! note
    HIWIN rails should be tested with a load on the carriage.

![MGN carriage warning](../assets/img/mgn-carriage-warning-c4c43311.png){ width="420" }

## Hotend

I highly recommend upgrading to a decent hotend. First decide: stay with Bowden, or go direct drive?

=== "Bowden"

    - [The original Creality hotend](https://s.click.aliexpress.com/e/_9zkfSp) | [cheap hotend clone](http://s.click.aliexpress.com/e/BnnuyFOu)
    - [High quality hotend by Mellow](http://s.click.aliexpress.com/e/3M2Kbf7w)
    - [Excellent quality hotend by Trianglelab](http://s.click.aliexpress.com/e/nOPUd8pS)
    - [Dragon V2 hotend](https://s.click.aliexpress.com/e/_A9Yt1B) - amazing results!

=== "Direct drive"

    [Trianglelab DDE direct drive - 24V full kit](http://s.click.aliexpress.com/e/4EpkugHi) - an amazing system!

    Its X carriage is very similar to the original Ender carriage. To install the DDE you need to drill two small holes for M3×6 mm screws in the carriage - a 2-minute job ([how](extras.md#trianglelab-dde)).

![Hotends](../assets/img/hotends-12030ef9.jpg)

**Use the two screws for alignment only, then remove them.**

![Trianglelab](../assets/img/trianglelab-5ef19d17.jpg)

## Z axis

Choose your Z setup:

1. **Single Z stepper** - I used this for a while and was satisfied, but dual Z adds even more rigidity and dramatically improves the Z axis.
2. **Dual Z with one stepper** - [dual Z kit: one stepper, 2 threaded rods and a belt](https://s.click.aliexpress.com/e/_AXlr6D). Gain back some lost Z height with [this BMG bracket](https://www.thingiverse.com/thing:3117704). I lost some height (the extruder touches the left top plate), but this became my favorite. Replace the kit's original Phillips screws with hex socket head screws from a local shop.
3. **Dual Z with two steppers** - this is the [recommended kit](https://s.click.aliexpress.com/e/_AAdoMv) for dual Z with an additional Z motor. **Align the Z axis to match on both sides.**

<div class="gallery" markdown>
![Dual Z - one stepper setup](../assets/img/p91130-192644-419dd534.jpg)
![Dual Z - two steppers](../assets/img/dual-z-two-steppers-edbbe1a1.jpg)
</div>

!!! note
    This method reduces the Z height, since the BMG can touch the top plates.

## Screws

The screws are already included in the [BLV Ender 3 Pro kit](https://s.click.aliexpress.com/e/_ALVpNX).

| Qty | Part |
| ---: | --- |
| 42 | [M3 8 mm hex socket head screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 8 | [M3 10 mm hex socket head screw](http://s.click.aliexpress.com/e/dC4nTB6C) |
| 4 | [M3 14 mm hex socket head screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 2 | [M3 6 mm hex socket head screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 2 | [M3 6 mm hex flat countersink screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 2 | [M3 16 mm hex flat countersink screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 1 | [M3 20 mm hex flat countersink screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 4 | [M3 50 mm hex flat countersink screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 12 | [M5 8 mm hex button head screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 2 | [M4 40 mm hex button head screw](https://s.click.aliexpress.com/e/_ALVpNX) |
| 2 | [M4 Nyloc](https://s.click.aliexpress.com/e/_ALVpNX) |
| 5 | [M3 Nyloc](https://s.click.aliexpress.com/e/_ALVpNX) |
| 14 | [M3 0.5 mm washer](https://s.click.aliexpress.com/e/_ALVpNX) |
| 32 | [M3 T-nut](https://s.click.aliexpress.com/e/_ALVpNX) |
| 10 | [M5 T-nut](https://s.click.aliexpress.com/e/_ALVpNX) |

**Only for dual Z:**

- 2 × [M3 10 mm hex button head screws](https://s.click.aliexpress.com/e/_ALVpNX)
- 4 × [M3 0.5 mm spring washer](http://s.click.aliexpress.com/e/dC4nTB6C)
- 1 × [100 pcs M3 spring washers](http://s.click.aliexpress.com/e/MlwOTumM) - optional

## Tools

- [Cable cutter](http://s.click.aliexpress.com/e/IacurE0)
- 2 × cheap steel wrenches - for the block and nozzle assembly
- [PTFE tube cutter](http://s.click.aliexpress.com/e/c5dDYfHW)
- [Dehumidifier (moisture absorber) for your dry box](https://s.click.aliexpress.com/e/_9z5kLX) - the best I tested
- [Stainless steel digital caliper](http://s.click.aliexpress.com/e/brCQyMCY)
- [Cable organizer](http://s.click.aliexpress.com/e/cLxQo5m0)
- [New Pinecil soldering iron](https://s.click.aliexpress.com/e/_A17thR) - it's amazing
- [Belt tension meter - 3D printed tool](https://www.thingiverse.com/thing:2230598)

## Optional

- [Easy fast wire connectors](http://s.click.aliexpress.com/e/cq30k5Yk)
- [Mayitr black braided cable sleeve, like Prusa](http://s.click.aliexpress.com/e/c4TGFoTe)
- [5 m LED strip 5050, 60 LEDs/m, 44-key, waterproof](http://s.click.aliexpress.com/e/bLv0LorW)
- [Wago compact wiring connector](http://s.click.aliexpress.com/e/cpmjKbk8)
- [500 pcs 3/32" G10 hardened steel balls for MGN12H rails](http://s.click.aliexpress.com/e/bNxC5T6s) (replacement)

## Filaments I used

- [NOULEI silk filaments](http://s.click.aliexpress.com/e/l3V3Lymy) | [link 2](http://s.click.aliexpress.com/e/dAY2Eky0) - most of my prints
- [1 kg PETG transparent black](https://s.click.aliexpress.com/e/_9u3xeD)
- [1 kg PLA silver](https://s.click.aliexpress.com/e/_APGkMv)
- [1 kg silk PLA gold](http://s.click.aliexpress.com/e/bgV8dvqu) - the best silk filament I've tested
