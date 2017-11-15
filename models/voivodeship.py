class Voivodeship:

    def __init__(self, name, number):
        self.counties = []
        self.name = name
        self.number = number
        self.region_type = 'województwo'

    def add_county(self, county):
        self.counties.append(county)
