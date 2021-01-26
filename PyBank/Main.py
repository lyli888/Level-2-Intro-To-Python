import csv

fields = []
numdata = []
caldata = []

rownum = 0
currentnum = 0
sumdata = 0
change = 0


with open('Resources/budget_data.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    fields = next(csv_reader) 
    
    
    for lines in csv_reader:
        
        currentnum = int(lines[1])
    
        sumdata = sumdata + currentnum
        caldata.append(lines[0])
        numdata.append(currentnum)
        rownum = rownum + 1





rownum = int(rownum)
difflist = []
diff = 0
i=0
j=i + 1
profitmax = 0
lossmax = 0

for x in numdata: 
        y = numdata[i]
        z = numdata[j]
        diff = (z - y)
        difflist.append(diff)    
        i = i+1
        j = j+1
        if j == rownum:
                break



diffindex = len(difflist)
             
avg=sum(difflist, 0)/len(difflist)



profitmax = max(difflist)



lossmax = min(difflist)



monthmax = difflist.index(profitmax) + 1

monthmin = difflist.index(lossmax) + 1

maxdate = caldata[monthmax]

mindate = caldata[monthmin]

f = open("Analysis/Analysis.txt", "a")

f.write("Financial Analysis \n")

f.write("Total Months: " + str(rownum) + "\n")

f.write("Total: $" + str(sumdata) + "\n")

f.write("Average Change: $" + str(avg) + "\n")

f.write("Max Profits: " + caldata[monthmax] + " $" + str(profitmax) + "\n")

f.write("Min Profits: " + caldata[monthmin] + " $" + str(lossmax))

f.close()

print("Financial Analysis \n")
print("Total Months: " + str(rownum) + "\n")
print("Total: $" + str(sumdata) + "\n")
print("Average Change: $" + str(avg) + "\n")
print("Max Profits: " + caldata[monthmax] + " $" + str(profitmax) + "\n")
print("Min Profits: " + caldata[monthmin] + " $" + str(lossmax))