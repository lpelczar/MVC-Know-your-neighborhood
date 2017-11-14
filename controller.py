from models.container import Container
from view import View
import os


class Controller:

    def __init__(self):
        self.container = Container()

    def start(self):
        os.system('clear')
        View.display_menu()
        while True:
            option = View.get_option_input()
            os.system('clear')
            View.display_menu()
            if option == '1':
                self.list_statistics()

    def list_statistics(self):
        
