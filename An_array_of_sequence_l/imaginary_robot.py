class Robot(object):
    def __init__(self, name):
        self.name = name
        self.leds = {ident: LED() for ident in range(4)}
        
    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
                
    def beep(self, frequency, times):
        return f'{"BEEP " * times}with frequency {frequency}'
    
    def rotate_neck(self, angle):
        return f'Neck rotated at {angle} degrees'

class LED:
    def set_brightness(self, intensity):
        return f'LED brightness set to {intensity}'
    
    