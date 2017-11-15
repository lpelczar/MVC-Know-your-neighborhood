
VOIVODESHIP = 'województwo'


class Voivodeship:

    def __init__(self, name, number):
        self.counties = []
        self.name = name
        self.number = number
        self.region_type = VOIVODESHIP

    def add_county(self, county):
        """
        Adds given county to Voivodeship

        :param county: County -> county which we want to add to Voivodeship
        """
        self.counties.append(county)
