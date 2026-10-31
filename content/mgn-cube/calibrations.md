---
title: Calibrations - BLV mgn Cube
description: BLV mgn Cube firmware update, configuration and calibration. Duet RepRap 3.x, stepper setup, PID tuning and optional features.
---

# Calibrations

Before calibrating, make sure the Duet board runs the right firmware. The project was released on RepRap 2.x and later moved to the Duet 3 board with RepRap 3.x. Community member [David Husolo](https://www.facebook.com/groups/371460246914851/user/1208415623/) published well-tuned BLV Cube configuration files on GitHub for both the Duet 2 WiFi and the Duet 3 running RepRap 3.x.

Several steps below point to the official Duet guides, which cover calibration in detail.

## 1. Update the Duet firmware

Duet boards are very well documented, with step-by-step guides for almost every task. Update to the latest RepRap firmware 3.x before calibrating. The Duet 2 WiFi and the Duet 3 use the same update guide.

[:material-download: Download the firmware](https://github.com/Duet3D/RepRapFirmware/releases){ .md-button }
[Update guide](https://duet3d.dozuki.com/Wiki/Getting_Started_With_Duet_3#Section_Updating_Duet_3_main_board_firmware){ .md-button }

## 2. Copy the config files

Copy the BLV configuration files to the SD card. If the card is new or empty, first prepare it with [this guide](https://duet3d.dozuki.com/Wiki/SD_Card).

| Your setup | Config files |
| --- | --- |
| RepRap 3.x (recommended) | [David Husolo's GitHub](https://github.com/armysolo/BLV-Cube), "firmware" folder. Thank you David! |
| FYSETC parts set | [FYSETC firmware for the BLV mgn Cube](https://github.com/FYSETC/FYSETC-BLV-MGN-CUBE) |
| RepRap 2.x | The SD card ZIP in the project files. One ZIP is a basic Duet 3 configuration, the other is for RepRap 2.x only. |

## 3. Connect to the web interface

The Duet has a built-in web interface with full control of the printer. This guide explains the network setup:

[Network setup guide](https://duet3d.dozuki.com/Wiki/Getting_Started_With_Duet_3#Section_Updating_Duet_3_main_board_firmware){ .md-button }

!!! danger "Avoid damaging the hardware"
    - Never disconnect cables from a powered Duet, except the USB cable.
    - Check all wires for shorts, especially fan, motor and heater wires.
    - Don't feed the board more than 24 volts.
    - Ground the frame and the bed carriage, and the motors if possible.
    - Don't scratch, short or damage the electronics while installing them.
    - Don't remove the memory card while the printer is running.
    - Take your time crimping connectors and check the wires with a multimeter.
    - Triple check the polarity and position of every connection.
    - With the steppers connected, don't move an axis quickly by hand.

## 4. Configure your printer

The provided configuration covers almost everything. You may still want to center the bed, set motor directions, add macro buttons or define temperature presets per filament. The [Duet guides](https://duet3d.dozuki.com/) cover all of this:

- [**Full Duet 2 WiFi guide**](https://duet3d.dozuki.com/Wiki/Step_by_step_guide)
- [**Full Duet 3 guide**](https://duet3d.dozuki.com/Wiki/Getting_Started_With_Duet_3)
- [**RepRap 3 overview**](https://duet3d.dozuki.com/Wiki/RepRapFirmware_3_overview), essential reading

**Complete these before moving on:**

- [Center your bed](https://duet3d.dozuki.com/Wiki/Centering_the_bed_or_setting_the_bed_origin)
- [Test your endstop switches](https://duet3d.dozuki.com/Wiki/Connecting_endstop_switches#Section_Test_endstop_switches)
- [Set up a different Z probe](https://duet3d.dozuki.com/Wiki/Connecting_a_Z_probe), only for other probe types
- [Set up a PT100 sensor](https://duet3d.dozuki.com/Wiki/Connecting_PT100_temperature_sensors), only with a PT100

### Stepper motors

With the FYSETC parts set you can skip this, since its labeled cables match the FYSETC configuration. With steppers from the BOM or the Blurolls set, the motors will probably turn the wrong way at first. Set them up like this:

![Stepper motors note](../assets/img/motors-steppers-note-min-8d41b50a.png){ width="560" }

1. **Identify the coil pairs.** A stepper has 4 wires, 2 per coil. This [short guide](https://duet3d.dozuki.com/Wiki/Choosing_and_connecting_stepper_motors#Section_Identifying_the_stepper_motor_phases) and [this video](http://www.youtube.com/watch?v=S0pGKgos498) show how to find them.
2. **Connect the steppers** using the original Duet stepper wiring, shown in the bottom right corner of [wiring diagram v3.2](wiring.md) under "Duet original steppers wiring".
3. **Test and configure** them with the [Duet documentation](https://duet3d.dozuki.com/Wiki/ConfiguringRepRapFirmwareCoreXYPrinter#Section_Movement_section). The video shows the expected movement for each test command.

!yt S0pGKgos498 | Easily identify the leads of a 4-wire stepper motor with a multimeter
!yt fPW-o5QJiSU | BLV mgn Cube 3D printer - steppers test

Then check the directions. In this video I press the jog buttons, and your printer should move the same way.

!yt OKzHyKRgO7I | BLV mgn Cube 3D printer - axis movement

**More guides:**

- [Tuning stepper motor drivers](https://duet3d.dozuki.com/Wiki/Tuning_Stepper_Motor_Drivers) for the Duet's TMC2660 drivers
- [Mesh bed compensation](https://duet3d.dozuki.com/Wiki/Using_mesh_bed_compensation) to change the mesh settings
- [Multiple independent Z motors](https://duet3d.dozuki.com/Wiki/Bed_levelling_using_multiple_independent_Z_motors) for true auto leveling
- [Filament sensor](https://duet3d.dozuki.com/Wiki/Connecting_and_configuring_filament-out_sensors)

## 5. Calibrate

These calibrations are mandatory. Follow the pictures exactly and work accurately, since they have a large effect on print quality.

![Mini IR sensor calibration](../assets/img/mini-ir-min-efb8fe55.jpg)

### Hotend PID

The picture shows the classic hotend PID tuning. Newer RepRap 3.x releases add an algorithm that detects fan speed changes and adjusts the heater in advance. To use it:

- Run the latest 3.x release.
- Define all your tools (T0) correctly.
- Define your fans according to the RRF instructions.
- Turn off the part cooling fan and run `M303 T0 S200`, with 200 replaced by your usual printing temperature. The algorithm turns the fan on by itself during tuning.

In short, replace **`M303 H1 S190`** with **`M303 T0 S190`**.

<div class="gallery" markdown>
![Hotend PID](../assets/img/pid-min-609839b7.jpg)
![Bed PID](../assets/img/pid-bed-min-77f2da8f.jpg)
</div>

## Optional calibrations

Read each guide before enabling the feature:

- [Reducing stand-still noise](https://duet3d.dozuki.com/Wiki/Reducing_Stand-Still_Noise) for quieter idle motors
- [Stall detection and sensorless homing](https://duet3d.dozuki.com/Wiki/Stall_detection_and_sensorless_homing)
- [Pressure advance](https://duet3d.dozuki.com/Wiki/Pressure_advance) to compensate for filament and extruder elasticity
- [Resume a print after a power failure](https://duet3d.dozuki.com/Wiki/Setting_up_to_resume_a_print_after_a_power_failure)
- [Accelerometer (experimental)](https://duet3d.dozuki.com/Wiki/Accelerometers) to measure ringing frequencies for DAA

## Useful guides

- [Macros](https://duet3d.dozuki.com/Wiki/Macros) in RepRap firmware
- [External buttons and a custom web interface panel](https://duet3d.dozuki.com/Wiki/Using_M581_-_External_Triggers_and_Building_a_Control_Panel)
- [G-code dictionary](https://duet3d.dozuki.com/Wiki/Gcode) with every G-code RepRapFirmware supports
- [Duet community projects](https://duet3d.dozuki.com/c/Community_Projects)

