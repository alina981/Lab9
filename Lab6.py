class Lamp:

    def __init__(self):
        self.power = 50
        self.consumption = 30
        self.service_life = 5000

    def metod1(self):
        return self.service_life//8 + (self.service_life%8 != 0)

    def metod2(self):
        return self.power/self.consumption


class Lamp_day(Lamp):
    def __init__(self):
        super().__init__()
        self.color_of_light = 'white'

    def right_change(self):
        if self.color_of_light == 'white':
            print("Данное освещение активизирует нервные центры, это увеличивает работоспособность")
        elif self.color_of_light == 'yellow':
            print("Данное освещение действует на человека расслабляюще, это снижает работоспособность")
        else:
            print("Данное освещение небезопасно для глаз")
        return



class Searchlight(Lamp):
    def __init__(self):
        super().__init__()
        self.motion_sensor = True

    def presence_of_motion_sensor(self):
        return self.motion_sensor


