from kivy.properties                           import  ListProperty
from kivy.clock                                import  Clock
from datastructures.makesmithInitFuncs         import  MakesmithInitFuncs
from connection.serialPortThread               import  SerialPortThread
import sys
import serial
import serial.tools.list_ports_osx
import threading

class SerialPort(MakesmithInitFuncs):
    '''
    
    The SerialPort is an object which manages communication with the device over the serial port.
    
    The actual connection is run in a separate thread by an instance of a SerialPortThread object.
    
    '''
    
    
    
    
    def __init__(self):
        '''
        
        Runs on creation, schedules the software to attempt to connect to the machine
        
        '''
        Clock.schedule_interval(self.openConnection, 5)
    
    def setPort(self, port):
        '''
        
        Defines which port the machine is attached to
        
        '''
        print ("update ports")
        print (port)
        self.data.comport = port
    
    def connect(self, *args):
        '''
        
        Forces the software to begin trying to connect on the new port.
        
        This function may not be necessary, but it should stay in because it simplifies the user experience.
        
        '''
        self.data.config.set('Maslow Settings', 'COMport', str(self.data.comport))
        
    '''
    
    Serial Connection Functions
    
    '''
    
    def openConnection(self, *args):
        #This function opens the thread which handles the input from the serial port
        #It only needs to be run once, it is run by connecting to the machine
        
        try:
            if not self.data.connectionStatus:
                #self.data.message_queue is the queue which handles passing CAN messages between threads
                x = SerialPortThread()
                x.setUpData(self.data)
                self.th=threading.Thread(target=x.getmessage)
                self.th.daemon = True
                self.th.start()
        except:
            pass
    