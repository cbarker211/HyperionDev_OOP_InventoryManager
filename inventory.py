#Import tabulate for the view_all function.
from tabulate import tabulate
#Import pycountry for the list of countries.
import pycountry


#========The beginning of the class==========
class Shoe:
    #Construct the class, assigning all of the instance variables.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #Method to output the cost of the shoe.
    def get_cost(self):
        print(f"The shoes cost R{self.cost}.")

    #Method to output the quantity of shoes.
    def get_quantity(self):
        print(f"There are {self.quantity} shoes in stock.")

    #Method to return a string representation of a class.
    def __str__(self):
        string = (f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}")
        return string


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

#Function to read the shoe data from the inventory.txt file.
def read_shoes_data():
    filename = "inventory.txt"
    #First use try except to handle if the file is missing.
    try:
        with open(filename, 'r') as f:
            pass
    except FileNotFoundError as error:
        print("Inventory file is missing! Please add the file and try again.")

    #If there are no errors, then continue.
    else:
        #Now handle if there is no data in the file.
        with open(filename, 'r') as f:
            #This line makes sure count is initialised before the for loop.
            #This makes sure that the program has a value of count to check in the if statement.
            count = -1  
            for count, line in enumerate(f):
                pass
        if count == 0:
            print("File has no data.")

        #If there is data in the file, then add the shoes as Shoe objects to the shoe list.
        elif count >= 1:
            with open(filename, 'r') as f:
                for count, line in enumerate(f):
                    #Don't add the headerline.
                    if count != 0:
                        #Split the line into the relevant sections and strip line breaks.
                        line = line.strip()
                        line = line.split(',')
                        #Append a new Shoe object to the list.
                        shoe_list.append(Shoe(line[0],line[1],line[2],line[3],line[4]))

        #If there is nothing at all in the file, print an error message.       
        else:
            print("Invalid file, please fix the file and try again.")

#Function to add data on new shoe
def capture_shoes():
    #Use pycountry to get a list of all valid countries.
    country_list = []
    for country in pycountry.countries:
        country_list.append(country.name.lower())

    #Now ask the user for the product country.
    while True:
        input_country = input("Please enter the country of origin of the shoe: ")
        if input_country.lower() not in country_list:
            print("Country not found, please retry.")
            continue 
        #If the country is valid, then break the for loop.   
        break
    #Make sure that the final country name is capitalized.
    country = ""
    for word in input_country.split(" "):
        country += word.capitalize() + " "
    country = country.strip()
    
    #Now ask the user for the product code.
    #You could probably add functionality to check if the code already exists.
    #However there may be shoes from multiple countries with the same code.
    #Same for the product name.
    while True:
        #Try-except to make sure that an integer is entered.
        try:
            code = int(input("Please enter the code of the shoe, without the SKU prefix: "))
        except:
            print("Code must be numeric, please reenter.")
            continue
        #Extra check to make sure the code is 5 letters long.
        if len(str(code)) != 5:
            print("The product code should have a length of 5, please reenter.")
            continue
        #If the code is valid, then break the while loop.   
        break
    #Now add on the SKU prefix
    code = "SKU" + str(code)

    #Now ask the user for the product name.
    input_product = input("Please enter the product name of the shoe: ")
    #Make sure that each word in the product is capitalized.
    product = ""
    for word in input_product.split(" "):
        product += word.capitalize() + " "
    product = product.strip()

    #Now ask the user for the product cost.
    while True:
        #Try-except to make sure that a float is entered.    
        try:
            cost = float(input("Please enter the cost of the shoe: "))
        except:
            print("Cost must be numeric, please reenter.")
            continue
        #Make sure cost is positive.
        if cost < 0:
            print("The cost of the product must be greater than or equal to zero, please reenter.")
            continue
        #If all the checks pass, then break the while loop.
        break

    #Now ask the user for the quantity.
    while True:
        #Try-except to make sure that an integer is entered.    
        try:
            quantity = int(input("Please enter the quantity of the shoe in stock: "))
        except:
            print("Quantity must be numeric, please reenter.")
            continue
        #Make sure quantity is positive.
        if quantity < 0:
            print("The quantity of the product must be greater than or equal to zero, please reenter.")
            continue
        #If all the checks pass, then break the while loop.
        break 

    #Create an object for the new Shoe.
    NewShoe = Shoe(country,code,product,cost,quantity)

    #Task description does not state this, but ideally the inventory.txt file should be updated.
    filename = "inventory.txt"
    #First check if the file exists.
    try:
        with open(filename, 'r') as f:
            pass
    except FileNotFoundError as error:
        #If the file doesn't exist, then create it.
        with open(filename,'w') as f:
            f.write("Country,Code,Product,Cost,Quantity\n")
            f.write(NewShoe.__str__())
    else:
        #If the file does exist, check if the headerline is there.
        with open(filename, 'r') as f:
            count = -1
            for count, line in enumerate(f):
                pass
       #If the file exists but the headerline is missing, then add it.
       #Also add the new shoe to the file.
        with open(filename,'a') as f:
            if count == -1:
                f.write("Country,Code,Product,Cost,Quantity")
            f.write("\n")
            f.write(NewShoe.__str__())
            #Finally also append the item to the shoe list.
            shoe_list.append(NewShoe)        

