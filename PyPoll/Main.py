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
votep = []
votes = []
currentp = 0

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
          
votes = [k, c, l, ot]

k2 = (k/voters) * 100
c2 = (c/voters) * 100
l2 = (l/voters) * 100
ot2 = (ot/voters) * 100

votep = [k2, c2, l2, ot2]

winner = 0

i = 0

for z in votes: 
    if votes[i]>winner: 
        winner=votes[i] 
        i = i + 1 

winum = 0
winnum = votes.index(winner)

winname = d[winum]

f = open("Analysis/Analysis.txt", "a")

f.write("Election Analysis \n")

f.write("Total no. of votes: " + str(voters) + "\n")

for g in range(0, cnum):
   
    f.write(str(candidates[g]) + " " + str(votes[g]) + " votes " + str(votep[g]) + "%" + "\n")



f.write("Winner is " + winname + "\n")

f.close()

    
print("Election Analysis \n")

print("Total no. of votes: " + str(voters) + "\n")

for h in range(0, cnum):
    print(str(candidates[h]) + " " + str(votes[h]) + " votes " + str(votep[h]) + "%" + "\n")

print("Winner is " + winname + "\n")