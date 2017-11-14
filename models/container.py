from voivodeship import Voivodeship
from county_region import CountyRegion
from county import County
import csv


class Container:

    def __init__(self):
        self.voivodeships = []

    def load_data_from_file(self):
        with open('malopolska.csv') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                if row['typ'] == 'województwo':
                    self.voivodeships.append(Voivodeship(row['nazwa'], row['woj']))
                elif row['typ'] == 'powiat':
                    for voivo in self.voivodeships:
                        if voivo.number == row['woj']:
                            voivo.add_county(County(row['nazwa'], row['pow'], False))
                elif row['typ'] == 'miasto na prawach powiatu':
                    for voivo in self.voivodeships:
                        if voivo.number == row['woj']:
                            voivo.add_county(County(row['nazwa'], row['pow'], True))
                else:
                    for voivo in self.voivodeships:
                        for county in voivo.counties:
                            if county.number == row['pow']:
                                county.add_county_region(CountyRegion(row['nazwa'], row['gmi'], row['typ']))
