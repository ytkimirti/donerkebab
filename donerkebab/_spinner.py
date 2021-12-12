from halo import Halo

class Spinner(Halo):
    def __init__(self, enabled, text='', autofail=True, spinner='dots'):
        super().__init__(text=text ,enabled=enabled, spinner=spinner)
        self.autofail = autofail
    
    # def fail(self):
    #     if self.enabled:
    #         super().fail()

    # def succeed(self):
    #     if self.enabled:
    #         super().succeed()

    def __exit__(self, type, value, traceback):
        """Stops the spinner. For use in context managers."""

        if self.autofail: 
            if (traceback):
                self.fail()
            else:
                self.succeed()
        return super().__exit__(type, value, traceback)