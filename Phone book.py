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
