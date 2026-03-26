products = ['Rice','Sugar','Wheat Flour','Milk','Eggs', 'Cooking Oil',
            'Tea Powder','Salt','Bread','Soap']
prices= [60,30,40,20,70,80,110,35,45,65]

print("------ Welcome to Grocery Store ------")
print("Here are the available products:\n")
for i in range(10):
    print(f"{str(i+1).ljust(8,' ')} {(products[i]).ljust(16,' ')} {str(prices[i]).ljust(6,' ')}")

items = list(map(int,input("Enter the indexes: ").split()))
print("Selected Items: ")
total_amount = 0
for item in items:
    print(products[item-1],prices[item-1])
    total_amount+= prices[item-1]


print(f"Total Amount to Pay: Rs. {total_amount},Thank you for shopping with us!")