class Flower(object):

    def __init__(self):
        self.name = ''
        self.number = 0
        self.price = 0.0

    def set_name(self):
        self.name = input('Flower name (string)\n> ')
    def get_name(self):
        print('Flower name:', self.name)

    def set_number(self):
        self.number = 0
        while self.number <= 0:
            number = input('Number of petals (positive integer)\n> ')
            try:
                self.number = int(number)
            except:
                pass   
    def get_number(self):
        print('Number of petals:', self.number)

    def set_price(self):
        self.price = 0.0
        while self.price <= 0:
            price = input('Flower price (positive float)\n> ')
            try:
                self.price = float(price)
            except:
                pass   
    def get_price(self):
        print('Flower price:', self.price)

flower = Flower()