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
        SearchFilter= input("which serach filtre you want to use :\ncity\ncategory\nminumum ratings\nminimum total value\nage\nfor combining two filter entre combine \n")
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
        elif SearchFilter == "minimum total value" :
            SearchFilterVal= input("enter filter value\n")
            FilterMinTotalVal(List ,SearchFilterVal)
            break
        elif SearchFilter == "age" :
            SearchFilterVal= input("enter filter value\n") 
            FilterAge(List ,SearchFilterVal)
            break
        elif SearchFilter == "combine" :
            Com=True
            Dict={
                "city" :FilterCity ,
                "category" :FilterCategory ,
                "minimum ratings" :FilterMinRatings ,
                "minimum total value" :FilterMinTotalVal ,
                "age" :FilterAge ,

            }
            First=input("enter your first filter \n").lower()
            FirstVal=input("enter your first filter avlue  \n")
            Second=input("second enter your second filter\n").lower()
            SecondVal=input("second enter your second filter value\n")
            operator = input ("which operator do you choose \nAND \nOR \n")
            if operator == "OR" :
                Firstop=[]
                Firstop=Dict[First](List , FirstVal ,Com)
                Secondop=[]
                Secondop=Dict[Second](List , SecondVal ,Com)
                seen_names=set()
                or_result=[]
                for item in (Firstop+Secondop) :
                    if item["customer"] not in seen_names :
                        or_result.append(item)
                        seen_names.add(item["customer"])
                if len(or_result) == 0 :
                    print("there is no client \n")
                else :
                    print("the clients of this combined filter are :")
                    for item in or_result :
                        print(item["customer"])             

            if operator == "AND" :
                Firstop=[]
                Firstop=Dict[First](List , FirstVal ,Com)
                Secondop=[]
                Secondop=Dict[Second](List , SecondVal ,Com)
                NamesInS={item["customer"] for item in Secondop}
                and_result=[item for item in Firstop if item["customer"] in NamesInS]
                print(len(and_result))
                if len(and_result) == 0 :

                    print("there is no client \n")
                else :
                    print("the clients of this combined filter are :")
                    for item in and_result :
                        print(item["customer"])
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

def FilterCity(List,Filter,Combine=False) :
    Filtred=[]
    Filtred=list(filter(lambda item : item.get("city") == Filter ,  List) )
    if len(Filtred) == 0 and Combine == False :
        print ("sorry ther is no client from :",Filter,"\n")
    elif Combine == False:
        print ("the client from " ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])
    if Combine == True : return Filtred
  
def FilterCategory(List , Filter,Combine=False):
    Filtred=[]
    Filtred=list(filter(lambda item : item.get("category") == Filter, List))
    if len(Filtred) == 0 and Combine == False :
        print ("sorry ther is no client who has bought  :",Filter,"\n")
    elif Combine == False:
        print ("the client who bought" ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])
    if Combine == True : return Filtred

def FilterMinRatings(List , Filter,Combine=False) :
    Filtred=[]
    Filtred=list(filter(lambda item : int(item.get("rating")) >= int(Filter) , List))
    if  len(Filtred) == 0 and Combine == False :
        print ("sorry ther is no client who has   :",Filter,"\n")
    elif Combine == False:
        print ("the clients who has a rating above" ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])
    if Combine == True : return Filtred

def FilterMinTotalVal(List , Filter,Combine=False) :
    Filtred=[]
    Filtred=list(filter(lambda item : float(item.get("total")) >= float(Filter), List))
    if len(Filtred) == 0 and Combine == False :
        print ("sorry ther is no client who has   :",Filter,"\n")
    elif Combine == False:
        print ("the clients who has a totale above" ,Filter , "are : \n")
        for item in Filtred :
            print(item["customer"])
    if Combine == True : return Filtred

def FilterAge(List ,Filter,Combine=False):
    Filtred=[]
    Filtred=list(filter(lambda item : int(item.get("age")) == int(Filter), List))
    if len(Filtred) == 0 and Combine == False :
        print ("sorry ther is no client who has   :",Filter,"\n")
    elif Combine == False:
        print ("the clients who has " ,Filter , " years old are : \n")
        for item in Filtred :
            print(item["customer"])    
    if Combine == True : return Filtred

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
        


