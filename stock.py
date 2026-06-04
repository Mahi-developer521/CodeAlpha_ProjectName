stock={"AAPL":180,"TSLA":250,"GLG":290,"AMZN":350}#stock name and price
k=int(input("How Many Stocks Do You Want?:"))#number of stocks user want to invest
portfolio={}#to store the stock name and quantity
total=0#total investment value
file=open("file.txt","w")#to save the data in .txt format
f=open("file.csv","w")#to save the data in .csv format
while(k!=0):
    Sname=str(input("Enter the Stock Name:")).upper()
    
    Quan=int(input("Enter the Quantity:"))
    if Sname in stock:
        Investment=Quan*stock[Sname]
        total+=Investment #to calculate the total investment value
        portfolio[Sname]=Quan
        file.write(Sname)
        file.write(":")
        file.write(str(Quan))
        file.write(":")
        file.write(str(Investment))
        file.write("\n")
        f.write(Sname)
        f.write(",")
        f.write(str(Quan))
        f.write(",")
        f.write(str(Investment))
        f.write("\n")
    else:
        print("Stock not found!" \
        "Enter The Valid Stock Name")
    k-=1
if(total==0):
    print("Sorry,Your Asking for Unavailable Stocks!")
port=input("Enter for Confirmation:(1/2/0)")
if(port=="1"):
    file.write("Total Investment:$")
    file.write(str(total))
    file.close()
    print("Saved In The Format of .txt")
elif(port=="2"):
    f.write("Total , ,")
    f.write(str(total))
    f.close()
    print("Saved In The Format of .csv")
elif(port=="0"):
    print("No Data Saved.")
