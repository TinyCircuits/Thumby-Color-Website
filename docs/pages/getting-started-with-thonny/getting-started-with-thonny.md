This page will go through the steps to get started using **Thumby Color** or the **Thumby Color Dev Board** using the Thonny IDE.


## **Installing the Thonny IDE**
To edit code and upload files to your device, we'll use an application called Thonny.

Download and install Thonny for your platform <a href="https://thonny.org/" target="_blank" alt="View the RP2040 Arduino board package source">**here**</a> 

<center>
![](install_use_thonny_images/1_download_thonny.png)
</center>


## **Configuring Thonny**
First, open Thonny using your OS application finder:

<center>
![](install_use_thonny_images/2_open_thonny.png)
</center>

Next, go to **Tools > Options > Interpreter**:

<center>
![](install_use_thonny_images/3_tools_thonny.png)
</center>
<center>
![](install_use_thonny_images/4_options_thonny.png)
</center>
<center>
![](install_use_thonny_images/5_interpreter_thonny.png)
</center>

Once in the **Interpreter** menu, set the following:

* _Which kind of interpreter should Thonny use for running your code?_ -> **MicroPython (Raspberry Pi Pico)**
* _Port of WebREPL_ -> **< Try to detect port automatically >**
<center>
![](install_use_thonny_images/6_interpreter_options_thonny.png)
</center>

Exit all of those windows and Thonny is ready to use!


## **Using Thonny**
### Connecting
Plug your **Thumby Color** or **Thumby Color Dev Board** into your computer with a USB-C cable. Turn the device on by looking at the screen and sliding the power switch to the right.

Now that the device is on, open Thonny and left-click the **red stop sign** symbol in the upper left-hand corner to connect the device. The **Shell** window at the bottom will show **>>>** meaning it is connected (if you do not see the **Shell** pane, go to **View** and check **Shell**).
<center>
![](install_use_thonny_images/7_interpreter_connect_device_thonny.png)
</center>


### Managing Files
#### File Panes
Inside Thonny, you will notice the two panes on the left show your computer files (upper left pane) and your device files (lower left pane). If you do not see the panes, go to **View** and check **Files**:

<center>
![](install_use_thonny_images/8_file_panes_thonny.png)
</center>

#### Uploading Files/Folders
In the lower left pane, double left-click folders to navigate until you reach a spot where you want upload a file or folder:
<center>
![](install_use_thonny_images/9_file_traverse_into_Games.png)
</center>

Now do the same in the upper left pane until you reach the file/folder you want to upload:
<center>
![](install_use_thonny_images/10_file_traverse_into_Games_pc.png)
</center>

Right-click the item you want to upload and click **Upload to /Games**:
<center>
![](install_use_thonny_images/11_upload.png)
</center>

Wait while to upload transfers the files to the device:
<center>
![](install_use_thonny_images/12_wait_for_upload_thonny.png)
</center>

After the transfer is complete, navigate back out of folders by pressing the blue links in the pane titles:
<center>
![](install_use_thonny_images/13_navigate_up_thonny.png)
</center>

#### Downloading Files/Folders
The above works the opposite way: right-click files/folders in the lower left pane and click **Download to**

#### Deleting Files/Folders
Files and folders on the device can be deleted by right-clicking them in the lower left pane and choosing **Delete**

#### Creating Folders
In the lower left pane, right click anywhere and choose **New Directory...**