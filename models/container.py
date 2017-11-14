from models.voivodeship import Voivodeship
from models.county_region import CountyRegion
from models.county import County
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
        return len(self.voivodeships)

    def get_county_quantity(self):
        counties = 0
        for voivo in self.voivodeships:
            counties += len(voivo.counties)
        return counties

    def get_urban_commune_quantity(self):
        pass

    def load_data_from_file(self):
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
        self.voivodeships.append(Voivodeship(name, number))

    def add_county(self, voivo_num, name, number, is_city):
        for voivo in self.voivodeships:
            if voivo.number == voivo_num:
                voivo.add_county(County(name, number, is_city))

    def add_county_region(self, county_num, name, number, kind):
        for voivo in self.voivodeships:
            for county in voivo.counties:
                if county.number == county_num:
                    county.add_county_region(CountyRegion(name, number, kind))
