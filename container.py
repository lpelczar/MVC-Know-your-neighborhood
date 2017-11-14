from region import Region
import csv


class RegionContainer:

    def __init__(self):
        self.regions = []

    def read_from_file(self):
        with open('malopolska.csv') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                self.regions.append(Region(row['woj'], row['pow'], row['gmi'], row['nazwa'], row['typ']))
