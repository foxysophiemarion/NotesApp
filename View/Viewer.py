from struct import unpack


class Viewer:

    def print_in_console(self, message: str):
        self.mes = message
        print(self.mes)

    def print_list_in_console(self, notes: list, message: str = ""):
        """
        Print the list to the console
        :param notes: list
        """
        if message == "":
            print("Notes list:")
        else:
            print(message)
        try:
            for note in notes:
                print("\t", note[0], note[1], note[2])
        except TypeError as e:
            print("empty")

    def print_note(self, note: list, message: str = ''):
        print(message)
        print("Note {} dated {} \n \t{}\n{}".format(*note))

    def get_data(self, message: str):
        """
        This function receives data from the console
        :param message: a string in which we describe what the user needs to enter
        """
        self.mes = message
        return input(self.mes)
