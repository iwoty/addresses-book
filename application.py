
from user_input import UserInput
from view import View
from address import Address
from work_adress import WorkAddress
from address_book import AddressBook


class Application:

    menu_options = ['Welcome to your Awesome OOP Address Book Manager!',
                    'What would you like to do?',
                    '  1. Create new address book',
                    '  2. Open address book from file',
                    '  0. Exit']

    def __init__(self):
        """
        Creates application object.
        """
        self.is_running = True
        self.user_input = UserInput()
        self.view = View()
        self.csv_file_path = ""
