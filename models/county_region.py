class CountyRegion:

    def __init__(self, name, number, region_type):
        self.name = name
        self.number = number
        self.region_type = region_type

    def __str__(self):
        return 'Name: {} Type: {}'.format(self.name, self.region_type)

    def __repr__(self):
        return 'Name: {} Type: {}'.format(self.name, self.region_type)
