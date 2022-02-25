def get_total(price_list):
	price_return = {}
	subtotal = 0.0
	for p in price_list:
		subtotal = subtotal + p
	price_return.update({"subtotal":subtotal})
	price_return.update({"tax":round(subtotal*0.07,2)})
	price_return.update({"total":round(subtotal+price_return["tax"],2)})

	return (price_return)

def main():
	
	my_items = []
	for i in range(1,6):
		try:
			my_items.append(float(input("Input price for item "+str(i)+": ")))
		except:
			print("Did you actually put in a valid number of type float?")
			exit()
	
	price_return = get_total(my_items)

	for key, val in price_return.items():
		print(key,": $",round(val,2))

if __name__ == "__main__":
	main()