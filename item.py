#items
import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",passwd="arnav",database="mart")
cursor=mycon.cursor()
#View Items
def items():                                         #MAIN FUNCTION
    print("1: View Items")
    print("2: Update Items")
    s=input("Choose an option[1/2]:")
    if s=="1":
        view_items()
    elif s=="2":
        update_items()
    else:
        print("Please choose a valid option.")
def view_items():                                    #sub-main function
    print("1:View All Items")
    print("2:Search Items")
    s=input("Choose an option[1/2]:")
    if s=="1":
        all_items()
    elif s=="2":
        search_items()
    else:
        print("Please choose a valid option")
def all_items():
    cursor.execute("select * from items")
    data=cursor.fetchall()
    print("%-10s"%"ITEM CODE","%-40s"%"PRODUCT NAME","%-30s"%"CATEGORY","%-30s"%"QUANTITY","%-30s"%"PRICE")
    print("**************************************************************************************************************************")
    for row in data:
        print("%-10s"%row[0],"%-40s"%row[1],"%-30s"%row[2],"%-30s"%row[3],"%-30s"%row[4])
def search_items():
    a=input("What Would You Like to Search for?[item_code,product_name,category,quantity,price]:")
    x=input("Enter valid "+str(a)+":")
    if a=="product_name" or a=="category":
        cursor.execute("select * from items where "+str(a)+"=\""+str(x)+"\";")
        data=cursor.fetchall()
        if data!=None:
            print("%-10s"%"ITEM CODE","%-40s"%"PRODUCT NAME","%-30s"%"CATEGORY","%-30s"%"QUANTITY","%-30s"%"PRICE")
            print("**************************************************************************************************************************")
            for row in data:
                print("%-10s"%row[0],"%-40s"%row[1],"%-30s"%row[2],"%-30s"%row[3],"%-30s"%row[4])
        else:
            print(a,"doesn't exist")
    if a=="item_code" or a=="quantity" or a=="price":
        cursor.execute("select * from items where "+str(a)+"="+str(x))
        data=cursor.fetchall()
        if data!=None:
            print("%-10s"%"ITEM CODE","%-40s"%"PRODUCT NAME","%-30s"%"CATEGORY","%-30s"%"QUANTITY","%-30s"%"PRICE")
            print("**************************************************************************************************************************")
            for row in data:
                print("%-10s"%row[0],"%-40s"%row[1],"%-30s"%row[2],"%-30s"%row[3],"%-30s"%row[4])
        else:
            print(a,"doesn't exist")
#Update Items
def update_items():                             #sub-main function
    print("1:Add Items")
    print("2:Remove Items")
    x=input("Choose an option[1/2]:")
    if x=="1":
        add_items()
    elif x=="2":
        remove_items()
    else:
        print("Please choose a valid option")
def add_items():
    print("-----ADDING ITEMS-----")
    ans='y'
    while ans.lower()=='y':
        item_code=int(input("Enter Item Code:"))
        product_name=input("Enter Product Name:")
        category=input("Enter Product Category:")
        quantity=int(input("Enter Quantity of the Product:"))
        price=int(input("Enter Price of the Product:"))
        cursor.execute("insert into items(item_code,product_name,category,quantity,price)values("+str(item_code)+",\""+str(product_name)+"\""+",\""+str(category)+"\","+str(quantity)+","+str(price)+");")
        mycon.commit()
        print("***RECORDS UPDATED SUCCESSFULLY***")
        ans=input("Add more?(Press 'y'):")
def remove_items():
    print("-----REMOVING ITEMS-----")
    ans='y'
    while ans.lower()=='y':
        item_code=input("Enter Item Code:")
        cursor.execute("delete from items where item_code="+str(item_code))
        mycon.commit()
        print("***RECORDS UPDATED SUCCESSFULLY***")
        ans=input("Remove more?(Press 'y'):")


    
