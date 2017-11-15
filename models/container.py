from models.voivodeship import Voivodeship
from models.county_region import CountyRegion
from models.county import County
from operator import attrgetter
import csv


class Container:

    VOIVODESHIP = 'województwo'
    COUNTY = 'powiat'
    URBAN_COMMUNE = 'gmina miejska'
    RURAL_COMMUNE = 'gmina wiejska'
    URBAN_RURAL_COMMUNE = 'gmina miejsko-wiejska'
    RURAL_AREA = 'obszar wiejski'
    CITY = 'miasto'
    CITY_COUNTY = 'miasto na prawach powiatu'
    DELEGACY = 'delegatura'

    def __init__(self):
        self.voivodeships = []

    def get_voivodeship_quantity(self):
        """
        Returns the voivodeships quantity in container

        :return: int -> quantity of voivodeships
        """
        return len(self.voivodeships)

    def get_county_quantity(self):
        """
        Returns the counties quantity in all voivodeships in container

        :return: int -> quantity of counties
        """
        counties = 0
        for voivo in self.voivodeships:
            counties += len(voivo.counties)
        return counties

    def get_city_county_quantity(self):
        """
        Returns the cities with counties rights quantity in all voivodeships in container

        :return: int -> quantity of cities with counties rights
        """
        city_counties = 0
        for voivo in self.voivodeships:
            for county in voivo.counties:
                if county.is_city:
                    city_counties += 1
        return city_counties

    def get_county_region_quantity(self, region_type):
        """
        Returns the county regions quantity in all voivodeships in container with given region type

        :param region_type: string -> type of the region (e.g. 'powiat')
        :return: int -> quantity of regions with given type
        """
        county_regions = 0
        for voivo in self.voivodeships:
            for county in voivo.counties:
                county_regions += county.get_county_region_quantity(region_type)
        return county_regions

    def get_county_with_max_communities(self):
        """
        Returns county with largest number of communities_number

        :return: County -> county with maximum number of communities
        """
        county = None
        for voivo in self.voivodeships:
            county = max(voivo.counties, key=attrgetter('communities_number'))
        return county

    def get_cities(self):
        """
        Returns list of all cities in every voivodeship

        :return: list -> list of cities in every voivodeship
        """
        cities = []
        for voivo in self.voivodeships:
            for county in voivo.counties:
                cities.extend(county.get_cities())
        return cities

    def sort_locations_by_name_length(self, locations):
        """
        Sort descending given locations by name length

        :param locations: list -> list of locations
        :return: list -> descending sorted locations by name length
        """
        return sorted(locations, key=lambda x: len(x.name), reverse=True)

    def get_locations_with_more_than_one_category(self):
        """
        Returns locations which have more than one category

        :return: list -> locations with more than one category
        """
        locations = []
        for voivo in self.voivodeships:
            for county in voivo.counties:
                locations.extend(county.get_regions_with_more_than_one_type())
        return locations

    def get_locations_startswith(self, query):
        """
        Returns list of locations which starts with given string

        :param query: string -> string for which we are searching
        :return: list -> locations with starts with given string
        """
        locations = []
        for voivo in self.voivodeships:
            if voivo.name.startswith(query):
                locations.append(voivo)
            for county in voivo.counties:
                if county.name.startswith(query):
                    locations.append(county)
                locations.extend(county.get_locations_startswith(query))
        return locations

    def sort_locations_by_name_and_type(self, locations):
        """
        Sort locations ascending by two keys: location name and location type

        :param locations: list -> list of locations
        :return: list -> sorted locations by name and location type
        """
        return sorted(locations, key=lambda x: (x.name, x.region_type), reverse=False)

    def load_data_from_file(self):
        """
        Loads data from file and adds them to container
        """
        FILE_NAME = 'malopolska.csv'
        NAME = 'nazwa'
        VOIVO = 'woj'
        COUNTY = 'pow'
        COUNTY_REGION = 'gmi'
        KIND = 'typ'

        with open(FILE_NAME) as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                if row[KIND] == self.VOIVODESHIP:
                    self.add_voivodeship(row[NAME], row[VOIVO])
                elif row[KIND] == self.COUNTY:
                    self.add_county(row[VOIVO], row[NAME], row[COUNTY], False)
                elif row[KIND] == self.CITY_COUNTY:
                    self.add_county(row[VOIVO], row[NAME], row[COUNTY], True)
                else:
                    self.add_county_region(row[COUNTY], row[NAME], row[COUNTY_REGION], row[KIND])

    def add_voivodeship(self, name, number):
        """
        Adds Voivodeship object to container with given name and number

        :param name: string -> name of the voivodeship
        :param number: string -> number of the voivodeship
        """
        self.voivodeships.append(Voivodeship(name, number))

    def add_county(self, voivo_num, name, number, is_city):
        """
        Adds county to given voivodeship by voivo_num with given name, number, and is_city parameters

        :param voivo_num: int -> number of the voivodeship for which we want to add county
        :param name: string -> name of the county
        :param number: int -> number of the county
        :param is_city: bool -> True if county is the city with county rights else False
        """
        for voivo in self.voivodeships:
            if voivo.number == voivo_num:
                voivo.add_county(County(name, number, is_city))

    def add_county_region(self, county_num, name, number, region_type):
        """
        Adds county region to given county by county_num with given name, number and kind

        :param county_num: int -> number of the county to which we want to add region
        :param name: string -> name of the region
        :param number: int -> number of the region
        :param region_type: string -> type of the region (e.g. 'miasto')
        """
        for voivo in self.voivodeships:
            for county in voivo.counties:
                if county.number == county_num:
                    county.add_county_region(CountyRegion(name, number, region_type))
