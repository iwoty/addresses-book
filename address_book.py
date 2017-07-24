
class AddressBook:

    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        if address.__class__.__name__ == 'Address':
            self.addresses.append(address)
        elif address.__class__.__name__ == 'WorkAddress':
            self.addresses.append(address)
        else:
            raise TypeError('Test dupy się nie powiódł ;(')
