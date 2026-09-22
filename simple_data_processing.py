#Simple data processing Project 
import csv
###Main functions 
def Menu (Dataset,DatasetName) :
    DatasetName=''
    print("========================================\n DATA ANALYZER\n========================================\nDataset:" ,DatasetName,"\nRecords:" ,count(Dataset),"\n1. Show all orders\n2. Filter orders\n3. Statistics\n4. Sort orders\n5. Find orders\n6. Dataset information\n7. Quit\n")
    while True :
        try :   
            op = int(input("Choose:\n"))
            if op not in Operations :
                print("please entre a number from the list \n")
            else : break 
        except ValueError :
            print("please entre a valid number \n")
    return op

def LoadData(File) :
    CsvReader=csv.DictReader(File)
    Rows=list(CsvReader)
    Columns=CsvReader.fieldnames
    return Rows , Columns

def ProcessData(List) :
    for item in List :
        Total =float(item["quantity"])*float(item["unit_price"])
        item["total"]=str(Total)
    keys= list(List[0].keys()) 
    return List , keys

def ShowAll (List , Columns ) :
    print(Columns)
    for item in List :
        ListItem=[]
        for FeildName in Columns :
            ListItem.append(item[FeildName])
        Line="," .join(ListItem)
        print(Line)

def Filter(List ) :
    while True :
        SearchFilter= input("which serach filtre you want to use :\ncity\ncategory\nminumum ratings\nminimum total value\nage\n")
        SearchFilter=SearchFilter.strip().lower()
        print(SearchFilter)
        if SearchFilter == "city" :
            SearchFilterVal= input("enter filter value\n") 
            FilterCity(List ,SearchFilterVal)
            break 
        elif SearchFilter == "category" :
            SearchFilterVal= input("enter filter value\n")
            FilterCategory(List ,SearchFilterVal)
            break
        elif SearchFilter == "minimum ratings" :
            SearchFilterVal= input("enter filter value\n")
            FilterMinRatings(List ,SearchFilterVal)
            break
        elif SearchFilter == "Minimum total value" :
            SearchFilterVal= input("enter filter value\n")
            FilterMinTotalVal(List ,SearchFilterVal)
            break
        elif SearchFilter == "age" :
            SearchFilterVal= input("enter filter value\n") 
            FilterAge(List ,SearchFilterVal)
            break
        else :  print("filtre does not exist enter a filter from the menu")
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
def FilterCity(List,Filter) :
    Filtred=[]
    Filtred=list(filter(lambda item : item.get("city") == Filter ,  List) )
    if len(Filtred) == 0 :
        print ("sorry ther is no client from :",Filter,"\n")
    else :
        print ("the client from " ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])
  
def FilterCategory(List , Filter):
    Filtred=[]
    Filtred=list(filter(lambda item : item.get("category") == Filter, List))
    if len(Filtred) == 0 :
        print ("sorry ther is no client who has bought  :",Filter,"\n")
    else :
        print ("the client who bought" ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])
    
def FilterMinRatings(List , Filter) :
    Filtred=[]
    Filtred=list(filter(lambda item : int(item.get("rating")) >= int(Filter) , List))
    if len(Filtred) == 0 :
        print ("sorry ther is no client who has   :",Filter,"\n")
    else :
        print ("the clients who has a rating above" ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])

def FilterMinTotalVal(List , Filter) :
    Filtred=[]
    Filtred=list(filter(lambda item : float(item.get("total")) >= float(Filter), List))
    if len(Filtred) == 0 :
        print ("sorry ther is no client who has   :",Filter,"\n")
    else :
        print ("the clients who has a totale above" ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])

def FilterAge(List ,Filter):
    Filtred=[]
    Filtred=list(filter(lambda item : int(item.get("age")) == int(Filter), List))
    if len(Filtred) == 0 :
        print ("sorry ther is no client who has   :",Filter,"\n")
    else :
        print ("the clients who has " ,Filter , " years old are : \n")
        for item in Filtred :
            print(item["customer"])    
    return

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
###load and process the data 
quit = False
end=False
while quit == False :
    try :
            ###FileName=input("which data set you want to treat : \n")
            FileName="orders.csv"
            with open(FileName, "r") as file :
                Rows,Columns= LoadData(file)
                ProcRows , ProcColumns =ProcessData(Rows)
                ###the main loop to display the menu until the user quits 
                while quit == False :
                    op=Menu(Rows,FileName)
                    if op == 7 : 
                        quit = True
                    if op == 1 : Operations[op](ProcRows ,ProcColumns)
                    if op ==2 : Operations[op](ProcRows)
    except FileNotFoundError :
        print("enter a valid file name \n")
    except PermissionError :
        print("you do not have the permission to open this file try another one \n")
    except OSError as e :
        print(f"a system error occured : {e}")
        


