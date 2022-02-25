class ItemToPurchase():

    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description=[]):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity),"@ $" + str(self.item_price), 
            "=  $" + str(self.item_price*self.item_quantity))

class ShoppingCart():
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, i_t_p):
        self.cart_items.append(i_t_p)

    def remove_item(self, item_name):
        for i,c in enumerate(self.cart_items):
            if item_name == c.item_name:
                del self.cart_items[i]
                return
        print("Item not found in cart")

    def modify_item(self, i_t_p):
        for c in self.cart_items:
            if i_t_p.item_name == c.item_name:
                if c.item_name == "none":
                    c.item_name = i_t_p.item_name
                if c.item_price == 0:
                    c.item_price = i_t_p.item_price
                if c.item_quantity == 0:
                    c.item_quantity = i_t_p.item_quantity
                if not c.item_description:
                    c.item_description = i_t_p.item_description
                return
                               
        print("Item not found in cart.")

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost = total_cost + i.item_price*i.item_quantity
        return total_cost

    def print_total(self):
        print(self.customer_name +"'s Shopping Cart -",self.current_date)
        print("Number of Items:", self.get_num_items_in_cart())
        for i in self.cart_items:
            i.print_item_cost()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        print("Total:","$"+str(self.get_cost_of_cart()))

    def print_descriptions(self):
        print(self.customer_name +"'s Shopping Cart -",self.current_date)
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print("Item Descriptions")
        for i in self.cart_items:
            des = ','.join(i.item_description)
            print(i.item_name+":", des)

def print_menu(sc):

    while(True):
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:")
        print()
        if choice == "q":
            return
        elif choice == "i":
            sc.print_descriptions()
        elif choice == "o":
            sc.print_total()
        elif choice == "a":
            print("ADD ITEM TO CART")
            print("Enter the item name:")
            i_n = input()
            print("Enter the item description:")
            i_d = input().split(",")
            print("Enter the item price:")
            try:
                i_p = float(input())
            except:
                print("Needs to be a float")
                exit()
            print("Enter the item quantity:")
            try:
                i_q = int(input())
            except:
                print("Needs to be an int")
                exit()
            itm = ItemToPurchase(i_n,i_p,i_q,i_d)
            sc.add_item(itm)
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            item_name = input()
            sc.remove_item(item_name)
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            print("Enter the item name:")
            item_name = input()
            print("Enter the new quantity:")
            try:
                new_quantity = int(input())
            except:
                print("Needs to be an int")
                exit()
            itm = ItemToPurchase(item_name = item_name, item_quantity = new_quantity)
            sc.modify_item(itm)
        else:
            print(choice,"is not a valid choice!")

def main():
    sc = ShoppingCart(input("Customer Name: "), input("Date: "))
    print("Customer Name:",sc.customer_name)
    print("Today's Date:",sc.current_date)
    print_menu(sc)

        
if __name__ == "__main__":
    main()

