---
title: Calibrations - BLV mgn Cube
description: BLV mgn Cube firmware update, configuration and calibration - Duet RepRap 3.x, stepper setup, PID tuning and optional calibrations.
---

# Calibrations

Before calibrating, make sure the right firmware is on the Duet board. When the project was released the Duet ran RepRap 2.x; it later moved to the Duet 3 board with RepRap 3.x. For the Duet 2 WiFi, our dear friend [David Husolo](https://www.facebook.com/groups/371460246914851/user/1208415623/) did amazing work on his BLV Cube config on GitHub: compatible, well-calibrated config files for both the Duet 2 WiFi and the Duet 3 running RepRap 3.x.

Several steps below point to the excellent Duet guides. With them you can calibrate your board and get to high-quality prints. (My fine-tuned config files were planned to be shared with the new FYSETC kit guide.)

## 1. Update the Duet firmware

Duet boards are the best documented boards, with step-by-step guides for almost anything. Update to the latest RepRap firmware 3.x before any calibration. The Duet 2 WiFi and the Duet 3 share the same update guide.

[:material-download: Download the firmware](https://github.com/Duet3D/RepRapFirmware/releases){ .md-button }
[Update guide](https://duet3d.dozuki.com/Wiki/Getting_Started_With_Duet_3#Section_Updating_Duet_3_main_board_firmware){ .md-button }

## 2. Copy the config files

Copy the BLV config files to the SD card. If the card is new or empty, follow [this guide](https://duet3d.dozuki.com/Wiki/SD_Card) first to rebuild the Duet SD card.

| Your setup | Config files |
| --- | --- |
| RepRap 3.x (recommended) | [David Husolo's GitHub](https://github.com/armysolo/BLV-Cube), in the "firmware" folder - thank you David for the amazing work! |
| FYSETC kit | [FYSETC firmware for the BLV mgn Cube](https://github.com/FYSETC/FYSETC-BLV-MGN-CUBE) |
| Old RepRap 2.x | The SD card ZIP in the project files (one ZIP is a basic Duet 3 config, the other is for RepRap 2.x only) |

## 3. Connect to the web interface

The Duet has a built-in web interface that gives you complete control of the printer. This guide helps you set up the network and access the board:

[Network setup guide](https://duet3d.dozuki.com/Wiki/Getting_Started_With_Duet_3#Section_Updating_Duet_3_main_board_firmware){ .md-button }

!!! danger "Do's and don'ts - avoid damaging your hardware"
    - Never disconnect cables from the Duet while it is powered, except the USB cable.
    - Check all wires and avoid shorts - especially fan, motor and heater wires.
    - Don't feed the board more than 24 volts.
    - Ground the extrusion frame and the bed carriage - and the motors too if you can.
    - Don't scratch, short or damage the electronics while installing them.
    - Don't remove the memory card while the printer is running.
    - Take your time crimping connectors and check the wires with a multimeter.
    - Triple check that "+" and "-" wires are plugged in properly and in the right place.
    - With the steppers connected, don't move an axis by hand fast enough to spin the motors quickly.

## 4. Configure your printer

The provided config files cover almost everything, but you may want final changes: centering the bed, motor directions, macro buttons, temperature presets per filament and so on. The [Duet guides](https://duet3d.dozuki.com/) cover all of this and more:

- [**Full Duet 2 WiFi guide**](https://duet3d.dozuki.com/Wiki/Step_by_step_guide)
- [**Full Duet 3 guide**](https://duet3d.dozuki.com/Wiki/Getting_Started_With_Duet_3)
- [**RepRap 3 overview**](https://duet3d.dozuki.com/Wiki/RepRapFirmware_3_overview) - must read

**Do these before the next step:**

- [Center your bed](https://duet3d.dozuki.com/Wiki/Centering_the_bed_or_setting_the_bed_origin)
- [Test your endstop switches](https://duet3d.dozuki.com/Wiki/Connecting_endstop_switches#Section_Test_endstop_switches)
- [Set up a different Z sensor](https://duet3d.dozuki.com/Wiki/Connecting_a_Z_probe) - only if you use another auto-leveling sensor
- [Set up a PT100 sensor](https://duet3d.dozuki.com/Wiki/Connecting_PT100_temperature_sensors) - only if you use a PT100 temperature sensor

### Stepper motors

With the FYSETC kit you can skip this: its plug-and-play cables are labeled, with the wires in the right order for the FYSETC config. If you bought the steppers from the BOM or have the Blurolls kit, the motors probably won't turn the right way (unless you're really lucky). Set them up like this:

![Stepper motors note](../assets/img/motors-steppers-note-min-8d41b50a.png){ width="560" }

1. **Identify the coil (phase) wires.** A stepper has 4 wires, 2 per coil, and you need to find the pairs - see this [quick guide](https://duet3d.dozuki.com/Wiki/Choosing_and_connecting_stepper_motors#Section_Identifying_the_stepper_motor_phases) or [this video](http://www.youtube.com/watch?v=S0pGKgos498).
2. **Connect the steppers** using the original Duet stepper wiring, shown in the bottom right corner of [wiring diagram v3.2](wiring.md) ("Duet original steppers wiring").
3. **Test and configure** them according to the [Duet documentation](https://duet3d.dozuki.com/Wiki/ConfiguringRepRapFirmwareCoreXYPrinter#Section_Movement_section). The video shows the expected movement for each command in the Duet guide.

!yt S0pGKgos498 | Easily identify the leads of a 4-wire stepper motor with a multimeter
!yt fPW-o5QJiSU | BLV mgn Cube 3D printer - steppers test

When the steppers are set up, check the motor directions: in this video I press the jog buttons by hand, and your printer should move the same way.

!yt OKzHyKRgO7I | BLV mgn Cube 3D printer - axis movement

**More guides:**

- [Tuning stepper motor drivers](https://duet3d.dozuki.com/Wiki/Tuning_Stepper_Motor_Drivers) - fully tune the Duet's TMC2660 drivers
- [Mesh bed compensation](https://duet3d.dozuki.com/Wiki/Using_mesh_bed_compensation) - to change the mesh settings
- [Multiple independent Z motors](https://duet3d.dozuki.com/Wiki/Bed_levelling_using_multiple_independent_Z_motors) - for true auto leveling
- [Filament sensor](https://duet3d.dozuki.com/Wiki/Connecting_and_configuring_filament-out_sensors)

## 5. Calibrate

These calibrations can't be skipped. Do them exactly as shown in the pictures, with maximum accuracy - they have a huge impact on the results.

![Mini IR sensor calibration](../assets/img/mini-ir-min-efb8fe55.jpg)

### Hotend PID

The picture shows the classic way to PID-tune the hotend. Newer RepRap 3.x releases add an algorithm that detects fan PWM changes and adjusts the heater in advance. To use it:

- Run the latest 3.x release.
- Define all your tools (T0) correctly.
- Define your fans according to the RRF instructions.
- Turn off the layer fan, then run `M303 T0 S200` - replace 200 with your normal printing temperature. The algorithm turns the fan on by itself while tuning.

In short: replace **`M303 H1 S190`** with **`M303 T0 S190`**.

<div class="gallery" markdown>
![Hotend PID](../assets/img/pid-min-609839b7.jpg)
![Bed PID](../assets/img/pid-bed-min-77f2da8f.jpg)
</div>

## Optional calibrations

Read each guide carefully before you enable the feature:

- [Reducing stand-still noise](https://duet3d.dozuki.com/Wiki/Reducing_Stand-Still_Noise) - quieter motors on standby
- [Stall detection and sensorless homing](https://duet3d.dozuki.com/Wiki/Stall_detection_and_sensorless_homing)
- [Pressure advance](https://duet3d.dozuki.com/Wiki/Pressure_advance) - compensates for the elasticity of the filament and extruder
- [Resume a print after a power failure](https://duet3d.dozuki.com/Wiki/Setting_up_to_resume_a_print_after_a_power_failure)
- [Accelerometer (experimental)](https://duet3d.dozuki.com/Wiki/Accelerometers) - find the ringing frequencies so DAA can reduce ringing

## Useful guides

- [Macros](https://duet3d.dozuki.com/Wiki/Macros) - macro scripts in RepRap firmware
- [External buttons and a custom web interface panel](https://duet3d.dozuki.com/Wiki/Using_M581_-_External_Triggers_and_Building_a_Control_Panel)
- [G-code dictionary](https://duet3d.dozuki.com/Wiki/Gcode) - every G-code RepRapFirmware supports, explained
- [Duet community projects](https://duet3d.dozuki.com/c/Community_Projects)

