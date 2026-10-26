class Order:

    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer: " + str(self.getCustomer()))
        print("     Quantity: " + str(self.getQtty()))
        print("     ------------")

    def getQtty(self):
        return self.qtty

    def getCustomer(self):
        return self.customer
