
import csv
from address import Address
from work_address import WorkAddress


class AddressBook:

    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise TypeError('Test dupy się nie powiódł ;(')

    def find(self, search_phrase):
        match_objects = []
        for obj in self.addresses:
            obj_data = [value.upper() for value in obj.__dict__.values()]
            for data in obj_data:
                if search_phrase.upper() in data:
                    if obj not in match_objects:
                        match_objects.append(obj)
        return match_objects

    def sort(self):
        sorted_addresses = []
        while self.addresses:
            next_min_element = min(self.addresses, key=lambda address: address.get_full_address())
            sorted_addresses.append(next_min_element)
            self.addresses.remove(next_min_element)
        self.addresses = sorted_addresses

    @staticmethod
    def create_from_csv(last_name, csv_path):
        new_address_book = AddressBook(last_name)

        with open(csv_path) as source:
            addresses_list = csv.DictReader(source)

            for address in addresses_list:
                if address['company'] == '':
                    new_address = Address(address["person"], address["city"], address["street"], address["house_no"])
                    new_address_book.add_address(new_address)
                else:
                    new_address = WorkAddress(address["person"], address["city"], address["street"],
                                              address["house_no"], address["company"])
                    new_address_book.add_address(new_address)

        return new_address_book

    def save_to_csv(self):
        filepath = self.name + '.csv'

        with open(filepath, "w") as addresses_csv:
            fieldnames = ['person', 'city', 'street', 'house_no', 'company']
            addresses_writer = csv.DictWriter(addresses_csv, fieldnames=fieldnames)
            addresses_writer.writeheader()
            addresses_list = self.addresses

            for address in addresses_list:
                if isinstance(address, WorkAddress):
                    addresses_dict = {'person': address.person, 'city': address.city, 'street': address.street,
                                      'house_no': address.house_no, 'company': address.company}
                    addresses_writer.writerow(addresses_dict)
                else:
                    addresses_dict = {'person': address.person, 'city': address.city, 'street': address.street,
                                      'house_no': address.house_no}
                    addresses_writer.writerow(addresses_dict)
