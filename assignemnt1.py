# -*- coding: utf-8 -*-

#MAIN FILE
#STUDENT NAME - Ravkeerat Singh 
#Student Id - 101344680


sid = int(101344680)
sname = "Ravkeerat Singh"

print("****Student Details****")
print ("Student ID:" + str(sid))
print("Student Name:" +sname)
print("****Starts here****")
#Employee page 

#Employee check 
#checking if its a number or not 
def employee_check(input):
    try:
        val = int(input)
        print(" Valid input ")
    except ValueError:
        try:
            val = float(input)
            print(" Valid input ")
        except ValueError:
            print("Invalid input . Please try again ")
#checking for unique id 
def unique_id(emp_id):
  current = set()
  return not any (i in current or current.add(i) for i in emp_id)
#checking if input is one of the options given 
while True:
  emp_type = input("Do you work hourly or are you manager")
  if emp_type in ('hourly' , 'HOURLY' ,'Hourly', 'manager','MANAGER','Manager'):
    break
  else:
    print("Wrong input")
#asking for user input
emp_name = input("Whats your name")

emp_id = input("Enter employee id: ")
employee_check(emp_id)

emp_experience = input("Enter work experinece(in yrs): ")
employee_check(emp_experience)

emp_discount_number = input("Enter the discount number: ")
employee_check(emp_discount_number)

#checking if input is empty or not 
if emp_id is not None:
  print("NOT NULL")
elif emp_experience is not None:
  print("NOT NULL")
elif emp_discount_number is not None:
  print("NOT NULL")
else:
  print("NULL")

print("Employee list:" + emp_name + " , "+ emp_id + " , " + emp_experience + " , " + emp_discount_number)


#Item page 
def item_check(input):
    try:
        # Convert it into integer
        val = int(input)
        print(" Valid input ")
    except ValueError:
        try:
            val = float(input)
            print("Valid input . Number = ", val)
        except ValueError:
            print("Invalid input . Please try again ")


item_no = input(" Enter item number: ")
item_check(item_no)

item_cost = input("Enter the discount number: ")
item_check(item_cost)

item_cost = input("Enter the item cost: ")
item_check(item_cost)

item_name = input("Please enter the input name")

if item_no is not None:
  print("NOT NULL")
elif item_cost is not None:
  print("NOT NULL")
elif item_cost is not None:
  print("NOT NULL")
else:
  print("NULL")

print("Item list:" + item_name + " , "+ item_no + " , " + item_cost)

#Purchase page
#need to print the item page(item number , name , cost)

#menu created 
# using the while loop to print menu list  
# def create_menu():
while True:  
    print("MENU")  
    print("1. Create Employee")  
    print("2. Create Item")  
    print("3. Make Purchase")  
    print("4. All employee summary")  
    print("5. Exit")  
    users_choice = int(input("\nEnter your Choice: "))  
  
# based on the users choice the relevant method is called
    if users_choice == 1:  
        print( "\nEmployee Created\n")  
      
    elif users_choice == 2:  
        print( "\nItem Created\n")  
        
    elif users_choice == 3:  
        print( "\nPurchase Made\n")  
  
    elif users_choice == 4:  
        print( "\nEmployee Summary \n")  
         
  
  # exit the while loop
    elif users_choice == 5:  
        break  
      
    else:  
        print( "Please enter a valid Input from the list")

#adding $ to the cost  

amt = int(input("Enter the amt: "))

currency = "${:,.2f}".format(amt)
curr ="€{:,.2f}".format(amt)
print(curr)
print(currency)