#Function to view details of all shoes.
def view_all():
    #Create empty table list.
    table = []
    #Loop over all shoe objects in the shoe list.
    for item in shoe_list:
        #Get string representation of object using the Shoe class method, and split using comma as delimiter.
        new_row = item.__str__().split(',')
        #Append a list of each object attribute to the table list.
        table.append([new_row[0],new_row[1],new_row[2],new_row[3],new_row[4]])
    print(tabulate(table, headers=["Country","Code","Product","Cost / R","Quantity"], tablefmt="rounded_outline"))

def re_stock():
    #Find the shoe object with the lowest quantity.
    #First make a list of the shoe quantities.
    quantities = []
    for shoe in shoe_list:
        quantities.append(int(shoe.quantity)) 
    #Count the number of minimum quantities.
    num_min = quantities.count(min(quantities))
    #If there is only one minimum, save the minimum index.
    if num_min == 1:
        min_index = quantities.index(min(quantities))
    #If there is more than one minimum, then find the indices of each minimum. 
    elif num_min >= 1:
        start_at = -1
        locs = []
        while True:
            try:
                loc = quantities.index(min(quantities),start_at+1)
            except ValueError:
                break
            else:
                locs.append(loc)
                start_at = loc
        #Now print all of the minima and ask the user which one to pick.
        print(f"There are multiple items with the same minimum value:")
        for i in range(0,len(locs)):
            index = locs[i]
            print(f"Index {index}: {shoe_list[index].__str__()}")
        #Make sure that the index is a valid integer.
        while True:
            try:
                user_index = int(input("Please enter the index of the shoe you would like to restock."))
            except ValueError:
                print("The index must be an integer.")
                continue
            else:
                if user_index not in locs:
                    print("The index must be one of the minima, please reenter.")
                    continue
            break
        min_index = user_index

    #Now ask the user if they want to update the quantity of shoes.
    while True:
        update_choice = input("Do you want to update the quantity? (Y or N): ").lower()
        #If yes then update the shoe list and output to the file.
        if update_choice == "y":
            #Some checks to make sure a valid integer is used for the quantity.
            while True:
                try:
                    update_quantity = int(input("Please enter the new quantity: "))
                except ValueError:
                    print("New quantity must be an integer, please reenter.")
                    continue
                else:
                    if update_quantity >= 0:
                        #When all the checks have passed, update the quantity in the shoe list.
                        shoe_list[min_index].quantity = update_quantity
                        #Now update the file, can just overwrite the file this time. 
                        filename = "inventory.txt"
                        with open(filename, 'w') as f:
                            f.write("Country,Code,Product,Cost,Quantity\n")
                            for shoe in shoe_list:
                                f.write(f"{shoe.__str__()}\n")
                    else:
                        print("New quantity must be a positive integer, please reenter.")
                break
            break

        #If no then exit the function.
        elif update_choice == "n":
            break
        else:
            print("Invalid option, please enter Y or N.")
            continue
    
def search_shoe():
    #Ask the user for the product code.
    while True:
        #Try-except to make sure that an integer is entered.
        try:
            code = int(input("Please enter the code of the shoe, without the SKU prefix: "))
        except:
            print("Code must be numeric, please reenter.")
            continue
        #Extra check to make sure the code is 5 letters long.
        if len(str(code)) != 5:
            print("The product code should have a length of 5, please reenter.")
            continue
        #If the code is valid, then break the while loop.   
        break
    #Now add on the SKU prefix
    code = "SKU" + str(code)
    
    #Build a list of the shoe codes.
    codes = []
    for shoe in shoe_list:
        codes.append(shoe.code) 
    #Print a string representation of the matching Shoe object.
    shoe_index = codes.index(code)
    print(f"{shoe_list[shoe_index].__str__()}\n")
    
def value_per_item():
    #Build and display a table similar to the view_all function, but just with product code and total value.
    table = []
    for shoe in shoe_list:
        total_value = float(shoe.cost) * float(shoe.quantity)
        #Append the results to the table list.
        table.append([shoe.product,shoe.code,total_value])
    print(tabulate(table, headers=["Product","Code","Total Value"], tablefmt="rounded_outline"))

def highest_qty():
    #Find the shoe object with the highest quantity.
    #First make a list of the shoe quantities.
    quantities = []
    for shoe in shoe_list:
        quantities.append(int(shoe.quantity)) 
    #Find the indices of each maximum. 
    start_at = -1
    locs = []
    while True:
        try:
            loc = quantities.index(max(quantities),start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    #Now print each item with the highest quantity and print that they are for sale.
    for i in range(0,len(locs)):
        index = locs[i]
        print(f"{shoe_list[index].product} is for sale! It costs R{shoe_list[index].cost}.\n")


#==========Main Menu=============
#Uncomment this to automatically read the inventory file when starting the program.
#read_shoes_data()
line_rule = "─"*60
print("Welcome to the inventory system.\n", line_rule)
while True:
    
    #Present the menu to the user and make sure that the user input is converted to lower case.
    menu = input(f'''Please select one of the following options below:
ra - read shoe data from file (append to inventory list)
ro - read shoe data from file (overwrite inventory list)
as - add new shoe
va - view all shoes
rs - restock shoes
ss - search shoes
vp - calculate value per item
hq - calculate the most stocked shoe
e - exit
{line_rule}
: ''').lower()

    #Perform functions based on input.
    if menu == 'ra':
        read_shoes_data()
        
    elif menu =='ro':
        #This option clears the existing shoe list before reading the inventory.txt file
        shoe_list = []
        read_shoes_data()

    elif menu == 'as':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 'rs':
        re_stock()
        
    elif menu == 'ss':
        search_shoe()

    elif menu == "vp":
        value_per_item()

    elif menu == 'hq':
        highest_qty()
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, please try again.")