from collections import Counter

COUNTY = 'powiat'
CITY = 'miasto'
CITY_COUNTY = 'miasto na prawach powiatu'


class County:

    def __init__(self, name, number, is_city):
        self.county_regions = []
        self.name = name
        self.number = number
        self.is_city = is_city
        self.communities_number = len(self.county_regions)
        self.region_type = COUNTY if not self.is_city else CITY_COUNTY

    def add_county_region(self, county_region):
        """
        Adds given county region to county regions list

        :param county_region: CountyRegion -> county region which we want to add to county
        """
        self.county_regions.append(county_region)

    def get_cities(self):
        """
        Returns list of cities within the county

        :return: list -> list of cities
        """
        cities = []
        cities.extend([city for city in self.county_regions if city.region_type == CITY])
        if self.is_city:
            cities.append(self)
        return cities

    def get_regions_with_more_than_one_type(self):
        """
        Returns list of regions which belong to more than one category

        :return: list -> regions with more than one category
        """
        counter = Counter([county.name for county in self.county_regions])
        return [k for k, v in counter.items() if v > 1]

    def get_locations_startswith(self, query):
        """
        Returns locations from county which starts with given string

        :param query: string -> string by which we are searching
        :return: list -> locations which starts with given string
        """
        return [region for region in self.county_regions if region.name.startswith(query)]

    def get_county_region_quantity(self, region_type):
        """
        Returns quantity of county regions with given region type

        :return: int -> quantity of regions with given type
        """
        regions_quantity = 0
        for region in self.county_regions:
            if region.region_type == region_type:
                regions_quantity += 1
        return regions_quantity
