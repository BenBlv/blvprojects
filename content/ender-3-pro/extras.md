---
title: Tips & extras - BLV Ender 3 Pro
description: BLV Ender 3 Pro extras - smart filament sensor, PEI surface, LEDs, bed springs, Trianglelab DDE, extra printed parts, rail tips and print samples.
---

# Tips & extras

## Smart filament sensor

What's so special about the **SKR [smart filament sensor](http://s.click.aliexpress.com/e/4FrAxFZW)**? At first I was confused: why pay $15 when a wire and an endstop switch cost $1.5? After [watching this video](http://Youtube.com/watch?v=iFGIKMAGJTk) I understood the potential.

A switch sensor only knows whether filament is there. If the spool jams or the filament gets stuck - nothing happens, and the printer keeps printing air. The smart sensor tracks the filament movement with a rotary encoder: if it suddenly jams, the print pauses. Worth every cent, especially for huge prints (12+ hours). A big like for this [smart filament sensor](http://s.click.aliexpress.com/e/4FrAxFZW)!

![Smart filament sensor](../assets/img/smart-filament-sensor-379f6e53.jpg)

## PEI surface

After a long time with the Energetic PEI spring steel sheet, I tested the new Trianglelab double-coated PEI spring steel sheet. It came well packed with alcohol wipes and - yes - a printed manual. The first try was a complete fail: the corners lifted. Then I read the manual, and the last tip did the trick: **scratch the PEI really well with brass wool**, and prints stick great. And unlike the Energetic PEI, prints release easily once the sheet cools down.

![Scratch the PEI sheet with brass wool](../assets/img/brass-wool-541ef7f5.jpg)

## LED installation

Use a 5V, 60 LEDs/m, non-waterproof strip that can be cut after every LED - the non-waterproof type slides into the V-slot channel more easily.

1. Cut a 15-LED strip, solder a long 4-wire cable to it, and slide it into the top V-slot channel.
2. Cut a 3-LED strip, solder a cable to it, and secure it with 2 zip ties to the back of the [transparent BMG extruder](https://s.click.aliexpress.com/e/_A3OmVx).
3. Connect both strips together and check the connection.
4. Then either:
    - connect them to an RGB LED controller (simple) and use the IR remote, or
    - connect them to the SKR Mini E3 LED pins and configure it.

![LED installation](../assets/img/led-installation-f824b3f9.jpg)

## Bed carriage springs

Replace the original Ender 3 Pro bed springs with the [yellow strong Creality CR-10 bed springs](http://s.click.aliexpress.com/e/YFNHPjE). The bed will be much more stable.

![Bed carriage springs](../assets/img/sprrings-6f325c47.jpg)

## Trianglelab DDE

How to install the Trianglelab DDE system:

1. Print `Carriage template.stl`.
2. Place the drilling template on the rear of the DDE system.
3. Drill two holes as shown, with a 6 mm drill bit, 4 mm deep.
4. Remove the template.
5. Install the DDE on the X carriage.

![Trianglelab DDE installation](../assets/img/triangelab-installl-622b3be2.jpg)

[Trianglelab DDE installation tutorial & STL](https://drive.google.com/drive/folders/1KL6InrIttUU6s1C7EP5DR8_zmNnUmlQb?spm=a2g0o.detail.1000023.51.47dc9b5afl5hrg){ .md-button }

## More printed parts

- [BMG bracket](https://www.thingiverse.com/thing:3117704) - with dual Z on one stepper, it gains back the lost Z height by lowering the BMG and stepper motor
- [Filament holder with ball bearings](https://www.thingiverse.com/thing:3209211)
- [Power supply silencer](https://www.thingiverse.com/thing:3659432)
- [Bed cable holder](https://www.thingiverse.com/thing:3423163)
- [Ender 3 / Pro X-axis cable holder](https://www.thingiverse.com/thing:2949858)
- [LCD cable holders](https://www.thingiverse.com/thing:2960375)
- [Very good filament filter](https://www.thingiverse.com/thing:497764) - recommended

## Rail tips

I used [cheap Chinese MGN12H rails from AliExpress](http://s.click.aliexpress.com/e/b4ZT5JAu) at $18 each. After buying from 4 different sellers, I found [the best rails at the "CNA Mechanical Parts Store"](http://s.click.aliexpress.com/e/b4ZT5JAu). I didn't even need to clean them - the blocks slide smoothly. Wonderful rails, highly recommended!

!!! danger "Stores to avoid"
    Don't buy rails from **"RDC Official Store"** or **"linkcnc Store"** on AliExpress. linkcnc sold me a used, damaged rail, shorter than ordered - it stayed stuck even after cleaning and lubricating. RDC started shipping MGN blocks in non-standard sizes.

**Cleaning and lubricating.** New rails won't be as smooth as they should be: they're coated at the factory with a protective oil that must be cleaned off (YouTube has videos on cleaning the carriage with WD-40). Then lubricate the rails and carriages with sewing machine oil or Teflon silicone grease - not thick grease, these are miniature rails. Ignore the "tilt the rail" smoothness test - it's wrong. You want them smooth, but not too smooth.

**[Cleaning an MGN12H carriage - video](http://www.youtube.com/watch?v=c53sa46C1qQ)** - a pretty good one. **Use a container so you don't lose the steel balls.** After reassembly there will be an empty space of one ball; that's normal.

Fixing the MGN rails can be very frustrating: they must be perfectly aligned and straight, or you'll get headaches. Don't start this project without tons of patience.

## Print samples

Most of my prints are made with [NOULEI silk filaments](http://s.click.aliexpress.com/e/dAY2Eky0) ([more NOULEI](http://s.click.aliexpress.com/e/l3V3Lymy)).

<div class="gallery" markdown>
![Print sample](../assets/img/img-d6fdeedb.jpg)
![Print sample](../assets/img/img-3b89a9ad.jpg)
![Print sample](../assets/img/img-c26a5d4b.jpg)
![Print sample](../assets/img/img-80122045.jpg)
![Print sample](../assets/img/img-24a5cfd9.jpg)
![Print sample](../assets/img/img-70bf4b94.jpg)
![Print sample](../assets/img/img-b04d706f.jpg)
![Print sample](../assets/img/img-75f2e65e.jpg)
![Print sample](../assets/img/img-14f01f82.jpg)
![Print sample](../assets/img/img-c394fdca.jpg)
</div>
