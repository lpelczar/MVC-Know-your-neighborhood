class Voivodeship:

    def __init__(self, name, number):
        self.counties = []
        self.name = name
        self.number = number

    def add_county(self, county):
        self.counties.append(county)

    def __str__(self):
        return 'Name: {}'.format(self.name)

    def __repr__(self):
        return 'Name: {}'.format(self.name)
