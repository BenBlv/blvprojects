---
title: "Trianglelab Matrix adapter for the Metal Kit"
description: "Hello my friends, for a long time I have been considering whether to purchase the E3D HEMERA extruder. To my great joy, a new extruder from Trianglela"
---

[← All updates](index.md){ .back-link }

# Trianglelab Matrix adapter for the Metal Kit

Hello my friends, for a long time I have been considering whether to purchase the [E3D HEMERA](https://e3d-online.com/products/e3d-hemera-direct-kit-1-75mm) extruder. To my great joy, a new extruder from Trianglelab appeared - [**MATRIX**](https://s.click.aliexpress.com/e/_ANs1Ql) , which is identical in most of its properties to HEMERA but costs much less and high quality.

![](../../assets/img/posts/80b57e9f9b02.jpg)

The main reasons why I so wanted to try the Matrix are:

- **Short filament path** - The distance between the wheels to the nozzle is 26mm. This is a huge advantage when printing soft and flexible materials. Beyond that the retraction distance is significantly smaller (mine set ot 0.6mm). Also, a much lower value can be entered at [pressure advance](https://docs.duet3d.com/)feature on Reprap FW which mines way more accurate extrusions and faster printing experience.
- **Bi-metal heatbreak** - The combination of two different materials in the heatbreak creates a state of very efficient thermal separation compared to other extruders. The hitbreak tube is made of two different materials with different thermal conductivity. This creates an excellent buffer between the heat block and the part that should always be cold - the dual gears that push the filament inwards.

<div class="gallery big" markdown>
![](../../assets/img/posts/c77c0e1099eb.jpg)
![](../../assets/img/posts/f869665b344d.jpg)
![](../../assets/img/posts/77ceabdc12c3.jpg)
</div>

Of course I did not refer to dual gear drive with **1:3 gear proportion** and other features, because it has already become almost standard. The only downside of this setup is the weight. For me, the total weight of the Hotend and extruder was about 360 grams. It is **heavier** than other extruders, on the other hand the performance can be very surprising..

As you can see, I was immediately tempted and purchased the new MATRIX extruder. After a pretty long time using the Matrix extruder with my [**BLV mgn Cube**](../index.md) 3d printer (upgraded to [**Metal kit**](new-metal-kit-upgrade-blv-mgn-cube.md)), I feel quite comfortable writing an objective opinion about it.

The new extruder came well packaged and all components are marked in separate bags with detail stickers. In addition, a page was attached detailing the entire contents of the package, including a QR code that refers to a [neat assembly guide](https://drive.google.com/drive/folders/1K_Jj4JfczDlKiNnwk-SYakOIQqm4zllD). They even added a Matrix step (CAD) file in case anyone would be interested in modeling mounts and extras. I must note that Trianglab always attaches all the necessary components to their products as well as detailed instructions. all included, whether it's shrinks, adpaters, wires or just zipties. **Well done**!

<div class="gallery big" markdown>
![](../../assets/img/posts/0f489b86bcbb.jpg)
![](../../assets/img/posts/3b53b1c2a5ed.jpg)
![](../../assets/img/posts/2e251dc7bf6e.jpg)
![](../../assets/img/posts/a25015adeb38.jpg)
</div>

This is what it looks like shortly before mounting on the X-axis:

<div class="gallery big" markdown>
![](../../assets/img/posts/8997ec327334.jpg)
![](../../assets/img/posts/bd28c8dc3c11.jpg)
![](../../assets/img/posts/d0b27ce5a69a.jpg)
![](../../assets/img/posts/7dfa85ec318d.jpg)
</div>

### Print test

I guess by this point you already want to see print results. So for those who can not resist, I added here some pictures of objects printed with the Trianglelab Matrix extruder. By the way, I really like print this cube, it's quite funny that it comes out more accurate when printed using a BLV printer.

<div class="gallery big" markdown>
![](../../assets/img/posts/b1aeff72c6e8.jpg)
![](../../assets/img/posts/d65d01e1fa1a.jpg)
![](../../assets/img/posts/4b49a3aef435.jpg)
</div>

### Installing the extruder

Although the [**MATRIX**](https://s.click.aliexpress.com/e/_ANs1Ql)is very similar to the HEMERA, the dimensions are slightly different so I preferred to create an adapter for the BLV Metal Kit. When I created the adapter, I referred to the nozzle location and tried to find the most optimal location. Some of the considerations were maintain a proper center of gravity and not lose of the build plate size.

<div class="gallery big" markdown>
![](../../assets/img/posts/60aba64e7403.jpg)
![](../../assets/img/posts/c70f4d2b93f6.jpg)
![](../../assets/img/posts/e74ca9786fc7.jpg)
</div>

The MATRIX adapter is [**available for download below**](#viewer-6bdjg). I uploaded also the source file (step file), so that it will be easy for you to add features and make changes as you wish. In order to assemble the adapter you will need the following components:

- [BLV mgn Cube 3dp printer](../index.md)+ [Metal Kit](new-metal-kit-upgrade-blv-mgn-cube.md) upgrade
- [BLV Matrix adapter](#viewer-d47dn) - printed from **PETG/ASA/ABS** with **80%+ infill**.
- [Trianglelab Matrix extruder](https://s.click.aliexpress.com/e/_ANs1Ql)
- 3 X M3 8mm Hex Flat head screws
- 1 X M3 16mm Hex Flat head screws
- 2 X M3 8mm Hex Socket head screws
- 3 X M3 16mm Hex Socket head screws
- 3 X M3 washers

In order to assemble the adapter, use these instructions:

![](../../assets/img/posts/a900ac4f27c9.jpg)

**Layers fan**

I temporarily chose to use a [James Tongue](https://www.thingiverse.com/thing:4042492/files) fan as a layered fan, but I changed the bracket to fit the Trianglelab Matrix extruder so the nozzle would be placed right in the middle. the modified fan mount available in the download section below.

### Download Section

BLV matrix v1.1.5.zipDownload ZIP • 179KB

File description

- BLV matrix adapter for metal kit.step - adapter source file.

- BLV matrix adapter for metal kit.stl - This is the matrix adapter file to printed.
- BLV matrix fan adapter.step - If you are using [James Tongue](https://www.thingiverse.com/thing:4042492/files) fan bracket, print this file.
- BLV matrix fan adapter.stl - Fan mount source file.

### Changes to be made in FIRMWARE (RRF3):

To use the MATRIX you have to Change the following lines in the Config.g file on your Duet. please mind that the following lines are for RRF3 version.

- **Thermistor:** change the Thermistor setting to match the matrix thermistor. under **M308** line chnage the T, B and C value to this: **T107537 B4725 C7.06e-8**
- **Esteps:** for me the default Esteps according Trianglelab manual were wrong, so i calibrated it and found that the most accurate setting for my matrix extruder. i advice you to calibrate your extruder too. for me i had to change the esteps value to: **E324.214** under **M92** line.
- **Stepper Drive**: Invert your Extruder drive direction by changing the S value to S0 or S1 under M569 line.
- **Probe position**: For the Mini IR sensor the offset values under G31 line are: **X16.795 Y25.4IMPORTANT**: please re-calibrate your Z offset right after changing the hotend.

**More prints**

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

My personal experience with the new Matrix extruder has been very positive. I highly recommend the extruder to anyone who wants an extruder that has all in one package. Although it is quite heavy, you gain consistent extrusion, short retraction and excellent printing experience. If I could change anything, then I would start with a small stepper as Nema 14 combined with high gear ratio. but over all i really like it.

**Note**: i will probably test the **BX H2 extruder** next (219g) with 1:7 ratio gear.

**Links:**

[Trinanglelab Matrix extruder](https://s.click.aliexpress.com/e/_ANs1Ql)
