
from address import Address


class WorkAddress(Address):

    def __init__(self, person, city, street, house_no, company):
        super().__init__(person, city, street, house_no)
        self.company = company

    def get_full_address(self):
        return '{}, {}, {} {}, {}'.format(self.person, self.city, self.street, str(self.house_no), self.company)
