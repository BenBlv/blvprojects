---
title: Start here - BLV mgn Cube
description: The road map of the BLV mgn Cube build, from preparation to the first print.
---

# Start here

This page is the road map of the build. Read it once before ordering anything, then follow the guide pages in order: [BOM](bom.md), [Download & Print](download-and-print.md), [Assembly](assembly.md), [Wiring](wiring.md) and [Calibrations](calibrations.md).

!!! tip "Before you begin"
    This is not a kit you assemble in an evening. Expect some 3D printing experience, basic electronics skills, a few weekends of work and a mid-range budget. In return you get a printer you understand down to the last screw.

## The build, step by step

1. **Prepare.**
   Read the project description and the linked material, watch the 3D animations and explore the printer in the [3D viewer](index.md#explore-in-3d). Make sure you understand the structure before you start.
2. **Get the parts.**
   Waiting for parts is the most frustrating stage. Check that you have everything in the [BOM](bom.md), plus spare T-nuts and screws. If you use your own electronics, make sure you know how to configure the firmware for your board.
3. **Build.**
   Prepare the tools and use a good corner alignment tool. A precise frame is the basis of good prints. The printed jigs make the assembly much easier. Tap the holes in the extrusion ends and check whether they take M5 or M6 screws, since this depends on the extrusion maker. Take your time with the rails. This [short video by 3D Distributed](http://youtube.com/watch?v=iX0U1ADH0MY) shows an easy way to align parallel rails. Reward yourself when the rails are in, you deserve it.
4. **Install the electronics.**
   Check every connection against the [wiring diagram](wiring.md), avoid shortcuts and use the right tools and parts. Connect the power cable last.
5. **Test and calibrate.**
   Update the Duet WiFi to the latest firmware, copy the provided configuration to the micro SD card, insert it and power up. The Mini IR sensor should blink 4 times at power-up. Check the endstops before you move any axis. When you home the printer it should move left and then to the rear. If it doesn't, check the motor wiring and the configuration. Calibrate the Z height and check the temperature readings. Run a **PID calibration** for both the bed and the hotend. This step is essential, without it prints will fail. When everything looks right, load filament and print a calibration cube. Details are on the [Calibrations](calibrations.md) page.
6. **Print and maintain.**
   Grease the rails with a synthetic PTFE grease or sewing machine oil. Keep the rails clean and the belts tight. Clean the PEI plate with alcohol after every print. If you built the air scrubber, replace the HEPA filter when needed.
7. **Share your build.**
   I would really appreciate an "I made one" photo. Knowing the project helped you build your own printer makes all the hours worth it.
8. **Remix and share.**
   There are many ways to make this printer better, which is why the source files are included. Improve it and share your remixes with the community.
