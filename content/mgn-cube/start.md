---
title: Start here - BLV mgn Cube
description: The first page of the BLV mgn Cube building guide - the build steps from start to finish, requirements and the project change log.
---

# Start here

This page is the road map of the build. Read it once before ordering anything, then follow the guide pages in order: [BOM](bom.md), [Download & Print](download-and-print.md), [Assembly](assembly.md), [Wiring](wiring.md) and [Calibrations](calibrations.md).

## What you need

- [x] A passion for 3D printing
- [x] 3D printing knowledge
- [x] Technical ability
- [x] Spare time
- [x] A budget

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

## Change log

| Date | Change |
| --- | --- |
| 29/10/22 | All broken links updated: screws, filaments, tools |
| 28/10/22 | Links updated |
| 28/10/22 | Huge BOM update + upgrades: new magnetic triple Z axis option (MJF parts) · new 8 mm magnetic Mic6 bed + silicone heater · new PET+PEI steel build plate setup · new ToolChanger E3D clone option (by Funssor) · new X-axis aluminium CNC tube 460 mm · new X-axis carbon fiber tube 460 mm · Klipper + RepRap new boards update · support for 48V TMC5160 drivers · 6 new hotend / extruder setup options |
| 06/06/22 | New panel files |
| 06/03/22 | Official support for **Klipper** ([download page](download-and-print.md)) |
| 24/01/22 | [New front panel beta testing](https://benlevi8.wixsite.com/blvprojects/post/new-front-panel-beta) |
| 04/01/22 | New step-by-step [assembly guide by David Husolo](https://www.ifixit.com/Device/BLV_MGN_Cube) |
| 18/07/21 | New step-by-step [assembly videos by FYSETC](https://www.facebook.com/groups/BenLevi/posts/883722929021911/) |
| 22/05/21 | New complete [BLV mgn Cube kit by FYSETC](https://benlevi8.wixsite.com/blvprojects/post/unboxing-fysetc-blv-mgn-cube-full-kit) |
| 24/03/21 | [New Discord channel](https://discord.com/invite/zY4GBfuzC4) |
| 06/03/21 | [BIQU H2 direct-drive bracket adapter](https://benlevi8.wixsite.com/blvprojects/post/the-new-biqu-h2-extruder-review) + fan duct |
| 13/02/21 | New [config + wiring diagram for Duet 3 6HC](https://www.facebook.com/groups/BenLevi/posts/796272867766918/) |
| 12/02/21 | [COB LED upgrade for the BLV mgn Cube](https://benlevi8.wixsite.com/blvprojects/post/let-there-be-cob-led-light) |
| 19/11/20 | [New PID procedure](https://www.facebook.com/groups/BenLevi/posts/746890766038462/) (Duet / RepRap) |
| 15/11/20 | [Trianglelab Matrix direct drive extruder adapter](https://benlevi8.wixsite.com/blvprojects/post/trianglelab-matrix-adapter-for-blv-cube-metal-kit) |
| 09/11/20 | [New Blind Joints frame for easy and accurate frame assembly](https://www.facebook.com/groups/BenLevi/posts/738763493517856/) |
| 30/08/20 | [New experimental BLTouch mount](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube) for the Metal Kit |
| 29/08/20 | [Metal Kit upgrade](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube) - replaces all the printed parts |
| 04/07/20 | New website for the project (after working on it Feb - Aug 2020) |
| 01/01/20 | [Silicone wiper upgrade](https://www.facebook.com/groups/BenLevi/posts/449121519148723/) (replaces the brass brush) |
| 13/09/19 | STEP files for the new twin fans |
| 09/08/19 | Powerful twin 4010 blower fan option (layer fan) for Bowden and direct drive |
| 03/08/19 | Updated Neopixel code by Claus Noack - works! · updated Neopixel wiring v2.2b |
| 21/07/19 | Optional frame reinforcement for taller Z-axis builds |
| 05/07/19 | Wiring diagram for 12V fans on a 24V system |
| 01/07/19 | Link to the full screws kit |
| 25/06/19 | Picture showing how to flip the belts at the rear |
| 11/06/19 | Hotend and heated bed PID tuning quick guide |
| 24/05/19 | Support for the Ender-3 bed size |
| 19/05/19 | Fixed typo in the purge message box |
| 12/05/19 | Quick frame wire holders (based on samella's design and thing:2576237) |
| 11/05/19 | E3D high temp 314 × 314 bed size |
| 10/05/19 | Fixed V6 locker - fan screw holes reduced to 2.7 mm |
| 01/05/19 | STL panels for PanelDue 4.3 and MKS TFT32 V4 (not supported by Duet) |
| 17/04/19 | Simplify3D profile v1.2 (added M81 S1 end script) · Neopixel wiring diagram (beta) and Mimasx code |
| 16/04/19 | Wiring diagram v3.2 · steppers setup guide for other stepper brands / batches |
| 04/04/19 | DXF (vector) files for the enclosure panels |
| 31/03/19 | Firmware: M80 PS_ON command on startup |
| 25/03/19 | Small fix: front panel - left plate for PanelDue 5 STL |
| 20/03/19 | DWG files for the bottom, rear and side panels |
| 19/03/19 | STEP (CAD) file for the direct drive setup |
| 18/03/19 | Wiring diagram fixed |
| 08/03/19 | Spitfire fan cover · front plate for Chimera (not suitable for layer fan / sensor) |
| 28/02/19 | Fixed Z-height calibration guide |
| 26/02/19 | Belt system V2 - use only flanged 623zz ball bearings + flip belt |
| 25/02/19 | Zesty Nimble front plate and block shield |
| 18/02/19 | Z height calibration guide |
| 17/02/19 | Renamed back the 8 mm / 12 mm mounts · walls dimensions PDF |
| 16/02/19 | BMG direct drive extruder (3 STL files + instructions) · big air scrubber - HEPA + carbon |
| 15/02/19 | Electronics schematics updated (dual extruder + buttons) |
| 09/02/19 | BOM calculator supports threaded rod length · block shield for BLTouch, 8 mm and 12 mm sensors · front panel for smartphone STL fixed |
| 07/02/19 | Printer size calculator (Excel file) and info |
| 06/02/19 | Printing orientation description + image |
| 03/02/19 | Jigs |
