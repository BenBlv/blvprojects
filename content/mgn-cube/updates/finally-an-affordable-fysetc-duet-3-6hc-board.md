---
title: "An affordable Duet 3 6HC board"
description: "I have been fantasizing for a long time about buying the Duet3 in order to use it as a board for my BLV mgn Cube 3D printer. The Duet3 6HC is actually"
---

[← All updates](index.md){ .back-link }

# An affordable Duet 3 6HC board

### Duet3 6HC board

I have been fantasizing for a long time about buying the [**Duet3**](https://www.duet3d.com/Duet3Mainboard6HC) in order to use it as a board for my BLV mgn Cube 3D printer. The Duet3 6HC is actually the new generation of the well known Duet wifi board running Reprap 3 FW. It has all the hottest features, excellent specifications, and the best documentation you can wish for a 3d printer board. Equipped with a fast 32 Bit processor, High-speed bus for Raspberry PI (SBC), 6 X Trinamic 5160 stepper drivers, 10 PWM outputs, 9 IO ports for endstops, probes, sensors, 4 Thermistor or PT1000 inputs, 2 CAN-FD buses for expansion boards (Up to 24 steppers), built-in Ethernet port, and running Duet web Access interface + RRF3 FW. There is much more to expand but these are the main features.

### So where's the problem?

225$ not including shipping is pretty much money, at least for me. Assuming my needs remain unchanged and given the insane price, the Duet 3 just wasn’t an option and it's a shame.

### finally!

All this was true until recently Fysetc decided to produce the Duet3 6HC. We should remember the Duet3 is an open source-based. When I saw the [**Duet3 6HC**](https://s.click.aliexpress.com/e/_A1uWxz) listing on Aliexpress, I was excited, since I realized there is now another source from which I can get the Duet 3 6HC at an excellent price that made it attractive to me. [**145$**](https://s.click.aliexpress.com/e/_A1uWxz) for one of the best 3d printer boards on the market is just amazing! 80$ less!! Within a short time from the moment I saw the listing page, it was already deep in my order list and I started counting days.

### Unboxing

<div class="gallery big" markdown>
![](../../assets/img/posts/9c02d6f5a00f.jpg)
![](../../assets/img/posts/46542a6d0e26.jpg)
![](../../assets/img/posts/a47ce7721f9f.jpg)
</div>

I ordered the Duet 3 6HC and out of curiosity also the 3HC expansion board. The boards came well packed, wrapped in an antistatic bubble bag and carton packaging. I must point out that They did a good job and included everything needed to install the board in both the mainboard and the expansion board. For some reason nowhere is it stated what comes with the board. I have prepared for you a complete list of all the components I received with the board:

- Duet3 6HC clone board
- Pack of 2.54mm Molex KK connectors and shells for most of the components.
- Pack of BVH-21T-P1.1B (JST) connectors and shells for steppers and heaters.
- Crimping pins for high current connectors
- \0.5m CAN cable
- 16GB sd card for Raspberry (if you are using one)
- 8GB sd card for FW config
- Raspberry cable

<div class="gallery big" markdown>
![](../../assets/img/posts/fcf4c0ffaa43.jpg)
![](../../assets/img/posts/a917e344a21a.jpg)
![](../../assets/img/posts/4ccf3afaa766.jpg)
</div>

As someone who has seen quite a few boards, I can say that this is a high-quality PCB. All components were properly soldered, the board was washed properly, and tested. I must say that the connectors provided by Fyestc are among the best I have ever worked with. using this [**cheap SN-28B Crimping Tool**](http://s.click.aliexpress.com/e/ctVlu2Gs) I got really nice crimp results, better than my original old Duet.

Before fixing the board on the back panel, I recommend updating the Duet3 and making sure the FW is running properly. You can find all the needed information about updating to the latest version [**here**](https://docs.duet3d.com/). The latest firmware version can be downloaded from [**here**](https://github.com/Duet3D/RepRapFirmware/releases).

I had to drill new holes on the rear panel since the new Duet3 6HC is much bigger than the old Duetwifi. Therefore it is worth checking that there is enough space in the back of the panel. For your convenience, I have attached a basic wiring diagram of the board as I installed it. Note that I have yet not added the power button. Also in this version, I have used an inductive sensor and an AC heated bed.

![](../../assets/img/posts/39114e2e519b.jpg)

And this is what it looks like after installation:

<div class="gallery big" markdown>
![](../../assets/img/posts/66e78cf36200.jpg)
![](../../assets/img/posts/57d4c5702a0a.jpg)
![](../../assets/img/posts/3521d9cd06bb.jpg)
</div>

### Configuration

About a week before It arrived, I sat down and read most of the Duet3 documentation. I highly recommend you do the same. All documentation is available [**here**](https://docs.duet3d.com/). For your convenience, I have prepared a basic config from which you can start configuring your own system. Note that in Config I used the new BIQU H2 extruder. therefore, the endstops and probe locations should be changed according to your BLV cube 3d printer settings.

My Duet3 config files are available here:

Basic Duet3 6HC config by Ben Levi.zipDownload ZIP • 5KB

You can also check **David Husolo** [**Duet RRF3 configurations**](https://github.com/armysolo/BLV?fbclid=IwAR0-mR3bgpyxTPCFCVhUZgBWfTpTGOmq77aLlfcxRdvNA5OaHYBYkjqmsJw) on his Github for Both BLV AM8 and BLV mgn Cube. I would like to take this opportunity to thank David for his tremendous efforts in the community.

### conclusion

I guess a lot of people are asking themselves, is it worth upgrading the board to Duet3 6HC? After all, Duet 3 6HC will function almost exactly like the old DuetWifi, which costs less. This was true until Fysetc put their Duet 3 up for sale for 145$ which is about $ 80 less than the duet officially. In terms of features, Since the Duet3 has a more powerful processor and Double precision floating point, I allow myself not to rely on the TMC drivers auto interpolation and I set my own desired micro-steps settings. We must keep in mind that while using auto interpolation, the driver will rarely reach 256 microsteps, however, we can force it to use a higher amount of microsteps, it will provide quieter motion, higher accuracy, and fantastic print quality. The new TMC5160 keeps surprise me with every print.

Those of you who use 3 Z axes auto-leveling, will be happy to hear that Duet 3 has 6 stepper drivers. That is, from now on you don't need to add an expansion card for 3 axis auto-leveling. The only downside for me in Duet 3 is the lack of a WIFI module. True, wireless module makes it slower to work with compared to the Duet3 Ethernet cable, but much more convenient.

After testing it for more than a month I can say with complete confidence that overall I am very pleased with the board and without a doubt, it is one of the best boards I have ever worked with. The prints come out super great, Duet's crazy web interface has become a must-have feature for me. recommended!

Here some sample prints using the Duet3 6HC board:

Printed using [**Biqu H2 direct drive extruder**](https://s.click.aliexpress.com/e/_AgqcYp)

Filament: [**Noulei PLA Silk filament**](https://s.click.aliexpress.com/e/_Ag1rDK), [**Prusament PLA silver galaxy**](https://shop.prusa3d.com/en/prusament/712-prusament-pla-galaxy-silver-1kg.html)

<div class="gallery big" markdown>
![](../../assets/img/posts/f9261a092485.jpg)
![](../../assets/img/posts/e00a6f88d0f9.jpg)
![](../../assets/img/posts/1931e609828d.jpg)
![](../../assets/img/posts/39702bb0af74.jpg)
![](../../assets/img/posts/2561aa33dba2.jpg)
![](../../assets/img/posts/1e0bad7198f2.jpg)
</div>

Hope you enjoyed reading

Sincerely

Ben Levi

![](../../assets/img/posts/8e903eef96c1.png)

**Edit**: Unfortunately, I received requests to delete the post. Some people in the industry think that open source is not really open source but a source to double their money. Sorry, but thanks to open source even the average person can afford an Arduino for example. I will make this clear again, My main goal is to make it all affordable for everyone. My sincere apologies to all those who do not think so. In addition, claims were made that I may be received board for "free" - I am sorry but I paid like any other person (photo attached).

![](../../assets/img/posts/dbcf6c7605b9.jpg)
