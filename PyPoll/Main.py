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
                
                
        for row in rows:
            if row[2] == "Khan":
                k = k + 1 
                
        for row in rows:
            if row[2] == "Correy":
                c = c + 1
                    
        for row in rows:
            if row[2] == "Li":
                l = l + 1
                
        for row in rows:
            if row[2] == "O'Tooley":  
                ot = ot + 1                
                
        
voters = (len(rows)) 

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
    winname = "Khan"
        
if win.index(winner) == 1:
    winname = "Correy"
        
if win.index(winner) == 2:
    winname = "Li"
        
if win.index(winner) == 3:
    winname == "O'Tooley"
    


f = open("Analysis/Analysis.txt", "a")

f.write("Election Analysis \n")

f.write("Total no. of votes: " + str(voters) + "\n")

f.write( "Khan: " + str(k) + " votes " + str(k2) + "%" + "\n")

f.write("Correy: " + str(c) + " votes " + str(c2) + "%" + "\n")

f.write("Li: " + str(l) + " votes " + str(l2) + "%" + "\n")

f.write("O'Tooley: " + str(ot) + " votes " + str(ot2) + "%" + "\n")

f.write("Winner is " + winname + "\n")

f.close()