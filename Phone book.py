import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\n Enter contact %d details in the following order (ONLY):" %(i+1))
        print("NOTE: * indicates mandatory fields")
        
print("...................................................................")
        temp = []
        for j in range(cols):
            
            if j == 1:
                temp.append(str(input("Enter number*: ")))
                
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = none
                    
            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == ' ' or temp[] ==
                
    print(phone_book)
    return phone_book

def menu():
    
    print("********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice: "))
def add_contact(pb):
    dip = []
    for i in range(len(pb)[0]):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
             dip.append(str(input("Enter date of(dd/mm/yy): ")))
        if i == 4:
             dip.append(str(input("Enter catagory(Family/Friends/work/others) ")))
    pb.append(dip)
    return pb
def remove_existing(pb)
ch = 1

pb = initial_phonebook()

while ch in (1, 2, 3, 4, 5):

ch = menu()

if ch == 1:

pb = add_contact(pb)

elif ch == 2:

pb = remove_existing(pb)

elif ch == 3:

pb = delete_all(pb)

elif ch == 4:

d = search_existing(pb)

if d == -1:

print("The contact does not exist. Please try again")

elif ch == 5:

display_all(pb)

else:

thanks()
