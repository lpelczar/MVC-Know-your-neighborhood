from models.container import Container
from view import View
import os
import sys


class Controller:

    COUNTY_REGIONS = ['gmina miejska', 'gmina wiejska', 'gmina miejsko-wiejska',
                      'obszar wiejski', 'miasto', 'delegatura']

    def __init__(self):
        self.cont = Container()

    def start(self):
        self.cont.load_data_from_file()
        os.system('clear')
        View.display_menu()
        while True:
            option = View.get_option_input()
            os.system('clear')
            View.display_menu()
            if option == '1':
                self.list_statistics()
            elif option == '2':
                self.display_three_cities_with_longest_names()
            elif option == '3':
                self.display_county_with_max_communities()
            elif option == '4':
                self.display_locations_with_more_than_one_category()
            elif option == '5':
                self.advanced_search()
            elif option == '0':
                sys.exit()

    def list_statistics(self):
        stats = {}
        stats[Container.VOIVODESHIP] = self.cont.get_voivodeship_quantity()
        stats[Container.COUNTY] = self.cont.get_county_quantity()
        stats[Container.CITY_COUNTY] = self.cont.get_city_county_quantity()
        for county_region in self.COUNTY_REGIONS:
            stats[county_region] = self.cont.get_county_region_quantity(county_region)
        View.display_stats_table(stats)

    def display_three_cities_with_longest_names(self):
        cities = self.cont.get_cities_by_name_length()
        sorted_cities = self.cont.sort_locations_by_name_length(cities)
        View.display_locations(sorted_cities[:3])

    def display_county_with_max_communities(self):
        county = self.cont.get_county_name_with_max_communities()
        View.display_county_with_max_communities(county.name)

    def display_locations_with_more_than_one_category(self):
        locations = self.cont.get_locations_with_more_than_one_category()
        View.display_locations_with_more_than_one_category(locations)

    def advanced_search(self):
        query = View.get_query()
        locations = self.cont.get_locations_startswith(query)
        sorted_locations = self.cont.sort_locations_by_name_and_type(locations)
        View.display_searched_locations(sorted_locations)
