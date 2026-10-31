---
title: "Let there be COB LED light"
description: "After a long time using the LED strip to illuminate the printing area, I wondered how I could make the LEDs sexier, hidden, and without having to prin"
---

[← All updates](index.md){ .back-link }

# Let there be COB LED light

After a long time using the LED strip to illuminate the printing area, I wondered how I could make the LEDs sexier, hidden, and without having to print parts. Also, I was tired of seeing uneven light shining from the diffuser due to the large distance between each LED and LED.

So I started researching again and finally came up with another type of LED that more suitable for the BLV mgn Cube 3d printer - COB LED STRIP.

![](../../assets/img/posts/161f6da46095.jpg)

In COB Strip the light-emitting diodes are much smaller than the standard LED strip, which allows a larger amount of light-emitting diodes to be inserted into the strip. In a standard LED strip you will find about 60 LEDs per meter, whereas in COB you will find 360 LEDs per meter. This is 6x times more than a standard strip. This advantage makes it possible to create a uniform light diffusion. Another advantage is the fact that it's manufactured so that the LEDs have a layer of silicone that acts as a diffuser and helps to evenly distribute the light.

![](../../assets/img/posts/d85be1624523.jpg)

Also, using a smaller size diode allows the strip to be narrower. I chose an 8mm width. This allowed me to insert the COB strip into the extrusion channel easily. the COB strip can be cut every 50mm and the intensity of the light can be adjusted too.

The first two strips I ordered from different stores on Aiexpress made me disappointed and I almost gave up. Eventually, I found a [**reliable store**](https://s.click.aliexpress.com/e/_9i94Go) that sold quality COB strips. I chose from product listing options: **6000K Cool White** + **24v 360 LEDs** + **2 meters**. The strips came well packaged, met the specifications, and gave the feeling that this is indeed a high-quality COB strip.

I cut the COB strip according to the marking, (every 50mm) to the appropriate length with scissors and soldered two 26AWG wires. If you do not want or can't solder, you can use [**this fast connector**](https://s.click.aliexpress.com/e/_9II1fw) (choose the "For 8 mm PCB" option). I then threaded the stip easily into the upper aluminum extrusion channels. The electrical wires can be connected in 2 ways:

- Direct connection to a 24V PSU
- Duet Fan output - If you choose to connect the COB to a fan outlet, you will be able to control the COB strip intensity by using a slider in the duet's control panel.

In my case, I'm using Fysetc amazing [**Duet 3 6HC board**](https://s.click.aliexpress.com/e/_A1uWxz). so I had to define the lights as a FAN output by adding this line to the **Config.g** file:

M950 F2 C"out9" Q500   
M106 P2 S0.2 H-1 C"Lights"

Then I connected the COB LED's strip wires to **OUT9** port on the Duet3 6HC board.

<div class="gallery big" markdown>
![](../../assets/img/posts/84429b5e29c8.jpg)
![](../../assets/img/posts/8e97a60d4b2b.jpg)
![](../../assets/img/posts/aa711c3434be.jpg)
</div>

I must note that I am very pleased with the end result, the lighting is very efficient, looks good and I have the ability to control the intensity of the lighting through the panel. I could not have asked for anything better. I very much hope this will help those of you who want to add lighting to your printer.

In these pictures you can be impressed by the streams I installed, by the way, these are prints made with the help of [**BIQU's amazing H2 extruder**](https://s.click.aliexpress.com/e/_AgqcYp) (I will review it very soon).

<div class="gallery big" markdown>
![](../../assets/img/posts/518f9c92e692.jpg)
![](../../assets/img/posts/b0feeb49f5d7.jpg)
![](../../assets/img/posts/333dd3524b8e.jpg)
![](../../assets/img/posts/904c70ff95ec.jpg)
</div>
