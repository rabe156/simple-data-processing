#Simple data processing Project 
import csv
###Main functions 
def Menu (Dataset,DatasetName) :
    print("========================================\n DATA ANALYZER\n========================================\nDataset:" ,DatasetName,"\nRecords:" ,count(Dataset),"\n1. Show all orders\n2. Filter orders\n3. Statistics\n4. Sort orders\n5. Find orders\n7. Quit\n")
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

def CleanData(List , Schema) :
    ValidRows=[]
    Errors=[]
    for Rownumber ,Row in enumerate(List , start=2) :
        RowErrors=Validation(Row , Schema ,Rownumber)
        if len(RowErrors) == 0 :
            ValidRows.append(Row)
        else : Errors.extend(RowErrors)

    return ValidRows , Errors

def ProcessData(List , CItem) :
    for Row in List :
        for item in CItem :
            if Row.get(item) == '' :
                Row[item]="0"

    for item   in List :
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
            operator = input ("which operator do you choose \nAND \nOR \n").lower().strip()
            if operator == "or" :
                Firstop=[]
                Firstop=Dict[First](List , FirstVal ,Com)
                Secondop=[]
                Secondop=Dict[Second](List , SecondVal ,Com)
                seen_names=set()
                or_result=[]
                for item in (Firstop+Secondop) :
                    if item["order_id"] not in seen_names :
                        or_result.append(item)
                        seen_names.add(item["order_id"])
                if len(or_result) == 0 :
                    print("there is no order \n")
                else :
                    print("the orders of this combined filter are :")
                    for item in or_result :
                        print(item)             

            if operator == "and" :
                Firstop=[]
                Firstop=Dict[First](List , FirstVal ,Com)
                Secondop=[]
                Secondop=Dict[Second](List , SecondVal ,Com)
                NamesInS={item["order_id"] for item in Secondop}
                and_result=[item for item in Firstop if item["order_id"] in NamesInS]
                print(len(and_result))
                if len(and_result) == 0 :

                    print("there is no order \n")
                else :
                    print("the order of this combined filter are :")
                    for item in and_result :
                        print(item)
            break    
        else :  print("filtre does not exist enter a filter from the menu")
def Statistics (List) :
    print("the statistics of this CSV file are : \n")
    print("the average age is \n", AverageAge(List))
    print("the average rating is \n", AverageRating(List))
    print("the total of the quantiy sold is \n", TotalQuantity(List))
    print("the total revenue is \n", TotalRevenue(List))
    print("the minimum order value is \n", MinOrder(List))
    print("the maximum order value is \n", MaxOrder(List))
    return
def Sort(List , Columns) :
    while True :
        Choice=input("Please choose a sorting option from the following \n1. price\n2. quantity\n3.  rating\n4.  age\n5.  total value \n").strip().lower()
        if Choice == "age" or Choice == "4" :
            Choice2=input("Ascending Or Descending\n").capitalize()
            Sorted=SortbyAge(List,Choice2)
            ShowAll(Sorted , Columns)
            break
        elif Choice == "quantity" or Choice == "2":
            Choice2=input("Ascending Or Descending\n").capitalize()
            Sorted=SortbyQuantity(List,Choice2)
            ShowAll(Sorted , Columns)
            break
        elif Choice == "rating" or Choice == "3":
            Choice2=input("Ascending Or Descending\n").capitalize()
            Sorted=SortbyRating(List,Choice2)
            ShowAll(Sorted , Columns)
            break
        elif Choice == "price" or Choice == "1":
            Choice2=input("Ascending Or Descending\n").capitalize()
            Sorted=SortbyPrice(List,Choice2)
            ShowAll(Sorted , Columns)
            break
        elif Choice == "total value" or Choice == "5":
            Choice2=input("Ascending Or Descending\n").capitalize()
            Sorted=SortbyTotalV(List,Choice2)
            ShowAll(Sorted , Columns)
            break
        else : print("please enter a valid sort choice \n")

def Find(List) :
    while True :
        Choice=input("choose from this list \n1.expensive order\n2.cheapest order\n3.highest-rated order\n4.customer\n5.product\n").strip().lower()
        if Choice == "expensive order" or Choice == "1" :
            Found=FindExpensive(List)
            PrintFound(Found, Choice)
            break
        elif Choice == "cheapest order" or Choice == "2"  :
            Found=FindCheapest(List)
            PrintFound(Found , Choice)
            break
        elif Choice == "highest-rated order" or Choice == "3"  :
            Found=FindHighRated(List)
            PrintFound(Found , Choice)
            break
        elif Choice == "customer" or Choice == "4" :
            Choice2=input("what customer you are looking for : \n")
            Found=FindCustomer(List,Choice2)
            PrintFound(Found ,Choice2)
            break
        elif Choice == "product" or Choice == "5" :
            Choice2=input("what product you are looking for : \n")
            Found=FindProduct(List,Choice2)
            PrintFound(Found , Choice2)
            break
        else : print("please entre a find option from the list")
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

