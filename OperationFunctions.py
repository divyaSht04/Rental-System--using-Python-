
import random
def convert(text):
    num=""
    for character in text:
        if character.isdigit():
            num= num+character
        elif character.isalpha():
            break
    return(num)

def genarate_bill(bill_ItemRent):
    '''
      This function prints the bill for the item you have rented from our store
    '''
    random_number=random.randint(0,1000)
    return "{}_{}.txt".format(bill_ItemRent, random_number)


def genarate_return_bill(bill_ItemReturned):
    '''
      This function prints the bill for the item you have rented from our store
    '''
    random_number=random.randint(1000,9999)
    return "{}_{}.txt".format(bill_ItemReturned, random_number)
