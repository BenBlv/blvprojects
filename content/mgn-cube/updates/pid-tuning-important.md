---
title: "PID tuning: important"
description: "PID calibration is a crucial step for high-quality prints. Here is why it matters, when to do it and how to prepare the hotend and bed."
---

[← All updates](index.md){ .back-link }

# PID tuning: important

I know that most of you are familiar with PID tuning and have already done it. But this is for those who have not performed a **PID calibration** yet.

PID calibration is a crucial step for getting high-quality prints. PID is an algorithm that uses 3 defined values to control and stabilize the nozzle and bed temperatures. The process is very simple. It should be done after building the printer and every time you change a component such as the heating element, the sensor, the bed sheet, or even when you add a silicone sock. At least 4 people asked for my help on Messenger, and most of their print quality issues vanished after a PID calibration.

Here are a few links with useful information about it:

1. [Duet3D documentation on tuning the heater temperature control](https://docs.duet3d.com/)
2. [BeTrue3D guide to PID tuning the hotend on a Duet WiFi/Ethernet](https://betrue3d.dk/duet-wifieth-pid-tuning-hotend/?fbclid=IwAR1x5exzV9DZmbrZbsseSdE3A_UrQ3_d7P3zbOxuXRyruCojGM3fNyTuqDI)
3. If you are using Marlin: [RepRap wiki on PID tuning](https://reprap.org/wiki/PID_Tuning?fbclid=IwAR2wKRebERrejZ3yASsZZFfb0tpw_ZAt5W_upDq-C2qVUOMuEnP0HHXlRmo)

**Please note:**

- Before running PID, the hotend and bed must be cool. Turn the printer off for half an hour before you start.
- Before running PID on the hotend, heat the bed to your regular print temperature, position the hotend about 5mm above the bed, set the layer fan to your usual fan speed, and only then start the hotend PID.
- Before running PID on the bed, turn on the hotend and the fan, and position the hotend about 10-20mm above the bed.

<div class="gallery big" markdown>
![](../../assets/img/posts/98065895ac1c.jpg)
![](../../assets/img/posts/a86e37d74ce4.jpg)
![](../../assets/img/posts/3786ac8e4882.jpg)
</div>
