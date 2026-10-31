---
title: Wiring - BLV mgn Cube
description: BLV mgn Cube wiring diagrams for Duet 2 WiFi, Duet 3 and the FYSETC parts set. Fans, Neopixel rings, BLTouch and the power relay.
---

# Wiring

Wiring is a critical step, so double check every wire. It usually takes about 3 hours. With the FYSETC parts set it takes about an hour, since that set came with an optimized diagram, ready-made labeled cables with plugs, stepper wires in the correct order and a plug-and-play PCB for the Neopixel rings. **Follow the diagram that matches your setup.**

!!! warning "Before you start"
    - Wire the printer with the AC plug **disconnected**.
    - Crimp every cable that goes into the power supply.
    - Don't mix negative and positive wires.
    - Double check every wire.

Click a diagram to open it full size. Zoom in to read the pin labels.

=== "Duet 2 WiFi"

    Three diagrams: the main wiring (v3.2), **12V fans on a 24V system** (wire 12V fans this way to protect the board and the fans), and the **Neopixel rings** on the front panel that show the printer status with animations. Arduino code for the rings: [latest code by Claus Noack](https://github.com/mule1972/NeoPixelBLVmgn) (confirmed working) or the [first alpha by Mimasx](https://github.com/mimasx/BLV_NeoPixelIntegration).

    <div class="gallery big contain" markdown>
    ![Duet WiFi wiring v3.2](../assets/img/duetwifi-wiring-v3-2-min-726cd8fc.jpg)
    ![12V fans on a 24V system](../assets/img/wiring-12v-fan-on-24v-system-min-b60ba6b7.jpg)
    ![Neopixel wiring v2.2b](../assets/img/neopixel-wiring-v2-2b-0e2f25f7.jpg)
    </div>

=== "Duet 3 6HC"

    Wiring diagram for the Duet 3 6HC board. Fans, heaters and the Neopixel rings follow the same logic as the Duet 2 diagrams.

    <div class="gallery big contain" markdown>
    ![Duet 3 wiring](../assets/img/ben-levi-duet-3-wiring-39114e2e.jpg)
    </div>

=== "FYSETC parts set"

    Four diagrams for the FYSETC parts set: the optimized general wiring, the **BLTouch** auto-leveling sensor, the **power button with relay module**, and the **FYSETC BLV Neopixel module**. The Neopixel module is a 5-minute install: the cables are ready, the rings come with soldered pins, and the 2-pin and 3-pin plugs only fit one way.

    <div class="gallery big contain" markdown>
    ![FYSETC general wiring](../assets/img/general-3f911e31.jpg)
    ![FYSETC BLTouch wiring](../assets/img/blv-kit-fysetc-bltouch-402ee7f9.jpg)
    ![PSU relay wiring](../assets/img/psu-ba3b3d91.jpg)
    ![BLV Neopixel module wiring](../assets/img/blv-neopixle-wiring-43d764cd.jpg)
    </div>

