---
title: "BLV Klipper Mainsail theme and carbon X axis"
description: "In my work (an autonomous drones dev lab) I use CNC machined carbon parts daily, and I noticed their price has dropped significantly."
---

[← All updates](index.md){ .back-link }

# BLV Klipper Mainsail theme and carbon X axis

### Carbon X axis

In my work (an autonomous drones dev lab) I use CNC machined carbon parts on a daily basis, and I noticed that the price of CNC machined carbon has dropped significantly.

A carbon tube is significantly lighter than an aluminum extrusion. The low weight takes some of the load off the motion system, which helps achieve better performance.

So I pulled out an old carbon X axis design I had made. It's a carbon tube combined with rivet nuts for fixing the rails, which saves the hassle of inserting nuts along the entire length of the tube. Only 2 jigs are needed at the ends to hold the M5 nuts.

I tried 4 different carbon services found on [AliExpress](https://s.click.aliexpress.com/e/_AMCl4g), and they all failed. Some weren't accurate, some required a minimum order of 100 pcs, and others simply couldn't add rivet nuts without them sticking out of the tube's outer walls.

Finally, I asked [Mellow](https://s.click.aliexpress.com/e/_AMCl4g) and sent him the plans. Two weeks later he sent me a video of the BLV carbon X axis:

<video controls preload="metadata" style="max-width:100%;width:280px" src="../../files/BLV-Klipper-Mainsail-theme.mp4"></video>

I don't have it yet and I haven't tested it, but most of you are familiar with [Mellow's](https://s.click.aliexpress.com/e/_AMCl4g) high-quality products. I hope to get it soon and test it. I have some concerns about the thickness of the tube, and a real fear that the rivet nuts will come loose over time without epoxy or a thicker tube. My backup plan is a safe solution: only holes without rivet nuts, and a long jig to hold the M3 nuts. I need to test it first. If it survives my tests, I will ask [Mellow](https://s.click.aliexpress.com/e/_AMCl4g) to add it to his store.

At this point I must mention again that I make no profit from this, and none from [Mellow](https://s.click.aliexpress.com/e/_AMCl4g) either. But I thank him and appreciate his support for the project and for making prototypes for testing.

### Klipper Mainsail theme

I moved from [Fluidd](https://docs.fluidd.xyz/) to [**Mainsail**](https://docs.mainsail.xyz/) and I'm happy. For those who don't know, Klipper has a few user interfaces to choose from. I had been using Fluidd, but I found out that it had not been updated for a while because the main developer left the project. So I decided to move to Mainsail, which has become popular.

The installation process was very convenient. I highly recommend installing the [MainsailOS](https://github.com/mainsail-crew/MainsailOS/releases) image on your Raspberry Pi SD card. It will save you a lot of time and frustration. Just follow the [MainsailOS installation guide](https://docs.mainsail.xyz/setup/mainsail-os).

After using it for a short while, I created a BLV theme for the Mainsail UI and wanted to share it with you:

![](../../assets/img/posts/967a90b2f74f.jpg)

You can download the BLV Mainsail theme pack:

File: BLV Mainsail klipper theme.zip (ZIP, 210KB)

To install it, check the [Mainsail theming guide](https://docs.mainsail.xyz/theming/prepare) or follow this quick guide.

#### Quick installation guide

1. Download the file and extract it.
2. In the "**Machine**" menu, click the gear icon and enable the "**Show hidden files**" option.
3. Create a "**.theme**" folder in your config folder.
4. Upload all the files from the zip file into the **.theme** folder.
5. Hit **Ctrl+F5** and enjoy.

!!! download "Files from this post"
    [:material-download: BLV-Klipper-Mainsail-theme.mp4](../../files/BLV-Klipper-Mainsail-theme.mp4){ .md-button }
