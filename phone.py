"""Module docstring"""


class Phone:
    """Class docstring"""
    line_type = 'проводной'

    def __init__(self, dial_type):
        self.dial_type = dial_type

    def ring(self):
        """Method docstring"""
        print('Дзззыыыыыынь!')

    def call(self, phone_number):
        """Method docstring"""
        print(f'звоню по номеру {phone_number}! Тип связи - {self.line_type}')


class MobilePhone(Phone):
    """Class docstring"""
    line_type = 'беспроводной'
    battary_type = 'Li-ion'

    def __init__(self, dial_type, network_type):
        self.network_type = network_type
        super().__init__(dial_type)

    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        """Method docstring"""
        print('Игра запущена!')


mobile_phone = MobilePhone('сенсорный', 'LTE')

print(mobile_phone.battary_type)
print(mobile_phone.network_type)
mobile_phone.start_game()
