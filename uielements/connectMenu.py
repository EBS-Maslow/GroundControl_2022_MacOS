from kivy.uix.floatlayout                      import  FloatLayout
from kivy.properties                           import  ListProperty
from datastructures.makesmithInitFuncs         import  MakesmithInitFuncs

import sys
import glob
import serial
import threading
import serial.tools.list_ports_osx

class ConnectMenu(FloatLayout, MakesmithInitFuncs):
    
    COMports = ListProperty(("Available Ports:", "None"))
    
    def setPort(self, port):
        print ("update ports")
        print (port)
        self.data.comport = port
        self.data.config.set('Maslow Settings', 'COMport', str(self.data.comport))
    def connect(self, *args):
        
        self.data.config.set('Maslow Settings', 'COMport', str(self.data.comport))
        
        #close the parent popup
        self.parentWidget.close()
        
    
    def updatePorts(self, *args):
        
        portsList = ["Available Ports:"]
        
        if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            sysports = glob.glob('/dev/tty[A-Za-z]*')
            for port in sysports:
                portsList.append(port)

        elif sys.platform.startswith('darwin'):
            sysports = glob.glob('/dev/tty.*')
            for port in sysports:
                portsList.append(port)
        
        else:
            raise EnvironmentError('Unsupported platform - can\'t find serial ports')

        if len(portsList) == 1:
            portsList.append("None")
        
        self.COMports = portsList

    