def Validation(List , Schema , RNumber) :
    RErrors =[]
    for Dictkey , DictValue in Schema.items() :
        Value = List.get(Dictkey) 
        if Value is None :
            RErrors.append(f"missing column : {Dictkey}")
            continue
        Value=Value.strip()
        if Value == '' :
            if DictValue["required"] == True :
                RErrors.append(f"{Dictkey} is empty")
                continue
        try :
            if DictValue["type"] == int :
                ConvertedValue = int(Value)
            elif DictValue["type"] == float :
                ConvertedValue =float(Value)
            elif DictValue["type"] == str :
                ConvertedValue=Value
        except ValueError :
            RErrors.append(
                f"{Dictkey} must be ,got '{Value}'"
            )
            continue
        if "min" in DictValue and ConvertedValue < DictValue["min"] :
            RErrors.append(f"{Dictkey} can not be less than {DictValue['min']}")
        if "max" in DictValue and ConvertedValue > DictValue["max"] :
            RErrors.append(f"{Dictkey} can not be less than {DictValue['max']}")    

    return RErrors

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

def AverageAge(List) :
    TotalAge=0
    count=0
    for item in List :
        TotalAge=TotalAge+int(item["age"])
        count=count+1
    return float(TotalAge/count)

def AverageRating(List) :
    TotalRating=0
    count=0
    for item in List :
        TotalRating=TotalRating+int(item["rating"])
        count=count+1
    return float(TotalRating/count)

def TotalQuantity(List) :
    TotalQuantity=0
    for item in List :
        TotalQuantity=TotalQuantity+int(item["quantity"])
    return float(TotalQuantity)

def TotalRevenue(List) :
    TotalRevenue=0
    for item in List :
        TotalRevenue=TotalRevenue+float(item["total"])
    return float(TotalRevenue)

def MinOrder(List) :
    Values=[]
    for item in List :
        Values.append(float(item["total"]))
    return min(Values)

def MaxOrder(List) :
    Values=[]
    for item in List :
        Values.append(float(item["total"]))
    return max(Values)

def SortbyAge(List , UInput) :
    SortedList=sorted ( List , reverse=(UInput == "Descending") , key=lambda item : int(item["age"]) ) 
    return SortedList

def SortbyQuantity(List , UInput) :
    SortedList=sorted ( List , reverse=(UInput == "Descending") , key=lambda item : int(item["quantity"]) ) 
    return SortedList

def SortbyRating(List , UInput) :
    SortedList=sorted ( List , reverse=(UInput == "Descending") , key=lambda item : int(item["rating"]) ) 
    return SortedList

def SortbyPrice(List , UInput) :
    SortedList=sorted ( List , reverse=(UInput == "Descending") , key=lambda item : float(item["unit_price"]) ) 
    return SortedList

def SortbyTotalV(List , UInput) :
    SortedList=sorted ( List , reverse=(UInput == "Descending") , key=lambda item : float(item["total"]) ) 
    return SortedList

def FindExpensive(List) :
    Value=[]
    Max=MaxOrder(List)
    print(Max)
    Value=list(filter(lambda item :float(item.get("total")) == Max,List))
    return Value
def FindCheapest(List) :
    ValueL=[]
    Value=list(min(List , key= lambda item : float(item.get("total"))))
    ValueL.append(Value)
    return ValueL
def FindHighRated(List) :
    ValueL=[]
    Value=max(List , key= lambda item : float(item.get("rating")))
    ValueL.append(Value)
    return ValueL
def FindCustomer(List , Customer) :
    Value=[]
    Value=list(filter(lambda item:item.get("customer")== Customer , List))
    return Value
def FindProduct(List , Product) :
    Value=[]
    Value=list(filter(lambda item:item.get("product")== Product , List))
    return Value
def PrintFound(List , IValue ) :
    print("---" , IValue ,"---\n")
    for item in List:
        for key , value in item.items() :
            print(key ," = " ,value)
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
Schema={
    "order_id":{"type" : int , "required" :True},
    "customer": {"type": str, "required": True},
    "age": {"type": int, "required": True, "min": 0, "max": 120},
    "city": {"type": str, "required": True},
    "category": {"type": str, "required": True},
    "product": {"type": str, "required": True},
    "quantity": {"type": int, "required": True, "min": 0},
    "unit_price": {"type": float, "required": True, "min": 0},
    "rating": {"type": int, "required": True, "min": 1, "max": 5}
}
while quit == False :
    try :
            ###FileName=input("which data set you want to treat : \n")
            FileName="orders.csv"
            with open(FileName, "r") as file :
                Rows,Columns= LoadData(file)
                if len(Rows) == 0 :
                    print("data set is empty please entre another dataset") 
                    continue
                Valid ,Errors = CleanData(Rows , Schema)
                print("\nvalid rows are : " , len(Valid))
                print("\n invalid rows are :" ,len(Errors))
                for Error in Errors :
                    print(Error)
                    print("end invalid")
                ProcRows , ProcColumns =ProcessData(Valid ,Columns)
                ###the main loop to display the menu until the user quits 
                while quit == False :
                    op=Menu(ProcRows,FileName)
                    if op == 7 : 
                        quit = True
                    if op == 1 or op == 4 : Operations[op](ProcRows ,ProcColumns)
                    if op ==2 : Operations[op](ProcRows)
                    if op ==3 or op == 5 : Operations[op](ProcRows)
    except FileNotFoundError :
        print("enter a valid file name \n")
    except PermissionError :
        print("you do not have the permission to open this file try another one \n")
    except OSError as e :
        print(f"a system error occured : {e}")
        


