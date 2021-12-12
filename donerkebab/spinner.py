from halo import Halo

class Spinner(Halo):
    def __init__(self, text='', autofail=True):
        super().__init__(text=text ,enabled=True)
        self.autofail = autofail

    def __exit__(self, type, value, traceback):
        """Stops the spinner. For use in context managers."""

        if self.autofail: 
            if (traceback):
                self.fail()
            else:
                self.succeed()
        return super().__exit__(type, value, traceback)