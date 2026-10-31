---
title: Build guide - BLV Ender 3 Pro
description: BLV Ender 3 Pro build guide. Assembly videos and instructions, belts, build volume adjustment and moving the PSU for dual Z.
---

# Build guide

## Assembly videos

!yt RGLydw9Z-Pk | Disassembly steps
!yt 2qyT3RMo_xo | Z axis and extruder assembly
!yt Ezdl2pPzPiA | Bed assembly
!yt jtvkmLhM9FM | X carriage assembly

## Assembly instructions

<div class="gallery big" markdown>
![Assembly instructions](../assets/img/img-ad21ddca.jpg)
![Assembly instructions](../assets/img/img-569c9138.jpg)
![Assembly instructions](../assets/img/img-adc493c1.jpg)
![Bed setup](../assets/img/img-d44b20bb.jpg)
![Rails position](../assets/img/img-a641b5fa.jpg)
</div>

## Belts

The original Creality belt is too flexible and reduces print quality. Use a fiberglass-reinforced GT2 6 mm belt instead. The X axis belt is clamped at a length of **785 mm**, measured between the clamps and not including the brass clamps. When replacing a belt, both ends can be locked with a zip tie.

**Build volume.** To keep the original build volume, change `Y_MIN_POS` in Marlin's **Configuration.h**. My value was **-9.15**. Adjust it to your setup. The picture shows where to find it.

<div class="gallery big" markdown>
![Y axis belt](../assets/img/y-axis-31700401.jpg)
![Build volume adjustment](../assets/img/adjustments-biuld-volum-02fdbc91.png)
</div>

## Dual Z: moving the PSU

The dual Z option requires moving the PSU:

1. Disconnect the PSU from the wall.
2. Disconnect the PSU from the printer.
3. Partly remove the plastic cover from the PSU.
4. Drill M5 holes as shown below.
5. Insert 3 × M5 8 mm button head screws with T-nuts.
6. Put the plastic cover back on the frame and tighten the screws.
7. Put the PSU back and lock it to the cover.

<div class="gallery big" markdown>
![Moving the PSU](../assets/img/psu-3ad9fca5.jpg)
</div>
