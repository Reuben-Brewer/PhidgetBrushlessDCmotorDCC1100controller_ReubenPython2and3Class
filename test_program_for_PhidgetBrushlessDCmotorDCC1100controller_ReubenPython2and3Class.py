# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision C, 09/03/2021

Verified working on: Python 2.7 and 3 for Windows 8.1 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

from PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *

import os, sys, platform
import time, datetime
import threading
import collections

###############
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###############

###############
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
###############

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject
    global BLDC_OPEN_FLAG
    global SHOW_IN_GUI_BLDC_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if BLDC_OPEN_FLAG == 1 and SHOW_IN_GUI_BLDC_FLAG == 1:
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
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds

    global PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject
    global BLDC_OPEN_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG

    print("Exiting all threads in test_program_for_MyPrint_ReubenPython2and3Class.")

    EXIT_PROGRAM_FLAG = 1

    #########################################################
    if BLDC_OPEN_FLAG == 1:
        PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #########################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global GUI_RootAfterCallbackInterval_Milliseconds

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    TestButton = Button(root, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    #################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################
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

    global USE_BLDC_FLAG
    USE_BLDC_FLAG = 1

    global USE_SINUSOIDAL_POS_CONTROL_INPUT_FLAG
    USE_SINUSOIDAL_POS_CONTROL_INPUT_FLAG = 0

    global USE_SINUSOIDAL_VEL_CONTROL_INPUT_FLAG
    USE_SINUSOIDAL_VEL_CONTROL_INPUT_FLAG = 0

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_BLDC_FLAG
    SHOW_IN_GUI_BLDC_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_BLDC
    global GUI_COLUMN_BLDC
    global GUI_PADX_BLDC
    global GUI_PADY_BLDC
    global GUI_ROWSPAN_BLDC
    global GUI_COLUMNSPAN_BLDC
    GUI_ROW_BLDC = 1

    GUI_COLUMN_BLDC = 0
    GUI_PADX_BLDC = 1
    GUI_PADY_BLDC = 10
    GUI_ROWSPAN_BLDC = 1
    GUI_COLUMNSPAN_BLDC = 1

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

    global root

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject

    global BLDC_OPEN_FLAG
    BLDC_OPEN_FLAG = -1

    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 2.0

    global SINUSOIDAL_MOTION_INPUT_MinValue
    SINUSOIDAL_MOTION_INPUT_MinValue = -50

    global SINUSOIDAL_MOTION_INPUT_MaxValue
    SINUSOIDAL_MOTION_INPUT_MaxValue = 50
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
    #################################################
    #################################################

    #################################################
    #################################################
    NumberOfBLDCmotorPoles = 4
    GearRatio = 1.0
    DistanceMMtoOutputShaftRevRatio = 72.0

    #PositionInRev = PositionInPhidgetsUnits*(1.0/(NumberOfBLDCmotorPoles * 3.0)) * (1.0/GearRatio)
    #PositionInMM = PositionInRev*DistanceMMtoOutputShaftRevRatio

    global BLDC_MostRecentDict

    global BLDC_MostRecentDict_Position_PhidgetsUnits_FromDevice
    BLDC_MostRecentDict_Position_PhidgetsUnits_FromDevice = -11111

    global BLDC_MostRecentDict_Velocity_PhidgetsUnits_FromDevice
    BLDC_MostRecentDict_Velocity_PhidgetsUnits_FromDevice = -11111

    global BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw
    BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw = -11111

    global BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed
    BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed = -11111

    global BLDC_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice
    BLDC_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice = -11111

    global BLDC_MostRecentDict_Temperature_DegC_FromDevice
    BLDC_MostRecentDict_Temperature_DegC_FromDevice = -11111

    global BLDC_MostRecentDict_Time
    BLDC_MostRecentDict_Time = -11111

    PositionInMM_last = -11111
    BLDC_MostRecentDict_Time_Last = -11111

    BLDC_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_BLDC_FLAG),
                                    ("root", root),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_BLDC),
                                    ("GUI_COLUMN", GUI_COLUMN_BLDC),
                                    ("GUI_PADX", GUI_PADX_BLDC),
                                    ("GUI_PADY", GUI_PADY_BLDC),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_BLDC),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_BLDC)])

    global BLDC_setup_dict
    BLDC_setup_dict = dict([("GUIparametersDict", BLDC_GUIparametersDict),
                            ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                            ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                            ("user_set_name", "Reuben's Test BLDC Controller"),
                            ("VINT_SerialNumber", 627656), #528938
                            ("VINT_PortNumber", 0),
                            ("DeviceChannel", 0),
                            ("DeviceID", 108),
                            ("NameToDisplay_UserSet", "Reuben's Test BLDC Controller"),
                            ("ENABLE_GETS_MAINTHREAD", 1),
                            ("FailsafeTime_Milliseconds", 10000),
                            ("MainThread_TimeToSleepEachLoop", 0.001),
                            ("ControlMode", "position"),  #position or velocity
                            ("VelocityMinLimit_PhidgetsUnits_UserSet", 0.0),
                            ("VelocityMaxLimit_PhidgetsUnits_UserSet", 10000.0), #700.0/(DistanceMMtoOutputShaftRevRatio*(1.0/(NumberOfBLDCmotorPoles * 3.0)) * (1.0/GearRatio))
                            ("VelocityStallLimit_PhidgetsUnits_UserSet", 15.0),  #Setting StallVelocity to 0 will turn off stall protection functionality
                            ("BrakingStrengthLimit_VelControl_Percent_UserSet", 100.0),
                            ("AccelerationMaxLimit_PhidgetsUnits_UserSet", 100000.0),
                            ("PositionMinLimit_PhidgetsUnits_UserSet", -950.0/(DistanceMMtoOutputShaftRevRatio*(1.0/(NumberOfBLDCmotorPoles * 3.0)) * (1.0/GearRatio))),
                            ("PositionMaxLimit_PhidgetsUnits_UserSet", 1000.0),
                            ("Kp_PosControl_Gain_UserSet", 20000.0),  #MUST BE NEGATIVE (-20000.0) FOR TOILET-SCOOTER-HUB-MOTOR, POSITIVE FOR PHIDGETS-BRAND MOTOR
                            ("Ki_PosControl_Gain_UserSet", 2.0),  #MUST BE NEGATIVE (-2.0) FOR TOILET-SCOOTER-HUB-MOTOR, POSITIVE FOR PHIDGETS-BRAND MOTOR
                            ("Kd_PosControl_Gain_UserSet", 40000.0),  #MUST BE NEGATIVE (-40000.0) FOR TOILET-SCOOTER-HUB-MOTOR, POSITIVE FOR PHIDGETS-BRAND MOTOR
                            ("DeadBand_PosControl_PhidgetsUnits_UserSet", 10.0),  #Lower DeadBand value is a tighter Position loop (allows less error)
                            ("RescaleFactor_MultipliesPhidgetsUnits_UserSet", 1.0)])  #1.0/(4.25) #1.0/138.0 for ToiletScooter to command revolutions instead of commutations
    '''
    ("UpdateDeltaT_ms", 100), #100 min for velocity, 20 min for position
    ("StartingActualAngle_Deg", 0.0),
    '''

    if USE_BLDC_FLAG == 1:
        try:
            PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class(BLDC_setup_dict)
            time.sleep(0.25)
            BLDC_OPEN_FLAG = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", root),
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
            time.sleep(0.25)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_BLDC_FLAG == 1 and BLDC_OPEN_FLAG != 1:
        print("Failed to open PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    ################################################# SHOWS HOW TO OFFSET THE ANGLE
    #################################################
    #if BLDC_setup_dict["ControlMode"] == "position":
    #    time.sleep(0.5)
    #    PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.SetPositionOffsetOnBoardWithoutMoving(90)
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################

        if USE_BLDC_FLAG == 1:
            ######################### GETs
            BLDC_MostRecentDict = PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            BLDC_MostRecentDict_Position_PhidgetsUnits_FromDevice = BLDC_MostRecentDict["Position_PhidgetsUnits_FromDevice"]
            BLDC_MostRecentDict_Velocity_PhidgetsUnits_FromDevice = BLDC_MostRecentDict["Velocity_PhidgetsUnits_FromDevice"]
            BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw = BLDC_MostRecentDict["Velocity_PhidgetsUnits_DifferentiatedRaw"]
            BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed = BLDC_MostRecentDict["Velocity_PhidgetsUnits_DifferentiatedSmoothed"]
            BLDC_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice = BLDC_MostRecentDict["DutyCycle_PhidgetsUnits_FromDevice"]
            BLDC_MostRecentDict_Temperature_DegC_FromDevice = BLDC_MostRecentDict["Temperature_DegC_FromDevice"]
            BLDC_MostRecentDict_Time = BLDC_MostRecentDict["Time"]

            #print("BLDC_MostRecentDict_Position_PhidgetsUnits_FromDevice: " + str(BLDC_MostRecentDict_Position_PhidgetsUnits_FromDevice))
            #print("BLDC_MostRecentDict_Velocity_PhidgetsUnits_FromDevice: " + str(BLDC_MostRecentDict_Velocity_PhidgetsUnits_FromDevice))
            #print("BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw: " + str(BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedRaw))
            #print("BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed: " + str(BLDC_MostRecentDict_Velocity_PhidgetsUnits_DifferentiatedSmoothed))
            #print("BLDC_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice: " + str(BLDC_MostRecentDict_DutyCycle_PhidgetsUnits_FromDevice))
            #print("BLDC_MostRecentDict_Temperature_DegC_FromDevice: " + str(BLDC_MostRecentDict_Temperature_DegC_FromDevice))
            #print("BLDC_MostRecentDict_Time: " + str(BLDC_MostRecentDict_Time))

            #########################

            ######################### SETs
            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
            SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)*math.sin(time_gain*CurrentTime_MainLoopThread)

            if USE_SINUSOIDAL_POS_CONTROL_INPUT_FLAG == 1 and USE_SINUSOIDAL_VEL_CONTROL_INPUT_FLAG == 0:
                PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.CommandMotorFromExternalProgram("position", SINUSOIDAL_INPUT_TO_COMMAND)

            elif USE_SINUSOIDAL_POS_CONTROL_INPUT_FLAG == 0 and USE_SINUSOIDAL_VEL_CONTROL_INPUT_FLAG == 1:
                PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3ClassObject.CommandMotorFromExternalProgram("velocity", SINUSOIDAL_INPUT_TO_COMMAND)

            elif USE_SINUSOIDAL_POS_CONTROL_INPUT_FLAG == 1 and USE_SINUSOIDAL_VEL_CONTROL_INPUT_FLAG == 1:
                print("CANNOT HAVE BOTH POS AND VEL CONTROL INPUTS")
            #########################

            time.sleep(0.010)

        else:
            time.sleep(0.030)

    #################################################
    #################################################

    print("Exiting main program 'test_program_for_PhidgetBrushlessDCmotorDCC1100controller_ReubenPython2and3Class.")
##########################################################################################################
##########################################################################################################