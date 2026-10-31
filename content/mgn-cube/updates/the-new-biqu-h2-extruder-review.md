---
title: "BIQU H2 extruder review"
description: "Finally, after a whole month of careful testing the BIQU H2 extruder on my BLV mgn Cube 3d printer. I feel pretty confident writing my conclusions abo"
---

[← All updates](index.md){ .back-link }

# BIQU H2 extruder review

Finally, after a whole month of careful testing the [**BIQU H2 extruder**](https://s.click.aliexpress.com/e/_A5gltu) on my [**BLV mgn Cube 3d printer**](../index.md). I feel pretty confident writing my conclusions about BIQU's new [**H2 extruder**](https://s.click.aliexpress.com/e/_A5gltu). I promise you that I have tried hard to write a balanced and honest review. After all, no one pays me to write anything.

### So why is everyone excited about the new extruder?

Well the [Biqu H2 extruder](https://s.click.aliexpress.com/e/_A5gltu) actually reminds the Hemera extruder, only with a small size stepper, higher gear ratio at half the weight of the E3D Hemera extruder. When they designed the [H2 extruder](https://s.click.aliexpress.com/e/_A5gltu), it was clear that the main principle behind the H2 design was to produce a Direct Drive at the lowest possible weight. Here is a picture that will show you how small the H2 extruder compared to the [Trianglab's matrix](https://s.click.aliexpress.com/e/_ANs1Ql) that [I reviewed](trianglelab-matrix-adapter-for-blv-cube-metal-kit.md) some time ago:

![](../../assets/img/posts/4991de637c1e.jpg)

Sure, I guess you can find a number of DIY extruders under 170g. But how many of them will actually be made of Aluminium and survive inside the enclosure? or will not wear out fast since they are not made of printed parts? Anyway, I'm glad someone saw the potential and really managed to reach such an impressive specification. And speaking of the specification:

Biqu H2 specs:

- Direct drive extruder Ratio 7:1 / Torque 770mN.m
- Size: 60x35x35mm
- Weight **219g** including hotend and fan! (mine was 225g)
- Max pushing force: 7.5kg (I was only able to verify 4.62kg)
- Max temperature: 260ºC but Upgradeable to 500ºC
- NEMA14 Motor 1.8º degrees Stepper motor.
- Nominal e-steps: 932 s/mm for 16x setup. (after Calibration: 917.444)
- NTC 3950 100k Thermistor and a 24v Heater.

So a long time ago I ordered the extruder. It wasn't cheap, [$ 100 for the extruder](https://s.click.aliexpress.com/e/_A5gltu) is definitely expensive. But when I bought it there was no reliable direct-drive alternative that weighs less than the H2 extruder. If there were alternatives in serial production, I guess the price would have been much lower than this. After a rather short wait, the packaging arrived. I was very excited to open it. The extruder came in an airtight custom box, lying comfortably in a soft material that kept it from being damaged. Very neat, it came with instruction and a separate bag that contained all the other accessories and tools. inside the package you will find:

- Biqu H2 extruder
- 3510 24v fan with a long cable.
- 35mm fan grill
- NTC 3950 100k Thermistor
- 24v 40W Heater with thick cables insulation
- Stepper motor cable
- Heat block silicone
- Yellow duck - My favorite item in this order.
- Screws and Tools
- additional order: All-metal Heatbrakes for higher temp printing: 1 x 303 Stainless Steel heatbrake 1 x Titanium heatbrake

<div class="gallery big" markdown>
![](../../assets/img/posts/9c0569e73d23.jpg)
![](../../assets/img/posts/23b14af92785.jpg)
![](../../assets/img/posts/4329b6920c45.jpg)
</div>

I must say I was very impressed with the build quality of the extruder. Everything is made of aluminum and looks good. The parts themselves have been smoothed, no chips, no dirt and no visual defects. I was sure the gears were made of a glass-filled plastic, But I was pleasantly surprised when I realized they were actually metal gears. However, I found some issues that bothered me a lot and I had to change them before my first use - Below you can read more about the changes I made. Here are some pictures of the extruder before I started disassembling and testing the H2 extruder.

<div class="gallery big" markdown>
![](../../assets/img/posts/63b62818278f.jpg)
![](../../assets/img/posts/db84295f222f.jpg)
![](../../assets/img/posts/93a9a0cc0bd7.jpg)
![](../../assets/img/posts/f3a5dc93bf0e.jpg)
</div>

This is what it looks like after removing the fan and exposing the entire **7:1 gears mechanism**:

<div class="gallery big" markdown>
![](../../assets/img/posts/3676da624f41.jpg)
![](../../assets/img/posts/d344779280f2.jpg)
![](../../assets/img/posts/34fb527d8527.jpg)
</div>

The heating block of the extruder is actually a regular aluminum heated block from which large pieces were shaved and drilled out. the main purpose was probably to lose weight. The heatbreak is a standard size but in profile D and you lock with two set screws. in the last photo, I tried to use a regular Heated block and it was fine. the first pic is the All-metal heatbreaks.

<div class="gallery big" markdown>
![](../../assets/img/posts/551e6ac36229.jpg)
![](../../assets/img/posts/aa35f0005c8b.jpg)
![](../../assets/img/posts/38d7d2740bf2.jpg)
![](../../assets/img/posts/7ba7f1573966.jpg)
![](../../assets/img/posts/0ff78a6348d0.jpg)
![](../../assets/img/posts/0f57b1bb1701.jpg)
</div>

Before you will assemble your Heater block I recommend you calibrate your extruder e-steps. I found a huge difference between BIQU's recommended e-steps (**932**) and the actually calibrated e-steps for my H2 extruder (**917.444**). you can also check if the motor direction is correct too.

One of the first modifications I made was to change the direction of the heatblock. I wanted the narrow part to be against the front of the printer so I could use an efficient cooling solution. Also, I did not like so much the inner finish of the original BIQU nozzle (first photo) So I replaced the nozzle with an [amazing quality nozzle](https://s.click.aliexpress.com/e/_ANF7sA) that I purchased a few months ago from Mellow's store. In order to lock the nozzle in place, I used a wrench and inserted an Allen key into the hole of the heater. This way I locked the nozzle in place without damaging the exterior finish of the block (second photo).

<div class="gallery big" markdown>
![](../../assets/img/posts/abdc7af7baee.jpg)
![](../../assets/img/posts/bb3c9854edff.jpg)
![](../../assets/img/posts/95c3baa5c62f.jpg)
</div>

after changing the heater block orientation and nuzzle I have started taking care of something else that was bothering me. I may be wrong, but it seems that the gears are made of black coated steel material that can rust over time due to moisture in the air. I noticed also that the Biqu doesn't bother to grease the gears before sending them out to customers and I found it very disturbing. Applying a little grease to the gears system will make the system work better, keep the gears longer and protect it from moisture in the long run. Luckily a few weeks ago I ordered the Super Pinda from PRUSA in order to test the accuracy compared to the mini IR sensor. and I added 5pcs of PRUSA grease. I found it to be an excellent grease even for use with linear rails. Therefore, I spread out a piece of paper, carefully disassembled the gears, and gently greased all the components. When greasing the gears please care not to accidentally grease the wheels that pull the filament. any presence of oil on them can cause an extrusion failure.

<div class="gallery big" markdown>
![](../../assets/img/posts/ed49d3506b19.jpg)
![](../../assets/img/posts/8e02bdff0a44.jpg)
![](../../assets/img/posts/9181c991dcf1.jpg)
![](../../assets/img/posts/02bcb4060907.jpg)
</div>

Immediately after assembling everything, I again had to disassemble everything because another annoying issue found. A cable must be connected to the extruder stepper motor. Someone chose to assemble the H2 extruder motor so that the cable socket is face down - critical mistake. At some point, the cable may come loose and get stuck in the item we are printing and destroying the whole print. to fix it, you must disassemble the extruder and then take out the two tiny M3 screws fixing the extruder body to the stepper motor. rotate the stepper motor 180 degrees and re-lock the screws back. Please mind that the threads are short and can be easily destroyed, so screw it gently and not too tight

<div class="gallery big" markdown>
![](../../assets/img/posts/7a5fa4d06419.jpg)
![](../../assets/img/posts/13464513762f.jpg)
![](../../assets/img/posts/6f5de4c585fa.jpg)
</div>

After several hours of designing and simulations, I was able to get a strong enough bracket that can support the new H2 extruder and is suitable for the [metal kit](new-metal-kit-upgrade-blv-mgn-cube.md) of my [**BLV mgn Cube 3d printer**](../index.md). Please note, that I added Spring washers to the long H2 extruder screws. After a few dozen hours of printing, I noticed that I needed to re-tighten the long screws which hold all the H2 components together. adding spring washers fixed the issue completely. I did a number of tests using double 3510 ball-bearing blowers, but the airflow was just ridiculous. I ended using a [powerful dual ball bearing 5015 blower fan](http://s.click.aliexpress.com/e/cTnlOmKc) which gave me fantastic results. Please feel free to download the bracket files, I added the STL file and STEP (CAD) file In order to make it easy for you to make changes as you wish:

![](../../assets/img/posts/4b290ffbadc8.jpg)

BLV Cube Metal H2 adapter.zipDownload ZIP • 442KB

**licensed under the Creative Commons - Attribution - Non-Commercial - Share Alike license**

<div class="gallery big" markdown>
![](../../assets/img/posts/46e928aa0cdf.jpg)
![](../../assets/img/posts/87fc828b711a.jpg)
![](../../assets/img/posts/c765ed9b51e3.jpg)
</div>

I always like installing thermistors and heaters at the end of the process, as they are very sensitive and the thin cables can tear easily. In my case, I don't compromise on the thermistor readings quality, so I replaced the H2's original NTC 3950 100k thermistor with a higher quality [Semitec 104NT-4-R025H42G](https://s.click.aliexpress.com/e/_AceUYa) thermistor. I also replaced the heater with a [stable 40W heater](https://s.click.aliexpress.com/e/_AUwpFM) that I always use. I'm still waiting for fo the new Mellow's [70W Ceramic heater](https://s.click.aliexpress.com/e/_9husmI) to be back to stock, I'll be probably the first to order it for testing. Please, don't forget to apply a non-conductive thermal grease both on the heater and thermistor. This helps stabilize the temperature and gives more accurate temps readings.

<div class="gallery big" markdown>
![](../../assets/img/posts/48e6513fb2ce.jpg)
![](../../assets/img/posts/b62cd5c59178.jpg)
</div>

And of course, every block and nozzle get the Slice engineering protection coating that has already saved me a few hotends in the past. it creates a polymer layer that isolates the block, making it easy to clean. with the original silicone sock - the hotend much safer now.

**small note**: It will not make your heater block non-stick PTFE like but it will be really easy to remove the filament from the block. After a while, your block will not get the disgusting color as a result of burnt filament residue. Despite the small amount of liquid. in fact, it was already enough for 12 nozzles and I had 25% of the bottle left.

<div class="gallery big" markdown>
![](../../assets/img/posts/350b144f8358.jpg)
![](../../assets/img/posts/2195ba8121cb.jpg)
</div>

I almost forgot to mention that I replaced the mini IR sensor that was damaged due to a case of a curious child ("Dad, I'm touching this and it's not lit anymore...") with an [inductive auto leveling sensor](https://s.click.aliexpress.com/e/_9uyeX0). I placed it on the back of the X-carriage (The bracket also is included in the H2 bracket zip). I added a 50mm M3 screw on the top of the X-carriage and secured all the wires with a zip tie to the screw. Then I used this [expandable Cable Sleeve](https://s.click.aliexpress.com/e/_ADi6Vk) size 13mm for the cables.

Now, just hold a sec before you load a new filament into your H2 extruder. It turns out BIQU left the filament opening exposed. If you leave the hole exposed, the filament will probably rub against the edge of the hole. In order to solve the problem, I added a [pneumatic connector](https://s.click.aliexpress.com/e/_ASZEQq) that will slightly increase the weight but prevents grinding of the filament on the hole edges.

<div class="gallery big" markdown>
![](../../assets/img/posts/dd7a3fbb4695.jpg)
![](../../assets/img/posts/f1482b90eb83.jpg)
</div>

Now that all the preparations were done, I loaded a new [silk rainbow PLA](https://s.click.aliexpress.com/e/_Af59sO) spool that i really like and started testing.

<div class="gallery big" markdown>
![](../../assets/img/posts/c932afa17ffe.jpg)
![](../../assets/img/posts/5f74f9281d6c.jpg)
![](../../assets/img/posts/88f35b4d5cbe.jpg)
</div>

### Sample tests!

I can describe to you how for a whole month I abused the extruder and took it to the limit. Starting by feeding almost 500g of PLA filament without printing, just to check if there is filament residue in the gear assembly. Heating the extruder to simulate enclosure and checking for missing steps. I printed using the BIQU H2 extruder almost 5 spools of filament: PLA, PLA silk, TPU, Petg, and PC blend using the All-metal heatbreak. Please take your time and look at my print samples:

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

Yes, it is expensive, there are many things to improve but **I would buy it again**. My experience with the H2 extruder was very good. The extrusion is very consistent, In most of my prints, the layers were uniform. pushing force is good, it handles well with most filament types, it's well built, low weight, and reliable. It is not easy to re-assemble but it's not something that happens every day. Currently, there are not many competitors in mass production that can provide the same results at such a low weight. Personally, I am less excited about extruders that have printed parts within the gear assembly. Therefore for me, this is the only alternative. I hope BIQU will be able to read this review and maybe address some of the issues. I also think the possibility of reducing even more weight of it exists.

### [Link to Biqu H2 extruder](https://s.click.aliexpress.com/e/_A5gltu)

Ben Levi
