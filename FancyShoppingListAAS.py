class FancyShoppingList:
    def __init__(self, food, amount):
        self.__food = food
        self.__amount = amount
        self.__standard_price = 0.00
        self.__calculated_price = 0.00 
        self.__price_list()

    def __price_list(self):
        if self.__food == 'Dry Cured Iberian Ham':
            self.__standard_price = 177.80
        elif self.__food == 'Wagyu Steaks':
            self.__standard_price = 450.00
        elif self.__food == 'Matsutake Mushrooms':
            self.__standard_price = 272.00
        elif self.__food == 'Kopi Luwak Coffee':
            self.__standard_price = 306.50
        elif self.__food == 'Moose Cheese':
            self.__standard_price = 487.20
        elif self.__food == 'White Truffles':
            self.__standard_price = 3600.00
        elif self.__food == 'Blue Fin Tuna':
            self.__standard_price = 3603.00
        elif self.__food == 'Le Bonnotte Potatoes':
            self.__standard_price = 270.81
        else:
            self.__standard_price = 0.00

    def calculate_cost(self):
        self.__calculated_price = self.__amount * self.__standard_price
        return self.__calculated_price
    
    def get_food(self):
        return self.__food
    
    def get_amount(self):
        return self.__amount
    
    def get_price_per_pound(self):
        return self.__standard_price
    
    def __str__(self):
        return f"Item: {self.__food}\nAmount ordered: {self.__amount:.1f} pounds\nPrice per pound: ${self.__standard_price:.2f}\nPrice of order: ${self.__calculated_price:.2f}"
