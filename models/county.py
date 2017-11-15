from collections import Counter


class County:

    def __init__(self, name, number, is_city):
        self.county_regions = []
        self.name = name
        self.number = number
        self.is_city = is_city
        self.communities_number = len(self.county_regions)

    def add_county_region(self, county_region):
        self.county_regions.append(county_region)

    def get_cities(self):
        cities = []
        cities.extend([city for city in self.county_regions if city.region_type == 'miasto'])
        if self.is_city:
            cities.append(self)
        return cities

    def get_regions_with_more_than_one_type(self):
        counter = Counter([county.name for county in self.county_regions])
        return [k for k, v in counter.items() if v > 1]

    def __str__(self):
        return 'Name: {}'.format(self.name)

    def __repr__(self):
        return 'Name: {}'.format(self.name)
