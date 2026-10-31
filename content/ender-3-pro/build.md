---
title: Build guide - BLV Ender 3 Pro
description: BLV Ender 3 Pro build guide - assembly videos and instructions, belts, build volume adjustment and moving the PSU for dual Z.
---

# Build guide

## Assembly videos

!yt RGLydw9Z-Pk | BLV Ender 3 Pro Project - disassembly steps
!yt 2qyT3RMo_xo | BLV Ender 3 Pro - Z axis and extruder assembly
!yt Ezdl2pPzPiA | BLV Ender 3 Pro - bed assembly
!yt jtvkmLhM9FM | BLV Ender 3 Pro - X carriage assembly

## Assembly instructions

<div class="gallery" markdown>
![Assembly instructions](../assets/img/img-ad21ddca.jpg)
![Assembly instructions](../assets/img/img-569c9138.jpg)
![Assembly instructions](../assets/img/img-adc493c1.jpg)
![Bed setup](../assets/img/img-d44b20bb.jpg)
![Rails position](../assets/img/img-a641b5fa.jpg)
</div>

## Belts

The original Creality belt is too flexible and hurts print quality. The kit comes with a fiberglass-reinforced GT2 6 mm belt, which is much better. The X-axis belt is clamped at a length of **785 mm** (the belt between the clamps, not including the brass clamps). If you need to replace a belt, you can lock both ends with a zip tie.

![Y axis belt](../assets/img/y-axis-31700401.jpg)

### Build volume adjustment

To keep the original build volume, change `Y_MIN_POS` in Marlin's **Configuration.h**. My calculation came to **-9.15**; adjust it to your needs. The picture shows where to find it.

![Build volume adjustment](../assets/img/adjustments-biuld-volum-02fdbc91.png)

## Dual Z - move the PSU

With the dual Z option, the PSU has to move:

1. Disconnect the PSU from the wall.
2. Disconnect the PSU from the printer.
3. Partly remove the plastic cover from the PSU.
4. Drill M5 holes as shown below.
5. Insert 3 × M5 8 mm button head screws + T-nuts.
6. Put the plastic cover back on the frame and tighten the screws.
7. Put the PSU back and lock it to the cover.

![Moving the PSU](../assets/img/psu-3ad9fca5.jpg)
