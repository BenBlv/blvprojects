---
title: BLV mgn Cube
description: BLV mgn Cube, an open-source CoreXY 3D printer on MGN12 linear rails. Overview, features, build volume, 3D viewer, gallery and videos.
---

# BLV mgn Cube

<div class="hero" markdown>
<div markdown>
<span class="tag">Open-source 3D printer</span>

The BLV mgn Cube is an open front CoreXY 3D printer that runs on MGN linear rails. It was designed for accuracy, efficiency and print quality, with one simple goal: to let anyone build a good and reliable 3D printer.

<div class="stats"><span><b>1.78M</b>downloads</span><span><b>6.3M</b>views</span><span><b>29/10/22</b>last update</span></div>

[Start building](start.md){ .md-button .md-button--primary }
[Download the files](download-and-print.md){ .md-button }
</div>

![BLV mgn Cube 3D printer](../assets/img/blv-cubg-mgn-trans-min-7ea675f5.png){ .no-lightbox }
</div>

!yt FC9tIDhOgD4 | BLV mgn Cube at 9000 mm/s² acceleration and 500 mm/s

## Why build it

**Fast, reliable, accurate**
:   Most low and mid range printers move on linear bearings or Delrin wheels because they are cheap. The price is accuracy and reliability. MGN linear rails are stiffer, more precise and much smoother, so you can print faster without losing quality. That is why high-end printers use them. When I found affordable MGN rails on AliExpress, I decided to build around them.

**Rigid open structure**
:   The open front is as rigid as a closed cube but still gives easy access to the bed and the prints. A front belt tensioner makes maintenance easier. The design came out of many hours of simulation and physical stress tests.

**Accessible**
:   Every part is easy to source, print or make. The BOM has no expensive or rare machined parts. Most parts are printed or bought online or locally. You can also use your own electronics, as long as you know how to adapt the firmware.

**Open source**
:   The original CAD files (STEP) are included in the project files. You are welcome to modify, remix and improve them. If you do, please share your work with the community, mark the parts as "remixed" and link back to this project.

**Ready to print**
:   I spent many hours tuning the firmware and the Simplify3D slicing profile for this printer. After the build, upload the config files, load the profile and start printing.

**Modular**
:   Both the Z height and the bed size can grow. You only need longer extrusions and rails. The included CAD file helps you calculate the dimensions of a custom size.

**Easy to build?**
:   Installing the rails takes about 70% of the build time. It takes precision and a few hours of alignment, and it is worth every minute when the printer runs. To help, the project includes 3D animation videos, PDF guides, sketches and measurements.

**Balanced budget**
:   The BOM aims for the best value without cutting quality: a top 32-bit board, good stepper motors and reliable sensors. A 5" PanelDue touch screen is optional. You can save $80 and [use a phone or tablet instead](https://docs.duet3d.com/User_manual/Reference/Duet_Web_Control_Manual) with no loss of features.

## Upgrades

Two official upgrades were released after the original design. Their files are part of the project download.

- **[Metal Kit](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube)** - CNC aluminum parts that replace most of the printed parts.
- **Blind Joints frame** - a bracket-free frame that assembles in about 20 minutes.

<div class="gallery" markdown>
![BLV Metal Kit parts](../assets/img/all-kit-small-min-41b4c7e9.png)
![Blind Joints frame](../assets/img/blv-frame-blind-joints-86644b47.png)
</div>

## Features

<div class="feature-list" markdown>

- **RepRap** and **Klipper** firmware support
- Input Shaper (Klipper)
- **9000** mm/s² acceleration and **500** mm/s with Klipper
- Efficient cooling system
- SuperSlicer and Simplify3D profiles
- HEPA and carbon air scrubber
- Rigid aluminum open front frame
- Dual extrusion option
- Front belt tensioners
- Mesh auto-leveling
- Internal LED lighting
- Blind Joints frame for fast assembly
- **Triple Z** for true bed leveling
- MGN12H linear rails
- High resolution X/Y stepper motors
- Full firmware configuration included
- Bed 300 × 300 mm, height 365, 465 or 565 mm
- Duet WiFi, Duet 3 or FYSETC Spider v2.2 (Klipper)
- TMC5160 high voltage 48V driver support
- Web interface from phone, tablet or desktop
- Electronics mounted at the back
- CNC aluminum parts with the [Metal Kit](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube)
- Open-source CAD files
- A large community with many remixes and upgrades

