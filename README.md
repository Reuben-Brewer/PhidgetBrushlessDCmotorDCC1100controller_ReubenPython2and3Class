########################  

PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class

Wrapper (including ability to hook to Tkinter GUI) to control 1 brushless/BLDC motor with Hall Effect sensors (via VINT). 
Supports both velocity and position control modes.

From Phidgets' website:
"The DCC1100 requires an 8-30V DC power supply and can control one brushless DC motor. The motor must have hall-effect feedback for this controller to function. The DCC1100 has a 5-pin Molex connector to interface with the motor's hall-effect output. This Phidget connects to your computer through a VINT Hub."

Brushless DC Motor Phidget
ID: DCC1100_0
https://www.phidgets.com/?tier=3&catid=64&pcid=57&prodid=1013

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision D, 11/12/2021

Verified working on: 

Python 2.7, 3.8

Windows 8.1, 10 64-bit

Raspberry Pi Buster 

(no Mac testing yet)

*NOTE THAT YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.*

########################  

########################### Python module installation instructions, all OS's

https://pypi.org/project/Phidget22/#files

To install the Python module using pip:
pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"

###########################

########################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

###########################

########################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

###########################

########################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -
sudo apt-get install -y libphidget22
 
###########################
