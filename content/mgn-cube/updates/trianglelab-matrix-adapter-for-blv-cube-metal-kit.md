---
title: "Trianglelab Matrix adapter for the Metal Kit"
description: "For a long time I considered buying the E3D Hemera extruder. Then Trianglelab released the Matrix, which is similar to the Hemera but costs much less."
---

[← All updates](index.md){ .back-link }

# Trianglelab Matrix adapter for the Metal Kit

For a long time I have been considering whether to buy the [E3D Hemera](https://e3d-online.com/products/e3d-hemera-direct-kit-1-75mm) extruder. To my great joy, a new extruder from Trianglelab appeared: the [**Matrix**](https://s.click.aliexpress.com/e/_ANs1Ql). It is identical to the Hemera in most of its properties, but it costs much less and is still high quality.

![](../../assets/img/posts/80b57e9f9b02.jpg)

The main reasons I wanted to try the Matrix so much are:

- **Short filament path.** The distance between the drive wheels and the nozzle is 26mm. This is a huge advantage when printing soft and flexible materials. Beyond that, the retraction distance is significantly smaller (mine is set to 0.6mm). A much lower value can also be used for the [pressure advance](https://docs.duet3d.com/) feature in RepRap Firmware, which means more accurate extrusion and faster printing.
- **Bi-metal heatbreak.** The heatbreak tube is made of two different materials with different thermal conductivity. This creates very efficient thermal separation compared to other extruders, and an excellent buffer between the heat block and the part that should always stay cold: the dual gears that push the filament in.

<div class="gallery big" markdown>
![](../../assets/img/posts/c77c0e1099eb.jpg)
![](../../assets/img/posts/f869665b344d.jpg)
![](../../assets/img/posts/77ceabdc12c3.jpg)
</div>

I'm not even counting the dual gear drive with a **1:3 gear ratio** and the other features, because they have almost become standard. The only downside of this setup is the weight. For me, the total weight of the hotend and extruder was about 360 grams. It is **heavier** than other extruders, but on the other hand, the performance can be very surprising.

As you can see, I was immediately tempted and bought the new Matrix extruder. After using it for a pretty long time on my [**BLV mgn Cube**](../index.md) 3D printer (upgraded with the [**Metal Kit**](new-metal-kit-upgrade-blv-mgn-cube.md)), I feel quite comfortable writing an objective opinion about it.

The new extruder came well packaged, with all components in separate bags marked with detailed stickers. A page listing the entire contents of the package was also included, with a QR code that leads to a [neat assembly guide](https://drive.google.com/drive/folders/1K_Jj4JfczDlKiNnwk-SYakOIQqm4zllD). They even added a Matrix STEP (CAD) file in case anyone wants to model mounts and extras. I must note that Trianglelab always includes all the necessary components with their products, as well as detailed instructions. Everything is included, whether it's heat shrinks, adapters, wires or just zip ties. **Well done!**

<div class="gallery big" markdown>
![](../../assets/img/posts/0f489b86bcbb.jpg)
![](../../assets/img/posts/3b53b1c2a5ed.jpg)
![](../../assets/img/posts/2e251dc7bf6e.jpg)
![](../../assets/img/posts/a25015adeb38.jpg)
</div>

This is what it looks like shortly before mounting it on the X axis:

<div class="gallery big" markdown>
![](../../assets/img/posts/8997ec327334.jpg)
![](../../assets/img/posts/bd28c8dc3c11.jpg)
![](../../assets/img/posts/d0b27ce5a69a.jpg)
![](../../assets/img/posts/7dfa85ec318d.jpg)
</div>

### Print test

I guess by now you already want to see some print results. So for those who can't resist, here are some pictures of objects printed with the Trianglelab Matrix extruder. By the way, I really like printing this cube. It's quite funny that it comes out more accurate when printed on a BLV printer.

<div class="gallery big" markdown>
![](../../assets/img/posts/b1aeff72c6e8.jpg)
![](../../assets/img/posts/d65d01e1fa1a.jpg)
![](../../assets/img/posts/4b49a3aef435.jpg)
</div>

### Installing the extruder

Although the [**Matrix**](https://s.click.aliexpress.com/e/_ANs1Ql) is very similar to the Hemera, the dimensions are slightly different, so I preferred to design an adapter for the BLV Metal Kit. When I designed the adapter, I focused on the nozzle position and tried to find the optimal location. Some of the considerations were keeping a proper center of gravity and not losing build plate area.

<div class="gallery big" markdown>
![](../../assets/img/posts/60aba64e7403.jpg)
![](../../assets/img/posts/c70f4d2b93f6.jpg)
![](../../assets/img/posts/e74ca9786fc7.jpg)
</div>

The Matrix adapter is available in the **download section** below. I also uploaded the source file (STEP file), so you can easily add features and make changes as you wish. To assemble the adapter, you will need the following components:

- [BLV mgn Cube 3D printer](../index.md) with the [Metal Kit](new-metal-kit-upgrade-blv-mgn-cube.md) upgrade
- BLV Matrix adapter, printed in **PETG/ASA/ABS** with **80%+ infill**
- [Trianglelab Matrix extruder](https://s.click.aliexpress.com/e/_ANs1Ql)
- 3 x M3 8mm hex flat head screws
- 1 x M3 16mm hex flat head screw
- 2 x M3 8mm hex socket head screws
- 3 x M3 16mm hex socket head screws
- 3 x M3 washers

Follow these instructions to assemble the adapter:

![](../../assets/img/posts/a900ac4f27c9.jpg)

### Layer fan

For now I chose to use a [James Tongue](https://www.thingiverse.com/thing:4042492/files) fan duct as the layer fan, but I modified the bracket to fit the Trianglelab Matrix extruder so the nozzle sits right in the middle. The modified fan mount is available in the download section below.

### Download section

File: BLV matrix v1.1.5.zip (ZIP, 179KB)

File description:

- BLV matrix adapter for metal kit.step - adapter source file
- BLV matrix adapter for metal kit.stl - the Matrix adapter file to print
- BLV matrix fan adapter.step - fan mount source file
- BLV matrix fan adapter.stl - if you are using the [James Tongue](https://www.thingiverse.com/thing:4042492/files) fan bracket, print this file

### Firmware changes (RRF3)

To use the Matrix, you have to change the following lines in the config.g file on your Duet. Please mind that these lines are for RRF3.

- **Thermistor:** change the thermistor settings to match the Matrix thermistor. In the **M308** line, change the T, B and C values to: **T107537 B4725 C7.06e-8**
- **E-steps:** for me, the default e-steps from the Trianglelab manual were wrong, so I calibrated my Matrix extruder to find the most accurate setting. I advise you to calibrate your extruder too. I had to change the e-steps value in the **M92** line to: **E324.214**
- **Stepper driver:** invert your extruder drive direction by changing the S value to S0 or S1 in the M569 line.
- **Probe position:** for the mini IR sensor, the offset values in the G31 line are: **X16.795 Y25.4**

**Important:** re-calibrate your Z offset right after changing the hotend.

### More prints

<div class="gallery big" markdown>
![](../../assets/img/posts/90cff1588259.jpg)
![](../../assets/img/posts/a70a4f607332.jpg)
![](../../assets/img/posts/44cb27a33865.jpg)
![](../../assets/img/posts/1eb2674c8707.jpg)
![](../../assets/img/posts/1fe357f9b5bc.jpg)
![](../../assets/img/posts/b1aeff72c6e8.jpg)
![](../../assets/img/posts/d65d01e1fa1a.jpg)
</div>

### Final conclusion

My personal experience with the new Matrix extruder has been very positive. I highly recommend it to anyone who wants an all-in-one extruder package. Although it is quite heavy, you get consistent extrusion, short retractions and an excellent printing experience. If I could change anything, I would start with a smaller stepper, such as a NEMA14, combined with a higher gear ratio. But overall, I really like it.

**Note:** I will probably test the **BIQU H2 extruder** (219g) with its 7:1 gear ratio next.

Get the [Trianglelab Matrix extruder](https://s.click.aliexpress.com/e/_ANs1Ql) on AliExpress.
