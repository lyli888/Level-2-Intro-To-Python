import csv


filename = "Resources/election_data.csv"
  

fields = [] 
rows = [] 
voters = 0
votes = []
candidates = []

k = 0
c = 0
l = 0
ot = 0

with open(filename, 'r') as csvfile: 

        csvreader = csv.reader(csvfile) 
      
  
        fields = next(csvreader) 
  
  
        for row in csvreader: 
            rows.append(row)
            votes.append(row[2])
    
    
        for x in votes: 
            if x not in candidates: 
                candidates.append(x) 
               
        
voters = (len(rows)) 
cnum = len(candidates)
d = {}
   

for a in range(0, cnum):
    d[a] = candidates[a]


for row in rows:
    if row[2] == d[0]:
        k = k + 1 
                
for row in rows:
    if row[2] == d[1]:
        c = c + 1
                    
for row in rows:
    if row[2] == d[2]:
        l = l + 1
                
for row in rows:
    if row[2] == d[3]:  
        ot = ot + 1    

k2 = (k / voters) * 100

c2 = (c / voters) * 100

l2 = (l / voters) * 100

ot2 = (ot / voters) * 100

win = [k2, c2, l2, ot2]

winner = 0

i = 0

for z in win: 
    if win[i]>winner: 
        winner=win[i] 
        i = i + 1 
        
winname = ""

if win.index(winner) == 0:
    winname = d[0]
        
if win.index(winner) == 1:
    winname = d[1]
        
if win.index(winner) == 2:
    winname = d[2]
        
if win.index(winner) == 3:
    winname == d[3]
    

f = open("Analysis/Analysis.txt", "a")

f.write("Election Analysis \n")

f.write("Total no. of votes: " + str(voters) + "\n")

for g in range(0, cnum):
    f.write(d[g] + str(k) + " votes " + str(k2) + "%" + "\n")



f.write("Winner is " + winname + "\n")

f.close()

    
print("Election Analysis \n")

print("Total no. of votes: " + str(voters) + "\n")

for h in range(0, cnum):
    print(d[h] + str(k) + " votes " + str(k2) + "%" + "\n")

print("Winner is " + winname + "\n")