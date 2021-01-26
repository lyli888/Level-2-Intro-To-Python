import csv


filename = "Resources/election_data.csv"
  

fields = [] 
rows = [] 
voters = 0
votes = []
candidates = []



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
votep = {}
votes = {}


for n in range(0, cnum):
    d[n] = 0

for q in range(0, cnum):
    for row in rows:
        if row[2] == candidates[q]:
            d[q] = d[q] + 1 
                
for p in range(0, cnum):
    votes[p] = d[p]

for r in range(0, cnum):
    votep[r] = (votes[r]/voters) * 100

winner = votes[0]

i = 0

for z in votes: 
    if votes[i]>winner: 
        winner=votes[i] 
        i = i + 1 


winname = candidates[i]

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