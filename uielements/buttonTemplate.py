from kivy.properties          import StringProperty
from kivy.properties          import ObjectProperty
from kivy.uix.behaviors       import ButtonBehavior
from kivy.uix.floatlayout     import FloatLayout

class ButtonTemplate(FloatLayout, ButtonBehavior):
    
    btnBackground        = StringProperty('atlas://data/images/defaulttheme/button')
    btnBackgroundDown    = StringProperty('atlas://data/images/defaulttheme/button_pressed')
    funcToCallOnPress    = ObjectProperty(None)
    funcToCallOnRelease  = ObjectProperty(None)
    text                 = StringProperty("")
    textColor            = StringProperty('[color=111111]')
    
    
    def internal_on_press(self, *args):
        '''
        
        Runs when the button is pressed
        
        '''
        
        if self.funcToCallOnPress != None:
            self.funcToCallOnPress()
        
        
    def internal_on_release(self, *args):
        '''
        
        Runs when the button is released
        
        '''
        
        if self.funcToCallOnRelease != None:
            self.funcToCallOnRelease()