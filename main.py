class Computer:
    def __init__(self):
        self.__maxprice = 150000

    def sell(self):
        print("Selling price:{}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
c.__maxprice=50000

c.setMaxPrice(50000)
c.sell()