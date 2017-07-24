
class UserInput:
    """
    Creates UserInput object.
    """
    def __init__(self):
        pass

    def get_option(self, options):
        user_input_number = input("\nPick an option (number): ")
        while not user_input_number.isnumeric():
            user_input_number = input("\nPick an PROPER option (number): ")

    def get_anykey(self):
        """
        Returns input that waits for anykey.
        """
        return input('Press -->ENTER<-- to move forward.')
