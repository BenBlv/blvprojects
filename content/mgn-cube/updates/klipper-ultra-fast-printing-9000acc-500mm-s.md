---
title: "BLV Cube + Klipper: 9000 mm/s² and 500 mm/s"
description: "After long experience with Reprap firmware, I decided to try Klipper."
---

[← All updates](index.md){ .back-link }

# BLV Cube + Klipper: 9000 mm/s² and 500 mm/s

![](../../assets/img/posts/15a5506bc9b9.jpg)

After long experience with Reprap firmware, I decided to try [Klipper](https://www.klipper3d.org/).

About two years ago, a good friend of mine (Manu) strongly recommended checking out Klipper firmware. At the time, the Klipper project began to take shape but the documentation was a big mess. Despite the potential, I decided to wait for the moment the system will be more convenient to install and easier for the average user. But to be honest, I was a bit skeptical. Two years have passed and I'm glad to see Klipper has become easier to install and even reliable.

Before I started testing the Klipper, I took my system to the edge of its limits running RRF firmware - At least that's what I thought. Installing a Klipper was a smart move, I felt like I was getting a new crazy printer that prints at ridiculously ultra-fast speed. It was the same [**FYSETC FULL kit**](https://s.click.aliexpress.com/e/_ACzKw1) I purchased a while ago with the BLV metal kit - the only difference is the firmware. Very quickly I came to the conclusion that the hotend is not good enough for fast printing, so I decided to purchase the [**Mellow NF-Sunrise Volcano 24V**](https://s.click.aliexpress.com/e/_A9Ap0z) (Direct drive extruder/hotend weight only **185g**), and soon after I found fast printing needs fast cooling so I added twin [4020 blowers](https://s.click.aliexpress.com/e/_9Hktwl) and started my tests.

<div class="gallery big" markdown>
![](../../assets/img/posts/9d44c1cb7d63.jpg)
![](../../assets/img/posts/109361457697.jpg)
![](../../assets/img/posts/e85139984c4c.jpg)
![](../../assets/img/posts/d9a8ee9e0620.jpg)
</div>

This is a video I took a while ago while testing the machine with Klipper firmware. All advanced settings were disabled and I only calibrated the Extruder and Z-offset. The printing results were amazing, but more amazing is that fast prints were made at speeds I never even dreamed of. It looked like the system is capable of much more than that - mainly due to the aluminum parts and the fact it was designed to withstand loads X9 times greater than now:

!yt FC9tIDhOgD4 | BLV mgn Cube at 9000 mm/s² acceleration and 500 mm/s

Some of the images you watched in the video:

<div class="gallery big" markdown>
![](../../assets/img/posts/2aa9b4f7609a.jpg)
![](../../assets/img/posts/78c45680a708.jpg)
![](../../assets/img/posts/b70993a917c2.jpg)
![](../../assets/img/posts/23f237a3af13.jpg)
![](../../assets/img/posts/c3af42727c74.jpg)
![](../../assets/img/posts/ea2dae4e27dd.jpg)
</div>

Immediately after I took this video, a long series of tests were started and pushed the boundaries. Then I wondered whether the Duet built-in drivers are my limits? a few years ago as the Tmc-2130 came out, I paid 35$ each for my BLV Anet mod and direct-fed it 24V instead of 12V in order to get more juice (torque). So, in this case, I'm testing a new **prototype Board** that has not yet been released to the market - It's so powerful... it's just amazing! more details very soon - I promise.

![](../../assets/img/posts/cb8c38426b93.jpg)

Anyway, I'm now confident enough to share with you all my Klipper files and settings including Superslicer BETA BLV profiles. This will give you a good starting point for getting your printer up and running Klipper.

if you can't wait and just want the files, Just download the BLV Klipper files here:

**Printer.cfg**

BLV printer cfg.zipDownload ZIP • 5KB

**BLV SuperSlicer profile**

BLV Superslicer profile.zipDownload ZIP • 327KB

### Installing Klipper

**BLV mgn Cube setup for the provided Klipper config**

- [FYSETC BLV mgn Cube full kit 3d printer](https://s.click.aliexpress.com/e/_ACzKw1) (DUET 2 wifi)
- BLV metal kit (included in the fysetc kit) - replaces all the printed parts with metal parts.
- [Mellow NF-Sunrise Volcano 24V](https://s.click.aliexpress.com/e/_A9Ap0z) - Lightweight High flow direct drive Extruder (185g)
- [Twin 4020 blowers](https://s.click.aliexpress.com/e/_9Hktwl) as a part cooling
- official Prusa super pinda leveling sensor - probes fast and accurate (not for glass).
- FYSETC bed + FYSETC Glass (included in the kit) + magnetic PEI spring steel sheet.

*STL and CAD files for the [NF-Sunrise volcano 24v](https://s.click.aliexpress.com/e/_A9Ap0z) and dual [4020 blowers](https://s.click.aliexpress.com/e/_9Hktwl) can be found down below.

### In order to use Klipper, you must get these parts too

- Raspberry PI ( I used raspberry pi 4)
- USB Type-C cable
- Fast Micro-SD or SSD USB 3.1 (I used 64GB Sandisk ultra)
- For input shaper, you would need this Acceleration sensor

**Klipper has 2 main parts:**

1. Klipper firmware - installed on the Board
2. Klipper core files + GUI - installed on the Raspberry's Micro-SD card. here you have 3 choices: [Fluidd](https://docs.fluidd.xyz) ( my favorite), Mainsail, Octopi.

### Klipper installation guide

I want to thank a special person - [**David Husolo**](https://www.facebook.com/groups/371460246914851/user/1208415623/) Who has contributed a lot and continues contributing to the BLV project. My dear friend David prepared an excellent guide that explains step by step how to install the Klipper. David's guide is available [**HERE**](https://www.ifixit.com/Guide/Klipper+Install/145923)

At some point, you would need to upload your "**printer.cfg**" file. I have uploaded my Printer.cfg and it is available inside the zip file below. please feel free to use it and modify it as you need.

BLV printer cfg.zipDownload ZIP • 5KB

Don't forget to edit the line below [MCU] tag:

[mcu]  
serial: /dev/serial/by-id/usb-Klipper_sam4e8e_xxxxxxxxxxxxxxxxxxxxxxxxxx-if00

The correct ID can be found using this command on PuTTY:

ls /dev/serial/by-id/*

Now that you have connected to your Klipper firmware I advise you first read all the Relevant documentation for Klipper firmware, you can do that by checking This [official Klipper website](https://www.klipper3d.org).

in the next update, you will be able to choose BLV scheme/Theme from the setting menu (Thanks to [Stefano](https://github.com/StuSerious)). This is how your panel should be like after you have done installing:

<div class="gallery big" markdown>
![](../../assets/img/posts/7709b77240a5.jpg)
![](../../assets/img/posts/a1d127fe5c3b.jpg)
</div>

Please note that I added a controlling slider for the COB led light (connected to Fan2 port).

### BLV Superslicer profiles

The best suitable slicer for the Klipper firmware currently is [SuperSlicer](https://github.com/supermerill/SuperSlicer/releases). It's an open-source slicer based on Prusa slicer. i managed to create a BETA printer + printing profile that will give you a start point. Please mind, these are the original files I used for some of the tests. In the video, I changed all the accelerations settings to 9,000 mm/s^2 and increased dramatically my speed. Feel free to use any other custom printing profile and share it on the BLV Facebook group to discord channel. I will be happy to mix it with the official BETA profile if it's good.

<div class="gallery big" markdown>
![](../../assets/img/posts/362b46c557b9.jpg)
![](../../assets/img/posts/f9239f3cd093.jpg)
</div>

in order to use SuperSlicer, please download the latest version of Superslicer from [this link](https://github.com/supermerill/SuperSlicer/releases)

Then, download the BLV SuperSlicer profile zip from here:

BLV Superslicer profile.zipDownload ZIP • 327KB

**How to use the BLV SuperSlicer profile:**

1. extract the content of the zip file
2. copy **BLV** folder to path: \SuperSlicer_x.x.xx.x_win64_xxxxxx\resources\profiles inside your SuperSlicer installation path.
3. copy BLV.ini and BLV.idx to path: \SuperSlicer_x.x.xx.x_win64_xxxxxx\resources\profiles it should be looking like this:

![](../../assets/img/posts/87a3c5891e77.jpg)

\4. Open SuperSlicer and Choose BLV and the Filaments set from the configuration screen.

### BLV NF-Sunrise Printed Parts

![](../../assets/img/posts/c1342c1d20a8.jpg)

Inside the CAD file, you will find the Cable chain files- it's an alpha version and I will probably switch to a bigger cable chain soon.

<div class="gallery big" markdown>
![](../../assets/img/posts/3702f5431ed9.jpg)
![](../../assets/img/posts/d9a8ee9e0620.jpg)
![](../../assets/img/posts/3e3407d6cd68.jpg)
![](../../assets/img/posts/2a8843fff315.jpg)
![](../../assets/img/posts/1bb6f99d18c6.jpg)
![](../../assets/img/posts/9fd0bdb29e23.jpg)
</div>

**You can download all the STL files from here:**

licensed under the Creative Commons - Attribution - Non-Commercial - Share Alike license.

BLV NF-Sunrise Volcano STL V1.1.zipDownload ZIP • 2.08MB

Edit: Fixed the NF mount

Check here the names of the parts and how to print them:

![](../../assets/img/posts/d0d381948fd4.jpg)

**For your convenience, you can also download the F3D file (CAD)**

licensed under the Creative Commons - Attribution - Non-Commercial - Share Alike license.

BLV NF-sunrise share CAD.zipDownload ZIP • 23.09MB
