import datetime
from OperationFunctions import convert,genarate_bill,genarate_return_bill




def display_items(rent):
    print("\t")
    print("***********************************************************************************************")
    print("| {:<8} | {:<35} | {:<18} | {:<10} | {:<10} |".format("Index","Name","Brand","Price","Stock left"))
    print("***********************************************************************************************")
    index=1
    for key,value in rent.items():
        brand = value["brand"]
        price = "${:.2f}".format(value["price"])
        quantity = value["quantity"]
        name = value["name"]
        print("| {:<8} | {:<35} | {:<18} | {:<10} | {:<10} |".format(index,name,brand,price,quantity))
        index+=1
    print("***********************************************************************************************")

def rent_items(rent,customer_name):
    totalamount=0
    rented_item=[]

    display_items(rent)
    
    while True:
        key= input("Enter the number of the item you want to rent or type exit or \"e\" to exit: ")
        if key.lower()=="e" or key.lower()=="exit":
            break
        if key not in rent:
            print("Item not available to rent out ")
            continue
        
        quantity= int(input("Enter quantity to rent: "))
        if(quantity<=0):
            print("Invalid quantity")
            continue
        elif(quantity>rent[key]["quantity"]):
            print("Invalid Quantity")
            continue

        price= rent[key]["price"]
        totalamount += price*quantity
        rent[key]["quantity"] -= quantity
        

        rented_item.append({
            "Customer name":customer_name,
            "name":rent[key]["name"],
            "brand":rent[key]["brand"],
            "price":rent[key]["price"],
            "quantity":quantity
        })

        add_items= input("Do you want to add more items to rent?(y/n): ")
        if add_items.lower()=="n":
            break
    
    print("Total amount: ${:.2f}".format(totalamount))
    bill=genarate_bill("Rented Item")
    print(genarate_bill.__doc__)

    file= open(bill,"a") 
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t  Rental Store LMT. ")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\tSamakhushi,Kathmandu | Contact number: 9841930222 ")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t \t \tBill")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Rented Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    file.write("\n")
    file.write("Customer Name: {}\n".format(customer_name))
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("{:<30} | {:<15} | {:<15} | {:<10}\n".format("Name", "Brand", "Quantity", "Unit Price"))
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    for item in rented_item:
             file.write("{:<30} | {:<15} | {:<15} | {:<10}\n".format(item["name"], item["brand"], item["quantity"], item["price"]))

    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")

    file.write(" Total: ${}".format(totalamount))

    print("Bill generated at: {}".format(bill))
    ask=input("Do you want to print the bill(y/n): ")
    if (ask=='y' or ask=="yes"):
        print("\n")
        print("\n")
        print("\n")
        print("----------------------------------------------------------------------------------------------------")
        print("\n")
        print("\t\t\t\t\tRental Store LMT. ")
        print("\n")
        print("----------------------------------------------------------------------------------------------------")
        print("\n")
        print("\t\t\t\tSamakhushi,Kathmandu | Contact number: 9841930222 ")
        print("----------------------------------------------------------------------------------------------------")
        print("\n")
        print("\t \t \t Bill")
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("Rented Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print("\n")
        print("Customer Name: {}\n".format(customer_name))
        print("--------------------------------------------------------------------------------------------------------------")
        print("{:<30} | {:<15} | {:<15} | {:<10}\n".format("Name", "Brand", "Quantity", "Unit Price"))
        print("\n")
        print("--------------------------------------------------------------------------------------------------------------")
        print("\n")
        for item in rented_item:
                print("{:<30} | {:<15} | {:<15} | {:<10}\n".format(item["name"], item["brand"], item["quantity"], item["price"]))

        print("\n")
        print("--------------------------------------------------------------------------------------------------------------")
        print("\n")

        print(" Total: ${}".format(totalamount))

def return_items(rent,customer_name):
    totalamount=0
    returned_item=[]
  
#   ask user for the date they rented the order
    datestr=input("Enter the date of rent of the item in Year-Month-day: ")
    date=datetime.datetime.strptime(datestr,'%Y-%m-%d') # gives date of the order rented

    strdays=str(datetime.datetime.now()-date) # Calculates the how many days the order has been taken by the customer
    new= convert(strdays)
    print(new)
    days=int(new)
    


    display_items(rent)

    
    while True:
        key= input("Enter the name of item you want to return or type exit or \"e\" to exit: ")
        if key not in rent:
            print("Item not available to rent out ")
            continue
        if key.lower()=="e" or key.lower()=="exit":
            break



        
        quantity= int(input("Enter quantity to return: "))
        if(quantity<=0):
            print("Invalid quantity")
            continue

        price= rent[key]["price"]
        totalamount += price*quantity


        # updates the quantity  in the dictionary 
        rent[key]["quantity"] += quantity

        # adds the information in rented item list
        returned_item.append({
            "Customer name":customer_name,
            "name":rent[key]["name"],
            "brand":rent[key]["brand"],
            "price":rent[key]["price"],
            "quantity":quantity
        })
        return_items= input("Do you want to return more items?(y/n): ")
        if return_items.lower()=="n":
            break

    
    if(days<=0):
        print("Please Enter correct date and time")
    elif(days<=5):
        bill=genarate_return_bill("Returned Item")
        print(genarate_return_bill.__doc__)

        file= open(bill,"a") 
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t\t\t\tRental Store LMT. ")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t\t\tSamakhushi,Kathmandu | Contact number: 9841930222 ")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t \t \tBill")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Returned Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        file.write("\n")
        file.write("Customer Name: {}\n".format(customer_name))
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("{:<35} | {:<18} | {:<10} | {:<10}\n".format("Name", "Brand", "Quantity", "Unit Price"))
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        for item in returned_item:
             file.write("{:<35} | {:<18} | {:<10} | {:<10}\n".format(item["name"], item["brand"], item["quantity"], item["price"]))

        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write(" Total: ${}".format(totalamount))
        file.close

        print("Bill generated at: {}".format(bill))
        
        ask=input("Do you want to print the bill(y/n): ")
        if ask=='y':
      
            print("\n")
            print("\n")
            print("\n")
            print("----------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t\t\t\t\t\tRental Store LMT. ")
            print("-----------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t\t\t\t\tSamakhushi,Kathmandu | Contact number: 9841930222 ")
            print("-------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t \t \tBill")
            print("--------------------------------------------------------------------------------------------------------------")
            print("Returned Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            print("\n")
            print("Customer Name: {}\n".format(customer_name))
            print("--------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("{:<35} | {:<18} | {:<10} | {:<10}\n".format("Name", "Brand", "Quantity", "Unit Price"))
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------")
            for item in returned_item:
                    print("{:<35} | {:<18} | {:<10} | {:<10}\n".format(item["name"], item["brand"], item["quantity"], item["price"]))

            print("\n")
            print("--------------------------------------------------------------------------------------------------------------")
            print("\n")
            print(" Total: ${}".format(totalamount))

    elif(days>5):
        num=days
        c=0
        while(num>=6):
            c=c+1
            num=num-1
        dtotalamount=0
        dtotalamount =(dtotalamount+ price*quantity)+(c*10)
        print("You have been late to return the item in Time ie (5 days) so 10$ is added for each day until today as a fine")
        bill=genarate_return_bill("Returned Item")
        print(genarate_return_bill.__doc__)

        file= open(bill,"a") 
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t\t\t\t\tRental Store LMT. ")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t\t\tSamakhushi,Kathmandu | Contact number: 9841930222 ")
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t \t \t Bill")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Returned Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        file.write("\n")
        file.write("Customer Name: {}\n".format(customer_name))
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("{:<35} | {:<18} | {:<10} | {:<10}\n".format("Name", "Brand", "Quantity", "Unit Price"))
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        for item in returned_item:
                file.write("{:<35} | {:<18} | {:<10} | {:<10}\n".format(item["name"], item["brand"], item["quantity"], item["price"]))

        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write(" Amount: ${}".format(totalamount))
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write(f"You have been fined $ {(c*10)} for {days-5} days late subbmission")
        file.write("\n")
        file.write(" Total Amount: ${}".format(dtotalamount))
        file.close

        print("Bill generated at: {}".format(bill))
        ask=input("Do you want to print the bill(y/n): ")
        if ask=='y':
            print("\n")
            print("\n")
            print("\n")
            print("----------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t\t\t\t\t\tRental Store LMT. ")
            print("----------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t\t\t\t\tSamakhushi,Kathmandu | Contact number: 9841930222 ")
            print("----------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t \t \t Bill")
            print("--------------------------------------------------------------------------------------------------------------")
            print("Returned Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            print("\n")
            print("Customer Name: {}\n".format(customer_name))
            print("--------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("{:<35} | {:<18} | {:<10} | {:<10}\n".format("Name", "Brand", "Quantity", "Unit Price"))
            print("--------------------------------------------------------------------------------------------------------------")
            print("\n")
            for item in returned_item:
                    print("{:<35} | {:<18} | {:<10} | {:<10}\n".format(item["name"], item["brand"], item["quantity"], item["price"]))

            print("\n")
            print("--------------------------------------------------------------------------------------------------------------")
            print("\n")
            print(" Amount: ${}".format(totalamount))
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------")
            print("\n")
            print(f"You have been fined $ {(c*10)} for {days-5} days late subbmission")
            print("\n")
            print(" Total Amount: ${}".format(dtotalamount))
                