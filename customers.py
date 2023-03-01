#customers
import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",passwd="arnav",database="mart")
cursor=mycon.cursor()
def registry():                                                                                                #MAIN FUNCTION
    print("1:View registry")
    print("2:Update Registry")
    s=int(input("Choose an option[1/2]:"))
    if s==1:
        customers()
    elif s==2:
        update_registry()
    else:
        print("Please choose a valid option")
def customers():
    print("1:Show all registered customers")                                                                  #sub-main function
    print("2:Search for a customer")
    s=input("Choose an option[1/2]:")
    if s=="1":
        all_customers()
    elif s=="2":
        search_customers()
    else:
        print("Please choose a valid option.")
        
def all_customers():
    cursor.execute("select * from customers")
    data=cursor.fetchall()
    print("%-10s"%"CUSTOMER ID","%-30s"%"CUSTOMER NAME","%-30s"%"PHONE","%-30s"%"ADDRESS")
    print("******************************************************************************************")
    for row in data:
        print("%-10s"%row[0],"%-30s"%row[1],"%-30s"%row[2],"%-30s"%row[3])

def search_customers():
    a=input("what would you like to search for?[cust_id,cust_name,phone]:")
    x=input("enter valid "+str(a)+":")
    if a=="cust_name":
        cursor.execute("select * from customers where cust_name=\""+str(x)+"\"")
        data=cursor.fetchall()
        if data!=None:
            print("%-10s"%"CUSTOMER ID","%-30s"%"CUSTOMER NAME","%-30s"%"PHONE","%-30s"%"ADDRESS")
            print("******************************************************************************************")
            for row in data:
                print("%-10s"%row[0],"%-30s"%row[1],"%-30s"%row[2],"%-30s"%row[3])
        else:
            print("customer doesn't exist")
    if a=="cust_id" or a=="phone":
        cursor.execute("select * from customers where "+str(a)+"="+str(x))
        data=cursor.fetchall()
        if data!=None:
            print("%-10s"%"CUSTOMER ID","%-30s"%"CUSTOMER NAME","%-30s"%"PHONE","%-30s"%"ADDRESS")
            print("******************************************************************************************")
            for row in data:
                print("%-10s"%row[0],"%-30s"%row[1],"%-30s"%row[2],"%-30s"%row[3])
        else:
            print("customer name doesn't exist")

#registry update
def update_registry():                                                                                          #sub-main function
    print("1:Add customer")
    print("2:Remove customer")
    x=input("Choose an option[1/2], or press 'X' to exit:")
    if x=="1":
        add_customer()
    elif x=="2":
        remove_customer()
    else:
        print("Please enter a valid option")


def add_customer():
    print("--------REGISTERING CUSTOMERS--------")
    ans='y'
    while ans.lower()=='y':
        cust_id=int(input("Enter customer ID:"))
        cust_name=input("Enter customer name:")
        phone=int(input("enter phone number:"))
        address=input("Enter address:")
        cursor.execute("insert into customers(cust_id,cust_name,phone,address)values("+str(cust_id)+",\""+str(cust_name)+"\""+",\""+str(phone)+"\",\""+str(address)+"\");")
        mycon.commit()
        print("*****RECORDS UPDATED SUCCESSFULLY*****")
        ans=input("Add more?(Press 'y'):")


def remove_customer():
    print("---------REMOVING CUSTOMERS---------")
    ans="y"
    while ans.lower()=="y":
        cust_id=int(input("Enter customer ID:"))
        cursor.execute("delete from customers where cust_id="+str(cust_id))
        mycon.commit()
        print("*****RECORDS UPDATED SUCCESSFULLY*****")
        ans=input("Remove more?(Press 'y'):")
        
        

        
    
    
