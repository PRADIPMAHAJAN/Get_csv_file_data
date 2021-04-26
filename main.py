statename=input("What is the state:")
cost = input("Cost or Rating:")
operation = input("Operation:")

def Karnataka():
  import csv  
  sortlist=[]
  hostalcode=[]
  costlist=[]
  ratelist=[]
  newrate=[]
  D={}
  with open('file.csv', 'rt',newline='\r\n') as f:
      csv_reader = csv.reader(f)

      for line in csv_reader:
          sortlist.append(line[2])
          if line[2]=="Karnataka":
            hostalcode.append(line[1])
            costlist.append(line[3])
            ratelist.append(line[4])
  if statename=="Karnataka":          
    zip(costlist,hostalcode)
    D=(dict(zip(costlist,hostalcode)))
    max_key = max(D, key=D.get)
    hostal_code = D[max_key]
    print("Hotel with",operation,"price in",statename,"is",hostal_code,"with price",max_key)
  
  else:
    #print(ratelist)
    for x in ratelist:
        Float = float(x)
        newrate.append(Float)
    #print(newrate)
    zip(newrate,hostalcode)
    D=(dict(zip(newrate,hostalcode)))
    #print(D)
    max_key = max(D, key=D.get)
    #print(max_key)
    hostal_code = D[max_key]
    print("Hotel with ",operation,"rating in karnataka is",hostal_code,"with rating",max_key)

def Maharashtra():
  import csv  
  ratelist=[]
  list1=[]
  result =0
  sum=0
  with open('csv.csv', 'rt',newline='\r\n') as f:
      csv_reader = csv.reader(f)

      for line in csv_reader:
        list1.append(line)
        if line[2]==statename:
          ratelist.append(line[4])
      div=len(ratelist)
      print(ratelist)
      for x in ratelist:
        Float = float(x)
        result =result+Float
      avg = result/div
      print(operation,"rating of Hotel in",statename,"is",avg)
      
if statename=="Karnataka" or statename=="India":
  Karnataka()
elif statename=="Maharashtra":
  Maharashtra()
else:
  India() 
