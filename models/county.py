class County:

    def __init__(self, name, number, is_city):
        self.county_regions = []
        self.name = name
        self.number = number
        self.is_city = is_city

    def add_county_region(self, county_region):
        self.county_regions.append(county_region)

    def __str__(self):
        return 'Name: {}'.format(self.name)

    def __repr__(self):
        return 'Name: {}'.format(self.name)
