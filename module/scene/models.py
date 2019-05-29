import time

class MessageScene:
    
    def __init__(self, lcd_manager, elapse_time):
        self.lcd_manager = lcd_manager
        self.elapse_time = elapse_time

    def play(self):
        frames = self._create_frames()
        for frame in frames:
            self.lcd_manager.set_frame(frame=frame)
            self.lcd_manager.display_frame()
            
            time.sleep(self.elapse_time)


    def set_message(self, message):
        self.message = message

    def _create_frames(self):
        return [ 
            self.message[cursor:cursor+self.lcd_manager.lcd_char_size()]
            for cursor in range(
                0,
                len(self.message),
                self.lcd_manager.lcd_char_size(),
            ) 
        ]
