
def updateRental(filename,rent):
    file=open(filename,"w")
    for key, details in rent.items():
        name = details["name"]
        brand = details["brand"]
        price = "${:.2f}".format(details["price"])
        quantity = details["quantity"]
        line=f"{key}, {name}, {brand}, {price}, {quantity}"
        file.write(line)
        file.write("\n")
        
