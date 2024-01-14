class Drink:

    def __init__(self, title, production_date):
        self.title = title
        self.production_date = production_date

#GETs
    def get_title(self):
        return self.title

    def get_production_date(self):
        return self.production_date

#SETs
    def set_title(self, title):
        self.title = title

    def set_production_date(self, production_date):
        self.production_date = production_date

#Type
    def get_type(self):
        print(type(self))

#toString
    def __str__(self):
        return f'{self.title},{self.production_date()},'