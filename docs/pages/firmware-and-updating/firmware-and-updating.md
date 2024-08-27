## Latest Firmware

<a href="https://color.thumby.us/firmware_2aa8e3d.uf2" target="_blank" alt="Firmware">**Download Latest MicroPython/Engine Firmware**</a> or the system <a href="https://github.com/TinyCircuits/TinyCircuits-Tiny-Game-Engine/tree/2aa8e3dd9eb6ded5479c19bf0fb504f0ecfba3b5" target="_blank" alt="Firmware">**files**</a> (August 27, 2024 @ 2:10PM EDT [commit 2aa8e3d])

* Fixed "__init_save_dir was never called" error
* Added some helpful `engine` API functions to help support legacy Thumby Games
* Switched `engine.reset()` to do a hard reset by default instead of soft (pass `True` to perform a soft reset)
* Fixed engine not returning correct exit code on hard reset for `micropython_loop` script to restart


### Old Firmware

<a href="https://color.thumby.us/firmware_4d64d5b.uf2" target="_blank" alt="Firmware">**Download MicroPython/Engine Firmware**</a> or the system <a href="https://github.com/TinyCircuits/TinyCircuits-Tiny-Game-Engine/archive/4d64d5b3fe43fa09e07447da160eedb603ae3c8c.zip" target="_blank" alt="Firmware">**files**</a> (August 26, 2024 @ 2:22PM EDT [commit 4d64d5b])

* Added small delay to processor startup to help solve issue where some units did not startup every time
* Fixed issue where engine scratch space couldn't be used completely
* Fixed issue where device was not hard reset after a game ends
* Fixed issue where "__init_save_dir was already called error" happened after a soft reset 

---

<a href="https://color.thumby.us/firmware_917b0b0.uf2" target="_blank" alt="Firmware">**Download MicroPython/Engine Firmware**</a> or the system <a href="https://github.com/TinyCircuits/TinyCircuits-Tiny-Game-Engine/archive/917b0b038294011df253e861f74b6f2657776a70.zip" target="_blank" alt="Firmware">**files**</a> (August 23, 2024 @ 12:20PM EDT [commit 917b0b0])

* Initial public update for small bugfixes


## Updating
1. Download the **latest** firmware above
2. Plug **Thumby Color** or **Thumby Color Dev Kit** into a computer
3. Turn the device off (switch to the **left** when looking at the screen)
4. Press and hold the down DPAD direction and switch the device back on
5. Open a file manager and copy and paste the downloaded **.uf2** to the **RP2350** device in your file manager

The above steps update the firmware, however, the system files should be updated too. Do the following:

1. Download the engine and system files using the **files** download links above
2. Extract/unzip the downloaded folder using your file manager
3. Plug a USB-C cable into the device and into your computer
4. Open Thonny and press the red stop sign button to connect (see "Getting Started With Thonny" above for more help)
5. In the **bottom-left** pane of Thonny:
    1. Right-click `main.py` and click `Delete`
    2. Right-click `system` and click `Delete`
6.  In the **top-left** pane of Thonny:
    1. Navigate inside the downlaoded and extracted folder to `TinyCircuits-Tiny-Game-Engine/filesystem`
    2. Right-click `main.py` and click `Upload to /`
    3. Right-click `system` and click `Upload to /`
7. Turn the device off and back on