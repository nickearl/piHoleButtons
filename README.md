# piHoleButtons
## A Python script to control Pi-Hole using the Pimoroni Button Shim

*By Nick Earl
5/25/2018*


This is a small script I wrote to use a Pimoroni Button Shim to control Pi-Hole running on a Raspberry Pi.  The Button Shim
has five physical buttons (A through E) and an LED status indicator, and comes with a Python library to control it.
The buttons are programmed to call the `pihole` console command to enable or disable ad blocking.

To use this script, you'll need:

* Any recent Raspberry Pi with 40 GPIO pins (Model 1 B+ or later).  I used a Raspberry Pi Zero W
* Pimoroni Button Shim
* Software libraries for Pimoroni Button Shim (get these from https://github.com/pimoroni/button-shim)

See full instructions and example video at: https://www.nickearl.net/2018/05/27/controlling-pi-hole-with-physical-buttons/

The script programs the buttons as follows:

* Button A
    * Disables the Pi-Hole for 5 minutes.  The LED will blink continuously from yellow to orange.
* Button B
    * Disables the Pi-Hole for 30 minutes.  The LED will blink continuously from yellow to orange.
* Button C
    * Doesn't do anything in my script, but you could use the same logic as the other buttons to add your own
    custom disable time or other function here.
* Button D
    * Disables the Pi-Hole indefinitely.  The LED will blink red continuously on and off.
* Button E
    * Enables the Pi-Hole, if it's disabled.  The LED will blink green twice.


Feel free to use and modify this script as you see fit!
