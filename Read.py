def read_Rentals(file_name):
    rent = {}
    File = open(file_name, "r")
    for line in File:
        items = line.split(", ")
        number, name, brand, price, quantity = items 
        rent[number] = {
            "name": name,
            "brand": brand,
            "price": float(price.strip("$")),
            "quantity": int(quantity)
        }
    return rent