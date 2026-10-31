---
title: "BIQU H2 extruder review"
description: "After a whole month of carefully testing the BIQU H2 extruder on my BLV mgn Cube 3D printer, I feel confident sharing my conclusions about it."
---

[← All updates](index.md){ .back-link }

# BIQU H2 extruder review

After a whole month of carefully testing the [**BIQU H2 extruder**](https://s.click.aliexpress.com/e/_A5gltu) on my [**BLV mgn Cube 3D printer**](../index.md), I feel pretty confident writing my conclusions about BIQU's new [H2 extruder](https://s.click.aliexpress.com/e/_A5gltu). I promise you that I have tried hard to write a balanced and honest review. After all, no one pays me to write anything.

### So why is everyone excited about the new extruder?

Well, the [BIQU H2 extruder](https://s.click.aliexpress.com/e/_A5gltu) actually resembles the E3D Hemera extruder, only with a smaller stepper and a higher gear ratio, at half the weight of the Hemera. Looking at the [H2 extruder](https://s.click.aliexpress.com/e/_A5gltu), it is clear that the main principle behind its design was to produce a direct drive at the lowest possible weight. Here is a picture that shows how small the H2 extruder is compared to the [Trianglelab Matrix](https://s.click.aliexpress.com/e/_ANs1Ql) that [I reviewed](trianglelab-matrix-adapter-for-blv-cube-metal-kit.md) before:

![](../../assets/img/posts/4991de637c1e.jpg)

Sure, I guess you can find a number of DIY extruders under 170g. But how many of them are actually made of aluminum and will survive inside the enclosure? And how many will not wear out fast because they are not made of printed parts? Anyway, I'm glad someone saw the potential and managed to reach such an impressive specification. And speaking of the specification:

BIQU H2 specs:

- Direct drive extruder, ratio 7:1, torque 770mN.m
- Size: 60x35x35mm
- Weight: **219g** including hotend and fan (mine was 225g)
- Max pushing force: 7.5kg (I was only able to verify 4.62kg)
- Max temperature: 260ºC, upgradeable to 500ºC
- NEMA14 1.8º stepper motor
- Nominal e-steps: 932 steps/mm for a 16x setup (after calibration: 917.444)
- NTC 3950 100k thermistor and a 24V heater

It wasn't cheap. [$100 for the extruder](https://s.click.aliexpress.com/e/_A5gltu) is definitely expensive. But when I bought it, there was no reliable direct drive alternative that weighed less than the H2. If there were alternatives in serial production, I guess the price would have been much lower. After a rather short wait, the package arrived and I was very excited to open it. The extruder came in an airtight custom box, lying comfortably in a soft material that kept it from being damaged. Very neat. It came with instructions and a separate bag that contained all the other accessories and tools. Inside the package you will find:

- BIQU H2 extruder
- 3510 24V fan with a long cable
- 35mm fan grill
- NTC 3950 100k thermistor
- 24V 40W heater with thick cable insulation
- Stepper motor cable
- Heat block silicone sock
- Yellow duck (my favorite item in this order)
- Screws and tools
- Additional order: all-metal heatbreaks for higher temperature printing, 1 x 303 stainless steel heatbreak and 1 x titanium heatbreak

<div class="gallery big" markdown>
![](../../assets/img/posts/9c0569e73d23.jpg)
![](../../assets/img/posts/23b14af92785.jpg)
![](../../assets/img/posts/4329b6920c45.jpg)
</div>

I must say I was very impressed with the build quality of the extruder. Everything is made of aluminum and looks good. The parts have been smoothed, with no chips, no dirt and no visual defects. I was sure the gears were made of glass-filled plastic, but I was pleasantly surprised when I realized they were actually metal gears. However, I found some issues that bothered me a lot, and I had to fix them before the first use. Below you can read more about the changes I made. Here are some pictures of the extruder before I started disassembling and testing it.

<div class="gallery big" markdown>
![](../../assets/img/posts/63b62818278f.jpg)
![](../../assets/img/posts/db84295f222f.jpg)
![](../../assets/img/posts/93a9a0cc0bd7.jpg)
![](../../assets/img/posts/f3a5dc93bf0e.jpg)
</div>

This is what it looks like after removing the fan and exposing the entire **7:1 gear mechanism**:

<div class="gallery big" markdown>
![](../../assets/img/posts/3676da624f41.jpg)
![](../../assets/img/posts/d344779280f2.jpg)
![](../../assets/img/posts/34fb527d8527.jpg)
</div>

The heat block of the extruder is actually a regular aluminum heat block from which large pieces were shaved and drilled out, probably to save weight. The heatbreak is a standard size but has a D profile, and it is locked with two set screws. The first photo shows the all-metal heatbreaks. In the last photo, I tried a regular heat block and it worked fine.

<div class="gallery big" markdown>
![](../../assets/img/posts/551e6ac36229.jpg)
![](../../assets/img/posts/aa35f0005c8b.jpg)
![](../../assets/img/posts/38d7d2740bf2.jpg)
![](../../assets/img/posts/7ba7f1573966.jpg)
![](../../assets/img/posts/0ff78a6348d0.jpg)
![](../../assets/img/posts/0f57b1bb1701.jpg)
</div>

Before you assemble the heat block, I recommend calibrating your extruder e-steps. I found a huge difference between BIQU's recommended e-steps (**932**) and the calibrated e-steps for my H2 extruder (**917.444**). This is also a good moment to check that the motor direction is correct.

One of the first modifications I made was to change the direction of the heat block. I wanted the narrow part to face the front of the printer so I could use an efficient cooling solution. I also didn't like the inner finish of the original BIQU nozzle (first photo), so I replaced it with an [amazing quality nozzle](https://s.click.aliexpress.com/e/_ANF7sA) that I had purchased from Mellow's store. To lock the nozzle in place, I used a wrench and inserted an Allen key into the heater hole. This way I tightened the nozzle without damaging the exterior finish of the block (second photo).

<div class="gallery big" markdown>
![](../../assets/img/posts/abdc7af7baee.jpg)
![](../../assets/img/posts/bb3c9854edff.jpg)
![](../../assets/img/posts/95c3baa5c62f.jpg)
</div>

After changing the heat block orientation and the nozzle, I started taking care of something else that was bothering me. I may be wrong, but it seems that the gears are made of black coated steel that can rust over time due to moisture in the air. I also noticed that BIQU doesn't grease the gears before sending them out to customers, and I found that very disturbing. Applying a little grease to the gear system makes it work better, helps the gears last longer and protects them from moisture in the long run. Luckily, I had ordered the SuperPINDA from Prusa to test its accuracy against the mini IR sensor, and I added 5 pcs of Prusa grease to that order. I found it to be an excellent grease, even for linear rails. So I spread out a piece of paper, carefully disassembled the gears and gently greased all the components. When greasing the gears, **take care not to grease the wheels that pull the filament**. Any oil on them can cause an extrusion failure.

<div class="gallery big" markdown>
![](../../assets/img/posts/ed49d3506b19.jpg)
![](../../assets/img/posts/8e02bdff0a44.jpg)
![](../../assets/img/posts/9181c991dcf1.jpg)
![](../../assets/img/posts/02bcb4060907.jpg)
</div>

Immediately after assembling everything, I had to disassemble it all again because I found another annoying issue. A cable must be connected to the extruder stepper motor, and someone chose to assemble the H2 motor so that the cable socket faces down. That is a critical mistake. At some point the cable may come loose, get stuck in the part you are printing and destroy the whole print. To fix it, disassemble the extruder and take out the two tiny M3 screws that fix the extruder body to the stepper motor. Rotate the stepper motor 180 degrees and tighten the screws again. Please mind that the threads are short and can be easily stripped, so screw them in gently and not too tight.

<div class="gallery big" markdown>
![](../../assets/img/posts/7a5fa4d06419.jpg)
![](../../assets/img/posts/13464513762f.jpg)
![](../../assets/img/posts/6f5de4c585fa.jpg)
</div>

After several hours of design work and simulations, I was able to get a bracket strong enough to support the H2 extruder that also fits the [metal kit](new-metal-kit-upgrade-blv-mgn-cube.md) of my [**BLV mgn Cube 3D printer**](../index.md). Please note that I added spring washers to the long H2 extruder screws. After a few dozen hours of printing, I noticed that I had to re-tighten the long screws that hold all the H2 components together, and adding spring washers fixed the issue completely. I did a number of tests using dual 3510 ball bearing blowers, but the airflow was just ridiculously weak. I ended up using a [powerful dual ball bearing 5015 blower fan](http://s.click.aliexpress.com/e/cTnlOmKc), which gave me fantastic results. Feel free to download the bracket files. I included both the STL file and the STEP (CAD) file, so you can easily make changes as you wish:

![](../../assets/img/posts/4b290ffbadc8.jpg)

The bracket is included in the [BLV mgn Cube project files](../download-and-print.md): the STL files are in `STL files to print/Biqu H2 extruder adapter For Metal kit` and the STEP files are in `open source/Biqu H2 adapter For Metal kit`.

The files are licensed under the Creative Commons - Attribution - Non-Commercial - Share Alike license.

<div class="gallery big" markdown>
![](../../assets/img/posts/46e928aa0cdf.jpg)
![](../../assets/img/posts/87fc828b711a.jpg)
![](../../assets/img/posts/c765ed9b51e3.jpg)
</div>

I always like to install thermistors and heaters at the end of the process, as they are very sensitive and the thin cables can tear easily. I don't compromise on thermistor reading quality, so I replaced the H2's original NTC 3950 100k thermistor with a higher quality [Semitec 104NT-4-R025H42G](https://s.click.aliexpress.com/e/_AceUYa) thermistor. I also replaced the heater with the [stable 40W heater](https://s.click.aliexpress.com/e/_AUwpFM) that I always use. I'm also waiting for Mellow's new [70W ceramic heater](https://s.click.aliexpress.com/e/_9husmI) to come back in stock, and I'll probably be one of the first to order it for testing. Don't forget to apply non-conductive thermal paste to both the heater and the thermistor. This helps stabilize the temperature and gives more accurate readings.

<div class="gallery big" markdown>
![](../../assets/img/posts/48e6513fb2ce.jpg)
![](../../assets/img/posts/b62cd5c59178.jpg)
</div>

And of course, every block and nozzle gets the Slice Engineering protective coating, which has already saved me a few hotends in the past. It creates a polymer layer that isolates the block and makes it easy to clean. Together with the original silicone sock, the hotend is much safer now.

**Small note**: the coating will not make your heat block non-stick like PTFE, but it will be really easy to remove filament from the block. Over time, your block will not get that disgusting color from burnt filament residue. Despite the small amount of liquid, it was already enough for 12 nozzles and I still had 25% of the bottle left.

<div class="gallery big" markdown>
![](../../assets/img/posts/350b144f8358.jpg)
![](../../assets/img/posts/2195ba8121cb.jpg)
</div>

I almost forgot to mention that I replaced the mini IR sensor, which was damaged by a curious child ("Dad, I touched this and it's not lit anymore..."), with an [inductive auto leveling sensor](https://s.click.aliexpress.com/e/_9uyeX0). I placed it on the back of the X carriage (the bracket is also included in the H2 bracket zip). I added a 50mm M3 screw on top of the X carriage and secured all the wires to it with a zip tie. Then I used this 13mm [expandable cable sleeve](https://s.click.aliexpress.com/e/_ADi6Vk) for the cables.

Now, hold on a second before you load filament into your H2 extruder. It turns out BIQU left the filament opening exposed, so the filament will probably rub against the edge of the hole. To solve the problem, I added a [pneumatic connector](https://s.click.aliexpress.com/e/_ASZEQq). It slightly increases the weight but prevents the filament from grinding on the hole edges.

<div class="gallery big" markdown>
![](../../assets/img/posts/dd7a3fbb4695.jpg)
![](../../assets/img/posts/f1482b90eb83.jpg)
</div>

With all the preparations done, I loaded a new spool of [silk rainbow PLA](https://s.click.aliexpress.com/e/_Af59sO) that I really like and started testing.

<div class="gallery big" markdown>
![](../../assets/img/posts/c932afa17ffe.jpg)
![](../../assets/img/posts/5f74f9281d6c.jpg)
![](../../assets/img/posts/88f35b4d5cbe.jpg)
</div>

### Sample tests

For a whole month I abused the extruder and pushed it to the limit. I started by feeding almost 500g of PLA through it without printing, just to check for filament residue in the gear assembly. I heated the extruder to simulate an enclosure and checked for missed steps. With the BIQU H2 I printed almost 5 spools of filament: PLA, silk PLA, TPU, PETG and a PC blend using the all-metal heatbreak. Take your time and look at my print samples:

<div class="gallery big" markdown>
![](../../assets/img/posts/30e69f33a383.jpg)
![](../../assets/img/posts/cc26bf273615.jpg)
![](../../assets/img/posts/1bf6b62608b2.jpg)
![](../../assets/img/posts/473dce3a2756.jpg)
![](../../assets/img/posts/fd1f89478e13.jpg)
![](../../assets/img/posts/c5fa0d889531.jpg)
![](../../assets/img/posts/88ebd4c0ec2e.jpg)
![](../../assets/img/posts/7f187c680f6d.jpg)
![](../../assets/img/posts/9ef272633409.jpg)
![](../../assets/img/posts/ccb830fa7e7b.jpg)
![](../../assets/img/posts/28cfb0fd44ec.jpg)
![](../../assets/img/posts/d49dfdaa7fd6.jpg)
![](../../assets/img/posts/a5bb19ee2441.jpg)
![](../../assets/img/posts/7daa6b16bff0.jpg)
![](../../assets/img/posts/daf70e40f025.jpg)
![](../../assets/img/posts/d2a1f2b58548.jpg)
![](../../assets/img/posts/21a26d0f5358.jpg)
![](../../assets/img/posts/c199f1eb4cd9.jpg)
![](../../assets/img/posts/5b491e15663b.jpg)
![](../../assets/img/posts/1b794c24c188.jpg)
![](../../assets/img/posts/55752cd0b94c.jpg)
![](../../assets/img/posts/83df290b7bfe.jpg)
![](../../assets/img/posts/ac01d0512743.jpg)
</div>

### Final conclusion

Yes, it is expensive and there are many things to improve, but **I would buy it again**. My experience with the H2 extruder was very good. The extrusion is very consistent, and in most of my prints the layers were uniform. The pushing force is good, it handles most filament types well, and it's well built, light and reliable. It is not easy to reassemble, but that's not something you do every day. Currently, there are not many mass-produced competitors that can deliver the same results at such a low weight. Personally, I am less excited about extruders that have printed parts in the gear assembly, so for me this is the only alternative. I hope BIQU will read this review and maybe address some of the issues. I also think there is room to reduce its weight even further.

Get the [BIQU H2 extruder on AliExpress](https://s.click.aliexpress.com/e/_A5gltu).

Ben Levi