</div>

## Build volume

- **Bed:** 300 × 300 mm (standard) or 350 × 350 mm (custom)
- **Height:** 365, 465, 565 or 665 mm

![Build volume options](../assets/img/build-volume-min-bb267165.png){ width="420" }

## Explore in 3D

The online viewers let you explore, measure and isolate parts in the browser:

- [Full printer](https://a360.co/2FLRqSa)
- [Frame only](https://a360.co/2DDDBn4)
- [Panels and walls only](https://a360.co/2JGlYZ4)

## Gallery

<div class="gallery" markdown>
![BLV mgn Cube](../assets/img/img-6402205e.gif)
![BLV mgn Cube](../assets/img/img-e2264cb8.jpg)
![BLV mgn Cube](../assets/img/img-c9976482.jpg)
![BLV mgn Cube](../assets/img/img-f9261a09.jpg)
![BLV mgn Cube](../assets/img/img-1ab3e774.jpg)
![BLV mgn Cube](../assets/img/img-332c64f5.jpg)
![BLV mgn Cube](../assets/img/img-e9074c24.jpg)
![BLV mgn Cube](../assets/img/img-c4eea3e7.jpg)
![BLV mgn Cube](../assets/img/img-c7e88303.jpg)
![BLV mgn Cube](../assets/img/img-10d38c05.jpg)
![BLV mgn Cube](../assets/img/img-0a61612d.jpg)
![BLV mgn Cube](../assets/img/img-03cd3a6f.jpg)
![BLV mgn Cube](../assets/img/img-be309c54.jpg)
![BLV mgn Cube](../assets/img/img-2596d52c.jpg)
![BLV mgn Cube](../assets/img/img-8fa7f536.jpg)
![BLV mgn Cube](../assets/img/img-4c0f3203.jpg)
![BLV mgn Cube](../assets/img/img-172e4791.jpg)
![BLV mgn Cube](../assets/img/img-2d31fa9b.jpg)
![BLV mgn Cube](../assets/img/img-54769fdb.jpg)
![BLV mgn Cube](../assets/img/img-2e74cb6e.jpg)
![BLV mgn Cube](../assets/img/img-686fe104.jpg)
![BLV mgn Cube](../assets/img/img-0d50f68f.jpg)
![BLV mgn Cube](../assets/img/img-dfb71fce.jpg)
![BLV mgn Cube](../assets/img/img-f9742585.jpg)
![BLV mgn Cube](../assets/img/img-7cf291ee.jpg)
![Online 3D viewer](../assets/img/3d-viewer-6146ecaf.jpg)
</div>

## Printer videos

!yt exeUR__tco8 | Printing with gold silk PLA
!yt -7xCHPYShQg | Printing
!yt agu6ReJOmm8 | Print sample

## Community videos

!yt Spc1cCTLFzs | Benchy with Prusament PLA
!yt N_bD6kgxAEA | Johnny Hallyday print
!yt 9-EyQRFcamc | BLV MGN Cube
!yt UkFa6o_Uuig | Resonance test at 100 mm/s, Metal Kit with NF Crazy Plus
!yt rSSUHyvyTfQ | BLV mgn Cube community build
!yt dt3wfzbeUKs | Mandalorian helmet, part 1
!yt 3Y3C2JK-PUg | BLV mgn Cube 3D printer
!yt ItAonH9IVy0 | Triple Z bed leveling
!yt SxxE28ZN7O8 | Torture test
!yt MtD9szFlxQU | SE edition
!yt jo5cHnJwMuU | Printing TPU
!yt es9ltH34RBk | Print sample
