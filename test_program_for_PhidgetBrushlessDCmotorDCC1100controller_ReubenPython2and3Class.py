# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision F, 05/10/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###########################################################
from PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
###########################################################

###########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###########################################################

###########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

    number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

    ListOfStringsToJoin = []

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if isinstance(input, str) == 1:
        ListOfStringsToJoin.append(input)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
        element = float(input)
        prefix_string = "{:." + str(number_of_decimal_places) + "f}"
        element_as_string = prefix_string.format(element)

        ##########################################################################################################
        ##########################################################################################################
        if element >= 0:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
            element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
        else:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
        ##########################################################################################################
        ##########################################################################################################

        ListOfStringsToJoin.append(element_as_string)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, list) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append(ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, tuple) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append("TUPLE" + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, dict) == 1:

        if len(input) > 0:
            for Key in input: #RECURSION
                ListOfStringsToJoin.append(str(Key) + ": " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a dict()
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    else:
        ListOfStringsToJoin.append(str(input))
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if len(ListOfStringsToJoin) > 1:

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        StringToReturn = ""
        for Index, StringToProcess in enumerate(ListOfStringsToJoin):

            ################################################
            if Index == 0: #The first element
                if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                    StringToReturn = "{"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                    StringToReturn = "("
                else:
                    StringToReturn = "["

                StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
            ################################################

            ################################################
            elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                StringToReturn = StringToReturn + StringToProcess + ", "
            ################################################

            ################################################
            else: #The last element
                StringToReturn = StringToReturn + StringToProcess

                if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                    StringToReturn = StringToReturn + "}"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                    StringToReturn = StringToReturn + ")"
                else:
                    StringToReturn = StringToReturn + "]"

            ################################################

        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    elif len(ListOfStringsToJoin) == 1:
        StringToReturn = ListOfStringsToJoin[0]

    else:
        StringToReturn = ListOfStringsToJoin

    return StringToReturn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertDictToProperlyFormattedStringForPrinting(DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

    ProperlyFormattedStringForPrinting = ""
    ItemsPerLineCounter = 0

    for Key in DictToPrint:

        if isinstance(DictToPrint[Key], dict): #RECURSION
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ": " + \
                                                 ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)

        if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
            ItemsPerLineCounter = ItemsPerLineCounter + 1
        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
            ItemsPerLineCounter = 0

    return ProperlyFormattedStringForPrinting
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG
    global MostRecentDict_Label

    global PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject
    global PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG
    global SHOW_IN_GUI_PhidgetBrushlessDCmotorDCC1100controller_FLAG
    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            MostRecentDict_Label["text"] = ConvertDictToProperlyFormattedStringForPrinting(
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict,
                NumberOfDecimalsPlaceToUse=3,
                NumberOfEntriesPerLine=1,
                NumberOfTabsBetweenItems=1)
            #########################################################

            #########################################################
            if PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG == 1 and SHOW_IN_GUI_PhidgetBrushlessDCmotorDCC1100controller_FLAG == 1:
                PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetBrushlessDCmotorDCC1100controller
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_PhidgetBrushlessDCmotorDCC1100controller = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_PhidgetBrushlessDCmotorDCC1100controller, text='   BLDC   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_PhidgetBrushlessDCmotorDCC1100controller = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    global MostRecentDict_Label
    MostRecentDict_Label = Label(Tab_MainControls, text="MostRecentDict_Label", width=120, font=("Helvetica", 10))
    MostRecentDict_Label.grid(row=0, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_PhidgetBrushlessDCmotorDCC1100controller_FLAG
    USE_PhidgetBrushlessDCmotorDCC1100controller_FLAG = 1

    global USE_PhidgetBrushlessDCmotorDCC1100controller_SINUSOIDAL_INPUT_FLAG
    USE_PhidgetBrushlessDCmotorDCC1100controller_SINUSOIDAL_INPUT_FLAG = 1

    global USE_PhidgetBrushlessDCmotorDCC1100controller_POSITION_CONTROL_FLAG
    USE_PhidgetBrushlessDCmotorDCC1100controller_POSITION_CONTROL_FLAG = 1 #SET TO 0 FOR VELOCITY CONTROL

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_PhidgetBrushlessDCmotorDCC1100controller_FLAG
    SHOW_IN_GUI_PhidgetBrushlessDCmotorDCC1100controller_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_PhidgetBrushlessDCmotorDCC1100controller
    global GUI_COLUMN_PhidgetBrushlessDCmotorDCC1100controller
    global GUI_PADX_PhidgetBrushlessDCmotorDCC1100controller
    global GUI_PADY_PhidgetBrushlessDCmotorDCC1100controller
    global GUI_ROWSPAN_PhidgetBrushlessDCmotorDCC1100controller
    global GUI_COLUMNSPAN_PhidgetBrushlessDCmotorDCC1100controller
    GUI_ROW_PhidgetBrushlessDCmotorDCC1100controller = 1

    GUI_COLUMN_PhidgetBrushlessDCmotorDCC1100controller = 0
    GUI_PADX_PhidgetBrushlessDCmotorDCC1100controller = 1
    GUI_PADY_PhidgetBrushlessDCmotorDCC1100controller = 10
    GUI_ROWSPAN_PhidgetBrushlessDCmotorDCC1100controller = 1
    GUI_COLUMNSPAN_PhidgetBrushlessDCmotorDCC1100controller = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 10
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetBrushlessDCmotorDCC1100controller
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 2.0

    global SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl
    SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl = -50.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl
    SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl = 50.0

    global SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl
    SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl = -1.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl
    SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl = 1.0
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject

    global PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG
    PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG = -1

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict = dict()

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Position_PhidgetsUnits_FromDevice
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Position_PhidgetsUnits_FromDevice = -11111.0

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_FromDevice
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_FromDevice = -11111.0

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw = -11111.0

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed = -11111.0

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice = -11111.0

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Temperature_DegC_FromDevice
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Temperature_DegC_FromDevice = -11111.0

    global PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Time
    PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_PhidgetBrushlessDCmotorDCC1100controller = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################

    #################################################
    global PhidgetBrushlessDCmotorDCC1100controller_GUIparametersDict
    PhidgetBrushlessDCmotorDCC1100controller_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_PhidgetBrushlessDCmotorDCC1100controller_FLAG),
                                    ("root", Tab_PhidgetBrushlessDCmotorDCC1100controller),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_PhidgetBrushlessDCmotorDCC1100controller),
                                    ("GUI_COLUMN", GUI_COLUMN_PhidgetBrushlessDCmotorDCC1100controller),
                                    ("GUI_PADX", GUI_PADX_PhidgetBrushlessDCmotorDCC1100controller),
                                    ("GUI_PADY", GUI_PADY_PhidgetBrushlessDCmotorDCC1100controller),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_PhidgetBrushlessDCmotorDCC1100controller),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_PhidgetBrushlessDCmotorDCC1100controller)])
    #################################################

    #################################################
    global PhidgetBrushlessDCmotorDCC1100controller_setup_dict_PositionControl
    PhidgetBrushlessDCmotorDCC1100controller_setup_dict_PositionControl = dict([("GUIparametersDict", PhidgetBrushlessDCmotorDCC1100controller_GUIparametersDict),
                            ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                            ("VINT_DesiredSerialNumber", -1), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                            ("VINT_DesiredPortNumber", 0), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                            ("DesiredDeviceID", 108),
                            ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                            ("NameToDisplay_UserSet", "Reuben's Test BLDC Controller"),
                            ("ENABLE_GETS_MAINTHREAD", 1),
                            ("FailsafeTime_Milliseconds", 10000),
                            ("MainThread_TimeToSleepEachLoop", 0.001),
                            ("ControlMode", "position"),  #position or velocity, AFTER SWITCHING ControlMode, YOU SOMETIMES NEED TO RUN PYTHON FILE ONCE AND THEN POWER-CYCLE BOARD FOR EFFECT TO TAKE
                            ("VelocityMinLimit_PhidgetsUnits_UserSet", 0.0),
                            ("VelocityMaxLimit_PhidgetsUnits_UserSet", 10000.0),
                            ("VelocityStallLimit_PhidgetsUnits_UserSet", 15.0),  #Setting StallVelocity to 0 will turn off stall protection functionality
                            ("BrakingStrengthLimit_VelControl_Percent_UserSet", 100.0),
                            ("AccelerationMaxLimit_PhidgetsUnits_UserSet", 100000.0),
                            ("PositionMinLimit_PhidgetsUnits_UserSet", -1000.0),
                            ("PositionMaxLimit_PhidgetsUnits_UserSet", 1000.0),
                            ("Kp_PosControl_Gain_UserSet", 20000.0),  #IF MOTOR-CONTROL FAILS, THEN TRY ALL-NEGATIVE-GAIN-VALUES (Kp, Ki, and KD)!
                            ("Ki_PosControl_Gain_UserSet", 2.0),  #IF MOTOR-CONTROL FAILS, THEN TRY ALL-NEGATIVE-GAIN-VALUES (Kp, Ki, and KD)!
                            ("Kd_PosControl_Gain_UserSet", 40000.0),  #IF MOTOR-CONTROL FAILS, THEN TRY ALL-NEGATIVE-GAIN-VALUES (Kp, Ki, and KD)!
                            ("DeadBand_PosControl_PhidgetsUnits_UserSet", 10.0),  #Lower DeadBand value is a tighter Position loop (allows less error)
                            ("RescaleFactor_MultipliesPhidgetsUnits_UserSet", 1.0),
                            ("UpdateDeltaT_ms", 20)]) #100 min for velocity, 20 min for position
    #################################################

    #################################################
    global PhidgetBrushlessDCmotorDCC1100controller_setup_dict_VelocityControl
    PhidgetBrushlessDCmotorDCC1100controller_setup_dict_VelocityControl = dict([("GUIparametersDict", PhidgetBrushlessDCmotorDCC1100controller_GUIparametersDict),
                            ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                            ("VINT_DesiredSerialNumber", -1), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                            ("VINT_DesiredPortNumber", 0), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                            ("DesiredDeviceID", 108),
                            ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                            ("NameToDisplay_UserSet", "Reuben's Test BLDC Controller"),
                            ("ENABLE_GETS_MAINTHREAD", 1),
                            ("FailsafeTime_Milliseconds", 10000),
                            ("MainThread_TimeToSleepEachLoop", 0.001),
                            ("ControlMode", "velocity"),  #position or velocity, AFTER SWITCHING ControlMode, MUST RUN PYTHON FILE ONCE AND THEN POWER-CYCLE BOARD FOR EFFECT TO TAKE
                            ("VelocityMinLimit_PhidgetsUnits_UserSet", -1.0),
                            ("VelocityMaxLimit_PhidgetsUnits_UserSet", 1.0),
                            ("VelocityStallLimit_PhidgetsUnits_UserSet", 15.0),  #Setting StallVelocity to 0 will turn off stall protection functionality
                            ("BrakingStrengthLimit_VelControl_Percent_UserSet", 100.0),
                            ("AccelerationMaxLimit_PhidgetsUnits_UserSet", 100.0),
                            ("PositionMinLimit_PhidgetsUnits_UserSet", -1000.0),
                            ("PositionMaxLimit_PhidgetsUnits_UserSet", 1000.0),
                            ("Kp_PosControl_Gain_UserSet", 20000.0),  #IF MOTOR-CONTROL FAILS, THEN TRY ALL-NEGATIVE-GAIN-VALUES (Kp, Ki, and KD)!
                            ("Ki_PosControl_Gain_UserSet", 2.0),  #IF MOTOR-CONTROL FAILS, THEN TRY ALL-NEGATIVE-GAIN-VALUES (Kp, Ki, and KD)!
                            ("Kd_PosControl_Gain_UserSet", 40000.0),  #IF MOTOR-CONTROL FAILS, THEN TRY ALL-NEGATIVE-GAIN-VALUES (Kp, Ki, and KD)!
                            ("DeadBand_PosControl_PhidgetsUnits_UserSet", 10.0),  #Lower DeadBand value is a tighter Position loop (allows less error)
                            ("RescaleFactor_MultipliesPhidgetsUnits_UserSet", 1.0),
                            ("UpdateDeltaT_ms", 100)]) #100 min for velocity, 20 min for position
    #################################################

    if USE_PhidgetBrushlessDCmotorDCC1100controller_FLAG == 1:
        try:

            if USE_PhidgetBrushlessDCmotorDCC1100controller_POSITION_CONTROL_FLAG == 1:
                PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class(PhidgetBrushlessDCmotorDCC1100controller_setup_dict_PositionControl)

            else:
                PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class(PhidgetBrushlessDCmotorDCC1100controller_setup_dict_VelocityControl)

            PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PhidgetBrushlessDCmotorDCC1100controller_FLAG == 1 and PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG != 1:
        print("Failed to open PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    ################################################# SHOWS HOW TO OFFSET THE ANGLE
    #################################################
    #if USE_PhidgetBrushlessDCmotorDCC1100controller_FLAG == 1:
    #    if PhidgetBrushlessDCmotorDCC1100controller_setup_dict["ControlMode"] == "position":
    #        time.sleep(0.5)
    #        PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.SetPositionOffsetOnBoardWithoutMoving(90)
    #################################################
    #################################################

    #################################################
    #################################################
    #################################################
    print("Starting main loop 'test_program_for_PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        #################################################
        #################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        #################################################
        #################################################

        ################################################# GET's
        #################################################
        if PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG == 1:

            PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict:
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Position_PhidgetsUnits_FromDevice = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["Position_PhidgetsUnits_FromDevice"]
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_FromDevice = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["Velocity_PhidgetsUnits_FromDevice"]
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["Velocity_PhidgetsUnits_DifferentiatedRaw"]
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["Velocity_PhidgetsUnits_DifferentiatedSmoothed"]
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["DutyCycle_PhidgetsUnits_FromDevice"]
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Temperature_DegC_FromDevice = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["Temperature_DegC_FromDevice"]
                PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict_Time = PhidgetBrushlessDCmotorDCC1100controller_MostRecentDict["Time"]

        #################################################
        #################################################

        ################################################# SET's
        #################################################
        if PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG == 1:

            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)

            if USE_PhidgetBrushlessDCmotorDCC1100controller_SINUSOIDAL_INPUT_FLAG == 1:

                if USE_PhidgetBrushlessDCmotorDCC1100controller_POSITION_CONTROL_FLAG == 1:
                    SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl + SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl - SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl)*math.sin(time_gain*CurrentTime_MainLoopThread)
                    PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.CommandMotorFromExternalProgram_PositionControl(SINUSOIDAL_INPUT_TO_COMMAND)

                else:
                    SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl + SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl - SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl)*math.sin(time_gain*CurrentTime_MainLoopThread)
                    PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.CommandMotorFromExternalProgram_VelocityControl(SINUSOIDAL_INPUT_TO_COMMAND)

        #################################################
        #################################################

        time.sleep(0.060)

    #################################################
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class.")

    #################################################
    if PhidgetBrushlessDCmotorDCC1100controller_OPEN_FLAG == 1:
        PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################