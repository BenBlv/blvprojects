---
title: "Metal Kit II update and clearance sale"
description: "It took 34 days to create this tiny part."
---

[← All updates](index.md){ .back-link }

# Metal Kit II update and clearance sale

### Metal Kit II update

34 days

It took 34 days to create this tiny part.

![](../../assets/img/posts/73995cf2b713.jpg)

Over the course of 34 days, I changed countless designs, tested, experimented, gathered and analyzed data. I gained a better understanding of the entire picture as a result of this small piece of the puzzle.

In order to design a system that is truly optimized for performance and produces above-average print quality, I had to stop compromising. Since I still have access to academic articles via my old student account at the university - I started searching for information that could help me develop a better motion system. As I studied all sorts of belt drive principles, some of which were completely unfamiliar to me, I also planned my experiments. Initially, most experiments aimed to compare the old system with prototypes. But in the process, I discovered that many clones do not even meet 30% of the specifications in the original data sheets. Since the user may accidentally use a less reliable alternative, I had to replace every component. Rather than testing only 3 types of parts, I ended up buying and testing at least 28 different kinds of bearings, idlers, steppers, belts and more.

This is a terrific opportunity for me to thank a friend of mine who provided me with professional laboratory equipment - a half-year salary cannot cover most of them. Due to the possibility of him being fired, no names will be mentioned here including photos. Thanks a lot bud :)

In order not to bore you with too much data, here is an example of a small test.  
i built a closed loop jig to find vibration correlation with bearing type.

The jig setup consists of a close loop belt, a stepper, a pulley, an idler, 3 axis vibration lab measurement equipment with 3 probes + a stationary precalibrated probe, and 2 x optic speed measurement equipment for steppers and idlers. Data logger and more..  
Idler/bearing was tested with five mounting options. Three types of belts, many bearings, Chinese idlers, and gates idlers. Isolating idler vibrations was the most challenging part here, but this was only one of many experiments. I also had to retest each setup twice in order to measure both idler/bearing orientations (side and top).

![](../../assets/img/posts/c2b464b4ace0.jpg)

Based on the information I gathered, I came to the following conclusions:

- **Stracture** Despite its small size, it aligns the two most critical parts of the system. You can see that the part is attached to the frame in three different directions while aligning the profiles that hold down the Y-axis (second image). While there are better ways to align a motion system frame, due to the circumstances and DIY budget, this is the most efficient method.ve method.
- **No more idlers** They failed over and over again. My tests showed that even the original Gates idler for 9mm belts failed. Within 65 hours of work, black powder appeared inside the gates bearings and vibration levels increased. I have tested 28 idler/bearing manufacturers (with different clearances and accuracy levels) and have lost all trust in idlers.
- **A belt's teeth on a bearing** There hasn't been a definitive answer in the community to whether belt teeth can be used on bearings. There will always be a different opinion... but facts are what I'm looking for, not opinions. This is being written while a small 680mm belt system experiment jig has been running (almost non-stop) for 384 hours. It already answered 60% of my questions after only checking it twice.

![](../../assets/img/posts/9ef9541cdd68.jpg)

- **No tensioners** - at least not like the traditional ones. It is very convenient to maintain the belt with a tensioner. There are usually two or three moving parts with clearance between them. Regardless of whether it is held with a screw or locked with set screws, I noticed a 19% increase in system noise. I have come up with a solution that I will share with you later.
- **Screws are not accurate** It is also possible to affect the reliability of the system by having a large clearance between the screw's OD and the bearing/idler ID - which is the exact case while using screws for the idler/bearing. Shoulder bolts (-0.005h) are an option, but after measuring a couple of shoulder bolts, I found that some don't follow DIN specifications and don't care about the customer. BOSSARD makes the best ones, I think but they are expensive. So.. In order to solve this problem, I chose a high-precision custom solution.
- **Balance is crucial!** Motion systems are adversely affected by the incorrect use of washers and shafts/dowels of poor accuracy. Belts can even be damaged by it. Consequently, I had to design parts that compress the bearings and also align them with other components.
- **Weight and center of mass** Even though they are light, certain components affect their position in relation to moving masses. Many changes there :)

It is just the tip of the iceberg, I have already changed many parts in the final design to make it more reliable. In response to those asking when it will be ready? I will probably send a few prototype files to be manufactured (not the full motion system). You can probably expect some of the parts to be revealed as I won't be able to hold back..

### Fysetc - BLV mgn Cube clearance sale !

![](../../assets/img/posts/46107bef8955.jpg)

The Fysetc team asked me to share with you a clearance sale for the BLV mgn Cube 3D printer. I was really surprised to see they are offering it with **free shipping** to **USA** and **EU** customers. In addition, the price has dropped dramatically to **630$**, which is an excellent deal. If you find it interesting, here are the links for Fysetc BLV clearance sale:

- [BLV mgn Cube - EU free shipping](https://s.click.aliexpress.com/e/_DDYrms7)
- [BLV mgn Cube - USA free shipping](https://s.click.aliexpress.com/e/_DB5a3Gr)
