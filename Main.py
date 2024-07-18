from Read import read_Rentals
from Operation import display_items,rent_items,return_items
from Write import updateRental
def main():
    try:
        rent = read_Rentals("rental_items.txt")
        while True:
            print("\t")
            print("***********************************************************************************************")
            print('''
                ╔════════════════════════════════════════════════════════════════════╗
                ║                                                                    ║
                ║                  WELCOME TO DIVYA SHRESTHA RENTAL                  ║
                ║                                                                    ║
                ║                       SAMAKHUSHI,KATHMANDU                         ║
                ║                                                                    ║
                ║====================================================================║
                ║ PLEASE SELECT A CATEGORY AS ( 1/2/3/4 ), ACCODING TO YOUR CHOICE:  ║
                ║                                                                    ║
                ║                                                                    ║
                ║                        1 = SHOW ITEMS                              ║
                ║                        2 = RENT ITEMS                              ║
                ║                        3 = RETURN ITEMS                            ║    
                ║                        4 = EXIT SHOP                               ║                                                                    
                ║                                                                    ║
                ╚════════════════════════════════════════════════════════════════════╝        
                         ''')
            Choice=int(input("Enter your choice: "))
            if Choice==1:   
                display_items(rent)
            elif Choice==2:
                try:
                    customer_name=input("Enter your full name name: ")
                    if customer_name=="":
                        print("Customer name should not be Empty!!")
                        continue                
                  
                    if not customer_name.strip():
                        raise ValueError
                    
                except ValueError :
                    print("There should not be any spaces and numeric in the input")
                rent_items(rent,customer_name)
                updateRental("rental_items.txt",rent)
                


            elif Choice==3:
                try:
                    customer_name=input("Enter your full  name: ")
                   
                    if not customer_name.strip():
                        raise ValueError
                    
                    
                except ValueError :
                    print("There should not be any spaces and numeric in the input")
                return_items(rent,customer_name)
                updateRental("rental_items.txt",rent)


            elif Choice==4:
                print("Thank You For Visiting Our Shop, Do Return Again.")
                break


            elif Choice>=0 or Choice<4:
                print("Choose number Between 1 and 4")
                
            else:
                raise ValueError
                
             
    except ValueError:
        print("You cannot Enter String Please enter option between 1 or 4")
        main()

if __name__=="__main__":
    main()