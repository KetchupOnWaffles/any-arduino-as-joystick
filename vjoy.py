import ctypes
import struct

CONST_DLL_VJOY = "C:\\Program Files\\vJoy\\x64\\vJoyInterface.dll"

class vJoy(object):
    def __init__(self, reference = 1):
        self.handle = None
        self.dll = ctypes.CDLL( CONST_DLL_VJOY )
        self.reference = reference
        self.acquired = False
        
    def open(self):
        if self.dll.AcquireVJD( self.reference ):
            self.acquired = True
            return True
        return False
    def close(self):
        if self.dll.RelinquishVJD( self.reference ):
            self.acquired = False
            return True
        return False
    def generateJoystickPosition(self, 
        wThrottle = 0, wRudder = 0, wAileron = 0, 
        wAxisX = 0, wAxisY = 0, wAxisZ = 0,
        wAxisXRot = 0, wAxisYRot = 0, wAxisZRot = 0,
        wSlider = 0, wDial = 0, wWheel = 0,
        wAxisVX = 0, wAxisVY = 0, wAxisVZ = 0,
        wAxisVBRX = 0, wAxisVBRY = 0, wAxisVBRZ = 0,
        lButtons = 0, bHats = 0, bHatsEx1 = 0, bHatsEx2 = 0, bHatsEx3 = 0):
        joyPosFormat = "BlllllllllllllllllllIIII"
        pos = struct.pack( joyPosFormat, self.reference, wThrottle, wRudder,
                                   wAileron, wAxisX, wAxisY, wAxisZ, wAxisXRot, wAxisYRot,
                                   wAxisZRot, wSlider, wDial, wWheel, wAxisVX, wAxisVY, wAxisVZ,
                                   wAxisVBRX, wAxisVBRY, wAxisVBRZ, lButtons, bHats, bHatsEx1, bHatsEx2, bHatsEx3 )
        return pos
    def update(self, joystickPosition):
        if self.dll.UpdateVJD( self.reference, joystickPosition ):
            return True
        return False
    #Not working, send buttons one by one
    def sendButtons( self, bState ):
        joyPosition = self.generateJoystickPosition( lButtons = bState )
        return self.update( joyPosition )
    def setButton( self, index, state ):
        if self.dll.SetBtn( state, self.reference, index ):
            return True
        return False
                

vj = vJoy()

# valueX, valueY between -1.0 and 1.0
# scale between 0 and 16000
def setJoy(value1, value2,  scale):
    val1 = int(value1*scale)
    val2 = int(value2*scale)
    #if you want to send more axis, the list of their names is in the function generateJoystickPosition
    joystickPosition = vj.generateJoystickPosition(wAxisX = val1, wAxisY = val2)
    vj.update(joystickPosition)
