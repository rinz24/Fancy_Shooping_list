from FancyShoppingListAAS import FancyShoppingList

def create_shopping_list():
    shopping_list = []
    num_items = int(input("How many items will you order today? "))
    
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))

    for i in range(1, num_items + 1):
        print(f"Item #{i}-")
        food = input("Enter food: ")
        amount = float(input("Enter amount of pounds: "))
        
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter amount of pounds: "))

        item = FancyShoppingList(food, amount)
        shopping_list.append(item)

    return shopping_list

def display_shopping_list(shopping_list):
    print("\nHere's a summary of the items purchased:")
    for i, item in enumerate(shopping_list, 1):
        print(f"Item: {item.get_food()}")
        print(f"Amount ordered: {item.get_amount():.1f} pounds")
        print(f"Price per pound: ${item.get_price_per_pound():.2f}")
        print(f"Price of order: ${item.calculate_cost():.2f}")
        print()

def calculate_total_cost(shopping_list):
    total_cost = sum(item.calculate_cost() for item in shopping_list)
    return total_cost

def main():
    items_list = create_shopping_list()
    display_shopping_list(items_list)
    total_cost = calculate_total_cost(items_list)
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
