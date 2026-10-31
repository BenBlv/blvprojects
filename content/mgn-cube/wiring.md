---
title: Wiring - BLV mgn Cube
description: BLV mgn Cube wiring diagrams for Duet 2 WiFi, Duet 3 and the FYSETC kit - fans, Neopixel rings, BLTouch and power relay.
---

# Wiring

Wiring is a critical step - double check every wire you install. It takes about 3 hours, sometimes more. With the FYSETC kit it takes about an hour: the kit has an optimized wiring diagram, all cables ready, stepper wires in the right order, labeled and with plugs, and a unique PCB for the Neopixel rings (5 minutes, plug and play, based on the original Neopixel project). **Make sure you follow the diagram for your setup.**

!!! warning "Before you start"
    - Wire the printer with the AC plug **disconnected** from any power source.
    - Crimp every cable that goes into the PSU (FYSETC kit cables are pre-crimped).
    - Don't mix negative and positive wires.
    - Double check every wire.

Click any diagram to enlarge it.

=== "Duet 2 WiFi"

    ![Duet WiFi wiring v3.2](../assets/img/duetwifi-wiring-v3-2-min-726cd8fc.jpg)

    **12V fans on a 24V system** - if your fans are rated 12V, this is the right way to wire them on 24V without damaging the board or the fans:

    ![12V fans on a 24V system](../assets/img/wiring-12v-fan-on-24v-system-min-b60ba6b7.jpg){ width="560" }

    **Neopixel rings** - installed on the front panel, they show the printer status with animations.

    ![Neopixel wiring v2.2b](../assets/img/neopixel-wiring-v2-2b-0e2f25f7.jpg){ width="560" }

    Arduino code for the rings:

    - [Most recent code by Claus Noack](https://github.com/mule1972/NeoPixelBLVmgn) - confirmed working
    - [First alpha version by Mimasx](https://github.com/mimasx/BLV_NeoPixelIntegration)

=== "Duet 3 6HC"

    If you have the Duet 3 board, this is your wiring diagram:

    ![Duet 3 wiring](../assets/img/ben-levi-duet-3-wiring-39114e2e.jpg)

=== "FYSETC kit only"

    **Optimized wiring for the FYSETC kit:**

    ![FYSETC general wiring](../assets/img/general-3f911e31.jpg)

    **BLTouch** - the FYSETC kit comes with a BLTouch auto-leveling sensor:

    ![FYSETC BLTouch wiring](../assets/img/blv-kit-fysetc-bltouch-402ee7f9.jpg){ width="560" }

    **Power button - relay module:**

    ![PSU relay wiring](../assets/img/psu-ba3b3d91.jpg){ width="560" }

    **FYSETC BLV Neopixel module** - a 5-minute install. All cables are ready, the Neopixels come with soldered pins, and the 2-pin and 3-pin plugs can't go wrong. Piece of cake!

    ![BLV Neopixel module wiring](../assets/img/blv-neopixle-wiring-43d764cd.jpg){ width="560" }

