amazon_cart = ["notebooks", 
                   "sunglasses", 
                   "earphones",
                   "toys",
                   "grapes"]
  
for x in amazon_cart:
  # print(x)
  name_length=len(x)
  # print(name_length)
  print(x[0:name_length:2])
