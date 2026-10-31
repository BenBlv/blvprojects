---
title: Download & Print - BLV mgn Cube
description: Download the BLV mgn Cube project files (with or without the Metal Kit) and learn how to print the parts - filament, settings and orientation.
---

# Download & Print

## Download the project files

The project has had several updates, add-ons and improvements since its release. To make it easy to pick the right files, there are two downloads - choose by whether you have the [Metal Kit](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube).

<div class="grid cards" markdown>

-   **I have the Metal Kit**

    ---

    A lighter version of the original project ZIP, without the files you don't need with the [Metal Kit](https://benlevi8.wixsite.com/blvprojects/post/new-metal-kit-upgrade-blv-mgn-cube). Print only the [hotend setup and the front panels](#3d-printing-the-parts); all other parts are optional.

    [:material-download: Download - 35.5 MB](download:BLV-mgn-Cube-V1.15-Metal-Kit.zip){ .md-button .md-button--primary }

-   **I don't have the Metal Kit**

    ---

    The original project file with all the printable parts: documents, drawings, print profile, **CAD files**, printable **STL files** and more.

    [:material-download: Download - 50.8 MB](download:BLV-mgn-Cube-V1.15.zip){ .md-button .md-button--primary }

</div>

### What's in the ZIP

| Folder | Contents |
| --- | --- |
| **Documents** | PDF files with most of the information needed for the project |
| **Firmware** | SD card content for the Duet / RepRap board: **Duet 2 WiFi** - the original configuration (firmware 2.xx+) · **Duet 3** - basic configuration (RepRap 3.xx+) |
| **Frame Panels** | All the measurements for making enclosure panels |
| **open source** | The original CAD files, including a few new add-ons and upgrades |
| **Slicing Profiles** | Simplify3D profile. Cura has a built-in BLV mgn Cube profile. (A PrusaSlicer profile was planned.) |
| **STL files to print** | All the STL files, including optional add-ons, upgrades and custom mounts - see below |

??? info "STL folders in detail"
    | Folder | Description |
    | --- | --- |
    | Bed Holder For Anet E12 Bed | Bed carriage mounts for the Anet E12 heated bed |
    | Bed Holder For CR-10 Bed | Bed carriage mounts for the Creality CR-10 heated bed |
    | Biqu H2 extruder adapter For Metal kit | BIQU H2 extruder adapter and fan mount for the Metal Kit |
    | BLV optic Led cable concept | Concept add-on that reflects the Duet indicator lights to the front - no soldering |
    | Chimera front plate adapter | For the Chimera hotend |
    | Direct Drive | Direct drive upgrade |
    | Frame wires Holder | Printed wire clip for 2040/2020 extrusions - 3 sizes |
    | Front Panel | All STL and PDF files for the front panel |
    | Hotend Setup for Metal kit | The new hotend setup for the Metal Kit - more upgrades in the community remixes |
    | Jigs | Main installation jig + 2 jigs for fixing rails on 2020 and 2040 |
    | Nozzle cleaner - Brass Brush | For the BIQU H2 extruder |
    | Nozzle cleaner - new silicone wiper | For the BIQU H2 extruder |
    | Optional - Air scrabber | Small air scrubbers that filter printing fumes |
    | Optional - BIG Air scrabber | Big, effective air scrubbers |
    | Original Bowden Hotend | The original full hotend setup (not for the Metal Kit) |
    | Side LED diffusers | Files for the side-mounted LED lights |
    | Trianglelab Matrix adapter For Metal kit | Trianglelab Matrix extruder adapter for the Metal Kit |
    | Twin fans Bowden Hotend | Upgraded part cooling with dual 4010 blowers |
    | Zesty Nimble | Adapter for the Zesty Nimble extruder - left and right versions |
    | ... | and all the other STL files |

## 3D printing the parts

How you print the parts has a huge impact on how they work, so follow the instructions closely: orientation, number of walls, printing angle, filament type and even print speed all matter. Most parts are designed to print without supports.

??? question "Can I buy a kit of printed parts?"
    Not everyone has a printer available or the time to print all the parts. Print services are usually expensive because they charge by print time. A cheaper option: an AliExpress store sells [BLV mgn Cube printed parts](https://s.click.aliexpress.com/e/_996qwz) in green PETG with 80% infill - a good solution if you have neither the time nor a printer.

    [3D printed parts for BLV mgn Cube](https://s.click.aliexpress.com/e/_996qwz){ .md-button }

### Filament

The parts must handle stress, pushing forces and heat.

| Filament | Notes |
| --- | --- |
| **PETG** | What I used |
| **PETG Carbon** | Very rigid; needs a hardened steel nozzle |
| ABS | Needs an enclosure; toxic fumes |
| PA12 | MJF / SLS printed |

!!! danger "Don't use PLA / PLA+"
    The parts will deform from the heat inside the printer.

### Print settings

- At least **6 outer walls / perimeters**
- **7 bottom** layers and **7 top** layers
- Most parts need **80%+ infill** - the sketches below show the exact infill for each part

### Orientation

The orientation of a part on the bed has a huge effect on its strength. The image shows exactly how to place every part. Some parts need supports, such as the tensioner idler holder - check before you hit print. Labels like X90 or Y-90 are the rotation to apply to the part.

![Print orientation of all the parts](../assets/img/orinetation-1d97169f.jpg)

## Parts descriptions

Each sketch shows a set of parts with the part name, material and infill. If a sketch contradicts the settings above, the settings above win (6 walls, 7 bottom, 7 top layers).

<div class="gallery" markdown>
![Front panel](../assets/img/blv-mgn-cube-front-panel-7bd15118.jpg)
![Rear corners and bearings](../assets/img/blv-cube-mgn-project-rear-corners-and-be-3a099c74.jpg)
![Hotend](../assets/img/img-a4d339fb.jpg)
![Tensioner and X mount](../assets/img/blv-mgn-cube-front-tensioner-b2defd33.jpg)
![Zesty Nimble drawing](../assets/img/img-be9a2f99.jpg)
![BMG direct drive](../assets/img/img-9402628b.jpg)
</div>

