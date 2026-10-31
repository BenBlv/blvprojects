---
title: "New front panel (beta)"
description: "Yes, this is a new front panel for the BLV mgn Cube printer."
---

[← All updates](index.md){ .back-link }

# New front panel (beta)

Yes, this is a new front panel for the BLV mgn Cube printer.

Right after I received my order from FYSETC and assembled the BLV mgn Cube 3D printer kit, I thought to myself: why not refresh the look of the front panel?

Designing the new front panel was not easy and it took me quite a while. As part of the new panel, I added a ball-jointed bracket for the LCD screen that FYSETC provided with the kit.

The look is unconventional, I know, but I sincerely hope you like it.

![](../../assets/img/posts/c9dabde9281f.jpg)

I rendered a few more pictures to help you see what the final panel looks like:

<div class="gallery big" markdown>
![](../../assets/img/posts/5798a2e08cb5.jpg)
![](../../assets/img/posts/895bc2ca7e32.jpg)
![](../../assets/img/posts/110613762ea1.jpg)
![](../../assets/img/posts/5074b726d315.gif)
</div>

The panel went through several versions before I allowed myself to release it as a beta. The following pictures show the prototype parts I printed on the Ender 3 V2. As you can see, the print quality is not amazing, but that was before I upgraded the printer with a BLV Ender 3 V2 kit.

<div class="gallery big" markdown>
![](../../assets/img/posts/77bd161156c3.jpg)
![](../../assets/img/posts/7c52612af3c7.jpg)
![](../../assets/img/posts/cd13d3cd8b2e.jpg)
![](../../assets/img/posts/d1d3946b9cc6.jpg)
</div>

Here is a short [video of the Neopixel animation](https://www.tiktok.com/@benleviblv/video/6985640380427406594).

For those of you who are not sure what the LEDs are for: the LED rings show the status of the printer, the hotend and the bed. This is done by an Arduino that monitors the communication line between the Duet board and the LCD. The first circuit was a bit complicated and not many people built it. Luckily, FYSETC released a [**super easy BLV PCB**](https://s.click.aliexpress.com/e/_AC5kIC) that saves all the trouble. It's an all-in-one board with a 24V regulator, an Arduino, a level shifter and all the parts needed to connect the Neopixels to your printer.

I used it since it is part of the FYSETC kit, and it took me less than 3 minutes to assemble. **Please note:** if you are using RepRap v3.xx, update your PCB with the [latest NeoPixelBLVmgn code](https://github.com/mule1972/NeoPixelBLVmgn). You will find a [flashing guide for the PCB](https://github.com/FYSETC/FYSETC-BLV-MGN-CUBE/tree/main/Firmware) in the FYSETC repository.

The assembly process is relatively simple. Some parts contain printed threads, so it is recommended to calibrate your printer first. I also created a 3D viewer to make it easy to understand where each part goes. [**Check out the 3D viewer**](https://a360.co/3BMm2xx).

<div class="gallery big" markdown>
![](../../assets/img/posts/8064018a3667.jpg)
![](../../assets/img/posts/433e6d5e0918.jpg)
</div>

### Download

Before you download the files, please understand that this is not the final version, so it is important to share your opinion with me. If you have any comments, insights or anything else on your mind, I would love to hear about it and improve the design.

The files are licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike license](http://creativecommons.org/licenses/by-nc-sa/3.0/).

The front panel STL files are included in the [BLV mgn Cube project files](../download-and-print.md), in the `STL files to print/Front Panel` folder. The beta Fusion 360 CAD file is no longer available.
