
d_price={"brush":120,"Soap":20,"Rice":120}
d_quantity={"brush":1,"Soap":2,"Rice":10}
total=0
for key in d_price.keys():
    total=total+d_price[key]*d_quantity[key]
print(total)