import csv


class Region:

    regions = []

    def __init__(self, voivodeship_num, county_num, community_num, name, region_type):
        self.voivodeship_num = voivodeship_num
        self.county_num = county_num
        self.community_num = community_num
        self.name = name
        self.region_type = region_type
        self.regions.append(self)

    @staticmethod
    def read_from_file():
        with open('malopolska.csv') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                Region(row['woj'], row['pow'], row['gmi'], row['nazwa'], row['typ'])
