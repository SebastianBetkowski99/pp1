class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no=1
    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print('Telewizor jest włączony . Numer kanału {}'.format(self.channel_no))  

        else:
            print('Telewizor jest wyłączony.')
telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()