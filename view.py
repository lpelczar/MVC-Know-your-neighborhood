from texttable import Texttable


class View:

    @staticmethod
    def display_menu():
        print('What would you like to do:\n\n' +
              '\t(1) List statistics\n' +
              '\t(2) Display 3 cities with longest names\n' +
              '\t(3) Display county\'s name with the largest number of communities\n' +
              '\t(4) Display locations, that belong to more than one category\n' +
              '\t(5) Advanced search\n' +
              '\t(0) Exit program\n')

    @staticmethod
    def get_option_input():
        return input('\nChoose option: ')

    @staticmethod
    def display_stats_table(stats: dict):
        t = Texttable()
        t.add_rows([['Ilość', 'MAŁOPOLSKIE']] +
                   [[v, k] for k, v in stats.items()])
        print(t.draw())

    @staticmethod
    def display_county_with_max_communities(county_name):
        print('Name of county with maximum number of communities: {}'.format(county_name))

    @staticmethod
    def display_three_cities_with_longest_names(cities):
        for _ in cities:
            print('Name: {}'.format(_.name))
