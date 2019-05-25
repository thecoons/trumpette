class DiodeManager:

    def __init__(self, interface, pin):
        self.interface = interface
        self.pin = pin

    def turn_on(self):
        self.interface.output(
            self.pin,
            self.interface.HIGH
        )

    def turn_off(self):
        self.interface.output(
            self.pin,
            self.interface.LOW,
        )
