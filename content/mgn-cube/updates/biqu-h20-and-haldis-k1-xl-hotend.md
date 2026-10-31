---
title: "BIQU H2O and Haldis K1-XL hotend"
description: "My first impressions, or shall I say unboxing, of a few hotend-extruder setups I'm testing. I'm sure it's going to be interesting."
---

[← All updates](index.md){ .back-link }

# BIQU H2O and Haldis K1-XL hotend

I want to share my first impressions, or shall I say unboxing, of a few hotend-extruder setups I'm testing. I'm sure it's going to be interesting. As you know, I try to be very thorough. Reaching full conclusions about an extruder or any particular component takes me about two full months of non-stop printing. Until then, I only allow myself to write about initial impressions.

### BIQU H2O - new extruder

I can sum up everything I write below about the [BIQU H2O](https://s.click.aliexpress.com/e/_AVr4sD) in one word: **beautiful**.

The new [BIQU H2O](https://s.click.aliexpress.com/e/_AVr4sD) arrived while I was busy working on the [BLV Metal Kit II](blv-metal-kit-ii-blv-carbon-new-stock-and-more.md), so it had to wait. If I had only known what I was missing. I have not been this impressed with an extruder in a long time.

![](../../assets/img/posts/b96530028ebf.jpg)

You're probably asking: **why do I even need a water-cooled extruder?**

I am not a fan of ABS printing, and most of the time I print PLA, PETG, flex and so on. But I have small children, and a closed enclosure keeps odors and particles away from them. Inside the enclosure the temperatures are much higher than without it, which can make it difficult to print common filaments. Water cooling is part of the solution.

Now let's get back to the [new H2O extruder](https://s.click.aliexpress.com/e/_AVr4sD). I'm sure you have already seen my [review of the original H2 extruder](the-new-biqu-h2-extruder-review.md). A lot of improvements went into the new extruder, and it looks like someone at BIQU did their homework. It is equipped with a high-temperature resistant motor (180°C) and stainless steel gears (according to the spec). I just wish they were **hardened** stainless steel. They added a MAX31865 module to support the included PT-100 sensor, which is a much more accurate temperature sensor at high temperatures. One more important thing: the bi-metal heatbreak is made of copper and titanium, not aluminum. As you know, aluminum can damage your water cooling system over time.

Another thing I really like is the sleek look. Everything is symmetrical, with clean lines. Very elegant! The RGB LEDs illuminating the water chamber are lovely. I almost forgot to mention that the [new H2O](https://s.click.aliexpress.com/e/_AVr4sD) is very small. It is even 11.6 mm smaller than the previous H2, and it weighs only 224 g. Check the photos below and notice the window that has been added for the hub wheel.

<div class="gallery big" markdown>
![](../../assets/img/posts/d9ffbee4c265.jpg)
![](../../assets/img/posts/6214508a5365.jpg)
![](../../assets/img/posts/c5e7006102fd.jpg)
![](../../assets/img/posts/2d038ccd262b.jpg)
</div>

Here's the full list of accessories that came in the package:

- BIQU yellow ducky - without it, I would probably have opened a dispute 🤣
- Full assembly manual, including firmware settings
- [BIQU H2O](https://s.click.aliexpress.com/e/_AVr4sD), fully assembled
- Copper-nickel plated heating block *(assembled)*
- Hardened steel 0.4 mm nozzle *(assembled)*
- Copper and titanium bi-metal heatbreak *(assembled)*
- Fittings / connectors for ID4/OD6 tubes
- KJH 04-M6 pneumatic connector for the PTFE tube
- High-quality PT-100 temperature sensor
- MAX31865 StepStick module (for the PT-100)
- JST connector and terminals
- Orange silicone sock
- 24V 70W heater cartridge
- Long motor cable
- RGB LED cable
- Screws
- All the needed tools

<div class="gallery big" markdown>
![](../../assets/img/posts/c0969eebd0e1.jpg)
![](../../assets/img/posts/858b78d8596a.jpg)
![](../../assets/img/posts/904dcdb8c233.jpg)
![](../../assets/img/posts/bfbf296e6ae5.jpg)
![](../../assets/img/posts/bb5159da726b.jpg)
</div>

#### So does it print well?

So far I'm getting fantastic results and I haven't had any problems. But I have to postpone my full conclusions until I reach at least 300 hours of printing. I used the adapter from the previous BIQU H2 and it works great. For now, I am absolutely in love with this extruder. BIQU, you got me!

### BIQU water cooling system

Then I realized I had thrown away all the water cooling systems from my old computers. Luckily, BIQU offered [a new 24V water cooling system](https://s.click.aliexpress.com/e/_AVr4sD) that is meant to suit the new [BIQU H2O](https://s.click.aliexpress.com/e/_AVr4sD). Even though I ordered it after the extruder, the water cooling system arrived first.

<div class="gallery big" markdown>
![](../../assets/img/posts/1370e542275f.jpg)
![](../../assets/img/posts/abdff05128b6.jpg)
![](../../assets/img/posts/41904fb48519.jpg)
![](../../assets/img/posts/b42390fef895.jpg)
</div>

The water cooling system was packed nicely, with all the needed accessories and even more. It includes all the tools you need, even a liquid funnel. The most important part is the pump. In this case it's the 12V [SysCooling P67D pump](https://s.click.aliexpress.com/e/_AFztCH), which is very reliable: 500 L/h max flow, ceramic bearings with a 50k-hour lifetime, a 25-27 dB sound level and G1/4 thread connectors. BIQU included three types of flexible tubes, brackets, double-sided stickers, tube diameter reducers (for other types of extruders), tools, connectors, screws and a power adapter.

Overall it looks good, but there is definitely room for improvement:

- **Buck converter** - the pump is 12V, so they used an [LM2596 buck converter](https://s.click.aliexpress.com/e/_A8xo7f) to convert 24V to 12V. The [LM2596](https://s.click.aliexpress.com/e/_A8xo7f) is a very cheap converter, and in my experience it tends to fail after prolonged use. On the other hand, it's very common, easy to find and costs only $3.
- **Spring clamps** - my friend David Husolo drew my attention to the fact that the kit uses clamps that are notorious for leaking. So I used a spare fitting from my PC water cooling system instead.
- **Coolant** - no coolant was provided with the system. If you decide to buy it, make sure to get a proper coolant.

<div class="gallery big" markdown>
![](../../assets/img/posts/b65b595a72c1.jpg)
![](../../assets/img/posts/f7abb25e52b1.jpg)
</div>

Please don't get me wrong, I really like this water cooling system. I once bought a water cooling system from another manufacturer, and a month later the pump stopped working. Of course, they refused to replace it. With the BIQU system I feel more confident, since I have had good experience with SysCooling pumps and I know BIQU has good customer service.

#### Final conclusion?

There is no way I am writing a final conclusion now. That will come only after testing the system for a long time, at least two months. I want to make sure there are no leaks, that the pump won't fail over time and that it really meets my requirements. Meanwhile, I can tell you that it works great, it is relatively quiet and the cooling is very effective.

### Haldis K1-XL new hotend with a unibody nozzle

I got one of the first early-bird units of the [new Haldis K1-XL hotend](https://s.click.aliexpress.com/e/_AeA133) for testing.

![](../../assets/img/posts/a5f1004f29ed.jpg)

Haldis is a relatively new manufacturer in the 3D printer market, but despite being new, their production quality stands out. Unlike a few other stores, they produce everything in-house. This gives them many advantages, including the ability to develop products themselves in a short time. The [new Haldis K1-XL hotend](https://s.click.aliexpress.com/e/_AeA133) is a good example of that. It has a unique unibody nozzle with an obvious advantage: the nozzle can be replaced quickly. How quickly, you ask? Just hit the play button below.

!yt 1uGRFWeUHuM

The K1-XL is the same size as a regular V6, but it has a unique structure. At first glance it looks like some sort of Dragon and Mosquito combination, but the truth is that it's very different. [The K1-XL has a bi-metal unibody nozzle](https://s.click.aliexpress.com/e/_AeA133), which means the whole nozzle and filament path, including the heatsink, can be replaced in a matter of seconds. Very convenient: no need to disassemble parts to clear a blockage, and no more fear of tightening the nozzle too hard or breaking the heatbreak. I love this approach. I was also surprised to find a very small, new type of temperature sensor, which is very refreshing. You can see it in the first picture below.

<div class="gallery big" markdown>
![](../../assets/img/posts/405829bb82b7.jpg)
![](../../assets/img/posts/88b734298de0.jpg)
</div>

As for the nozzle itself, it's a copper-nickel plated nozzle with an integrated heatsink on its upper part. At the bottom there is a thread, and the whole nozzle assembly simply screws into the thick heated cylinder. Note that the heated element is thick, and my doubts about heat dissipation turned out to be justified: the red heatsink does not seem to be sufficient. I think it will struggle with high temperatures. In the end, I had to use a [Gdstime 4020 dual ball bearing fan](https://s.click.aliexpress.com/e/_AOiAov) to get optimal results.

#### So what came in the package?

Unlike other manufacturers, there is no fancy packaging here. Everything came packed in bubble wrap and plastic bags. That could be because this is the first batch of the [Haldis K1-XL](https://s.click.aliexpress.com/e/_AeA133).

- [Main frame with an integrated thermistor](https://s.click.aliexpress.com/e/_AeA133) (thermistor type not specified)
- Ceramic heating element (no connectors?)
- 2 x bi-metal unibody 0.4 mm copper nickel-plated nozzles
- Orange silicone sock
- PTFE lockers/clips

<div class="gallery big" markdown>
![](../../assets/img/posts/1a6863751eb5.jpg)
![](../../assets/img/posts/96b117fe8dd4.jpg)
![](../../assets/img/posts/446ba3959b76.jpg)
</div>

Unfortunately, for this price I would expect fancier packaging, some tools like a socket screwdriver, a detailed manual, connectors and the right cables. The listing is also missing a lot of information about the heating element, the type of thermistor and the materials.

**An important note about something that bothers me: lack of information.** I recommend that every manufacturer selling 3D printer parts give full details on the material of each component, the sensor type, the heater type, the maximum temperature range, optimal slicer and firmware settings and so on. It helps customers decide whether to buy the product and how to use it. The less data you provide, the more concerns and failures your customers will have when using your products.

Anyway, let's continue.

Besides the insufficient heat dissipation, I noticed that the ceramic heater opening is too wide. Even after heating the block up to 260°C, when the metal had expanded, it was still too loose. This matters a lot, because there is no efficient heat transfer between the heating element and the heating block. The manufacturer suggested using thermal paste to fill the gap between them. I tried that, and the temperature jumps on the graph got smaller, but in my opinion it was still not enough.

**Overall, I think the K1-XL idea is beautiful and very refreshing.** The production quality is excellent. However, it needs rigorous testing of how everything works together, and a beta testing group, before it is released to customers. If I could advise the manufacturer, I would change a few things:

- Fix the gap between the ceramic heater and the metal (like the [Trianglelab CHC heater](https://s.click.aliexpress.com/e/_AE8CzL))
- Provide more details: a spec list, measurements and so on
- Add tools and connectors
- Make nice packaging that suits the price

Here is a nice photo of the [Trianglelab Rapido](https://s.click.aliexpress.com/e/_ALWey1), the [Haldis K1-XL](https://s.click.aliexpress.com/e/_AeA133), the [Orbiter V2](https://s.click.aliexpress.com/e/_ASClVX) and the [BIQU H2O](https://s.click.aliexpress.com/e/_AVr4sD). I know, the BIQU is so small, and yet it's both an extruder and a hotend.

![](../../assets/img/posts/82c875b87025.jpg)

#### Final conclusion?

Unfortunately, I had to take it off. I get unstable temperatures because of the ceramic heater issue, which can hurt print quality. I really hope this gets resolved, because I like the idea of a unibody nozzle.

### BIQU Hermit Crab - tool changer?

Samuel Gonzalez from the BLV Facebook group [shared his plan to adapt](https://www.facebook.com/groups/BenLevi/posts/979539799440223/) the [BIQU Hermit Crab tool changer](https://s.click.aliexpress.com/e/_A7ZUhT) to the BLV Cube 3D printer.

<div class="gallery big" markdown>
![](../../assets/img/posts/b6c7871b018e.jpg)
![](../../assets/img/posts/5267b17f1ad9.jpg)
![](../../assets/img/posts/f1d79ea78383.jpg)
</div>

Later he posted an awesome video of the [BIQU Hermit Crab](https://s.click.aliexpress.com/e/_A7ZUhT) tool changer on his BLV Cube printer:

!yt hwoDO2xHcK4

Inspired by him, I decided to order a [BIQU Hermit Crab](https://s.click.aliexpress.com/e/_A7ZUhT) for testing. So far I have only opened the box and done some dry testing, without mounting it on the printer. Many modifications are needed to fit it to the printer. I was very impressed with the reliability of the locking mechanism, but I have two main concerns that keep me from exploring this option further:

1. **The weight** - both the back plate and the front plate are made of aluminum, and they weigh quite a lot. I have a suggestion for BIQU that might make it much lighter: a lot of weight could be removed from both plates by using a thick PCB plate instead of aluminum, while keeping the central locking mechanism in aluminum. The bonus is that you would have even more space for electronic components.
2. **Offset** - with the Hermit Crab, the hotend must move 30 mm forward, and that's a lot.

As for the product itself, BIQU continues to deliver very high-quality products, great packaging and a detailed manual. Even a 10-year-old could put it together, with dad helping with the settings, which are also included in the manual.

<div class="gallery big" markdown>
![](../../assets/img/posts/2015f64c427e.jpg)
![](../../assets/img/posts/2fe60d60876b.jpg)
![](../../assets/img/posts/4f9e508061b5.jpg)
</div>

I hope you enjoyed reading. I promise to share my findings as I search for the perfect setup for the new BLV Cube update.

Sincerely,

Ben Levi

![](../../assets/img/posts/8e903eef96c1.png)
