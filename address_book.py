
import csv
from address import Address
from work_address import WorkAddress


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

    @staticmethod
    def create_from_csv(last_name, csv_path):
        csv_path = last_name + '.csv'
        new_address_book = AddressBook(last_name)

        with open(csv_path) as source:
            addresses_list = csv.DictReader(source)
            for address in addresses_list:
                if ADDRESS SPLIT krotszy niz 5 (jest company):
                    new_address = Address(address["person"], address["city"], address["street"], address["house_no"])
                    new_address_book.add_address(new_address)
                else:
                    new_address = WorkAddress(address["person"], address["city"], address["street"],
                                              address["house_no"], company["company"])
                    new_address_book.add_address(new_address)

        return new_address_book

    def save_to_csv(self):
        filepath = self.__class__.__name__ + '.csv'
        with open(filepath, "w") as addresses_csv:
            fieldnames = ['person', 'city', 'street', 'house_no', 'company']
            addresses_writer = csv.DictWriter(addresses_csv, fieldnames=fieldnames)
            addresses_writer.writeheader()
            addresses_list = User.get_user_list()
            for user in user_list:
                user_dict = {'name': user.get_name(), 'mail': user.get_mail(), 'password': user.get_password(), 'role': user.get_class_name().lower()}
                user_writer.writerow(user_dict)
