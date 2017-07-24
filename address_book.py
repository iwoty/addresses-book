
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

    def find(self, search_phrase):
        match_objects = []

        for obj in self.addresses:
            if search_phrase.upper() in [value.upper() for value in obj.__dict__.values()]:
                match_objects.append(obj)

        return match_objects

    def sort(self):
        """
        Bubble sort.
        """
        for address in self.addresses:
            for i in range(1, len(self.addresses)):     # i-1 so begin from 2nd element
                if self.addresses[i-1].get_full_address[0] > self.addresses[i].get_full_address[0]:
                    self.addresses.insert(i, self.addresses.pop(i-1))
