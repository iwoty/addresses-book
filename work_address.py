
from address import Address


class WorkAddress(Address):

    def __init__(self, person, city, street, house_no, company):
        super().__init__(person, city, street, house_no)
        self.company = company

    def get_full_address(self):
        return '{}, {}, {} {}, {}'.format(self.person, self.city, self.street, str(self.house_no), self.company)

    def __eq__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return ((self.person, self.city, self.street, self.house_no)
                    == (other.person, other.city, other.street, other.house_no))
        else:
            return ((self.person, self.city, self.street, self.house_no, self.company)
                    == (other.person, other.city, other.street, other.house_no, other.company))
