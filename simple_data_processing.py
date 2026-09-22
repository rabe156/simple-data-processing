#Simple data processing Project 
import csv
###Main functions 
def Menu (Dataset) :
    DatasetName=''
    print("========================================\nSALES DATA ANALYZER\n========================================\nDataset:" ,DatasetName,"\nRecords:" ,count(Dataset),"\n1. Show all orders\n2. Filter orders\n3. Statistics\n4. Sort orders\n5. Find orders\n6. Dataset information\n7. Quit\n")
    while True :
        try :   
            op = int(input("Choose:\n"))
            if op not in Operations :
                print("please entre a number from the list \n")
            else : break 
        except ValueError :
            print("please entre a valid number \n")
    return op

def ShowAll () :
    return
def Filter() :
    return
def Statistics () :
    return
def Sort() :
    return
def Find() :
    return
def DatasetInfo () :
    return
def Quit() :
    return
###Secondary functions 
def count(List) : 
    total =0
    for item in List :
        total =total+1
    return total
###Programme

###operation dictionary will be used to select the function 
Operations={
    1:ShowAll ,
    2:Filter ,
    3:Statistics ,
    4:Sort ,
    5:Find ,
    6:DatasetInfo ,
    7:Quit
}
###the main loop to display the menu until the user quits 
quit = False
with open("orders.csv" , "r") as file :
    CsvReader=csv.DictReader(file)
    Rows=list(CsvReader)
    while quit == False :
        op=Menu(Rows)
        if op == 7 : 
            quit = True


