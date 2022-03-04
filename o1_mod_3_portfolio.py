class ItemToPurchase():

    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity),"@ $", f"{self.item_price:.2f}", 
            "=  $" + f"{(self.item_price*self.item_quantity):.2f}")

def main():

    items = []
    for i in range(1,3):
        print("Item " +str(i))
        print("Enter the item name:")
        i_n = input()
        try:
            print("Enter the item price:")
            i_p = float(input())
            print("Enter the item quantity:")
            i_q = int(input())
            items.append(ItemToPurchase(i_n, i_p, i_q))
        except:
            print("Item price must be a float, and item quantity must be an int!")
            exit()

    print("TOTAL COST")
    total = 0
    for i in items:
        i.print_item_cost()
        total = total + i.item_price*i.item_quantity

    print("Total: $" + f"{total:.2f}")

        
if __name__ == "__main__":
    main()

