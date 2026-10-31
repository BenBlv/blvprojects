---
title: "The Metal Kit upgrade"
description: "For several months I have been designing and testing a kit of CNC-machined aluminum parts to replace the BLV mgn Cube's printed motion system parts."
---

[← All updates](index.md){ .back-link }

# The Metal Kit upgrade

As you know, for several months I have been designing and testing a new kit of components that replaces all the printed parts of the BLV mgn Cube's motion system. In other words, instead of printed parts made of PETG/ABS, we can enjoy precise, reliable parts made of CNC-machined aluminum. The new upgrade kit further increases the printer's capabilities, eliminates flex in the frame and improves performance. The new components are smaller, stronger and weigh much less.

![](../../assets/img/posts/41b4c7e9a3d9.png)

Happily, after such a long and tedious period, the moment we have all been waiting for has arrived: the kit is ready in beta. I sent all the source files I developed to the manufacturer for free, and in return he sells the kits to us at a very low price. Of course, I don't make any profit from this, and it allows him to keep the price of the kits very low.

In less than a week, 100 kits were sold to the beta group members for $109, including free shipping. The manufacturer has since raised the price to $119 + free shipping and promised that this will be the fixed price of the kit. That is still a bargain for over 50 pieces.

### Where can I get it?

You can get it from the [**official manufacturer and seller**](https://s.click.aliexpress.com/e/_dZWiHmO).

Please note, my dear friends, and I will remind you again: I don't own any store and I make no profit. I am only the developer of the kit, and the files were given to the manufacturer for free to keep it affordable, since the manufacturer doesn't need to pay for the design.

**Warning:** I have been notified that an **unauthorized** store on AliExpress started selling a **non-genuine metal kit** that is not accurate and does not use the original files. I've received some complaints about mismatched parts. **Please do not buy from them.** The only genuine BLV metal kit parts can be found at the [**official BLV metal kit store**](https://s.click.aliexpress.com/e/_dZWiHmO).

### Source files and STL files to print

- For now, you need to print the new hotend shield. The new shield is smaller and fits the new setup. Please note that the kit doesn't include the 4010 fans and fan screws. Download the [**new hotend shield STL**](../../files/BLV-Metal-Kit-hotend-shield.zip).
- To help you, I'm releasing the source files of the X-carriage. The zip contains both the new hotend shield and the X-carriage metal parts, so it will be easier to remix, design or modify parts and make them even better. Please note that the files are licensed [under Creative Commons Attribution-NonCommercial-ShareAlike](https://creativecommons.org/licenses/by-nc-sa/4.0/). Download the [**X-carriage source files**](../../files/BLV-Metal-Kit-X-carriage-source.zip).

<div class="gallery big" markdown>
![](../../assets/img/posts/bc8e054f2213.png)
![](../../assets/img/posts/4d8d53cbcd8b.png)
</div>

### Auto-leveling sensors

The kit supports:

- **IR mini** sensor
- **BLTouch** with a printed adapter (experimental): download the [**BLTouch adapter**](../../files/BLV-Metal-Kit-BLTouch-adapter.zip)

Since it's a new carriage, you need to change the probe offset in the firmware, because the firmware needs to know the position of the probe relative to the tool. On Duet, the command that defines the offset is G31, and you can search for it inside the config file. More information can be found in the [**Duet documentation**](https://docs.duet3d.com/).

For your convenience, I have added accurate distance measurements for the probes:

![](../../assets/img/posts/c4537c69d265.jpg)

### Assembly video guides

!yt h6RqIR12xYc | Metal Kit - left X mount
!yt PkNG_4DqNDU | Metal Kit - right X mount
!yt xgskB43XnrQ | Metal Kit - left rear corner

- **Left X mount:** use only the plates with the "L" mark on them. Do not use plates with the "R" mark.
- **Right X mount:** use only the plates with the "R" mark on them. Do not use plates with the "L" mark.
- **Left rear corner:** pay attention to the length of the motor standoff.

!yt mT_S7TKsJ8E | Metal Kit - right rear corner
!yt ZSMAie1AsHY | Metal Kit - left tensioner

- **Right rear corner:** pay attention to the length of the motor standoff.
- **Left tensioner:** make sure to use only parts with an "L" or "Left" marking.

!yt XTAEOTpn_As | Metal Kit - right tensioner

- **Right tensioner:** make sure to use only parts with an "R" or "Right" marking.

!yt ychonAO79lA | Metal Kit - Z motor mount

**Z motor mount** assembly video.

!yt hjXf-C7vWmQ | Metal Kit - Z axis top mount
!yt eE851Lm2ddo | Metal Kit - X carriage

- **Z top mount** assembly video
- **X carriage:** please note that the belt locker is experimental. I personally prefer using a zip tie instead.
