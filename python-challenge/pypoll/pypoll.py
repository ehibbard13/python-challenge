import os
import csv

election_data_csv=os.path.join('resources','election_data.csv')

#define needed varibles
ballot_id=[]
county=[]
candidate=[]
new_candidates=[]
vote_count=[]
results=[]
percent=[]
winner_votes=0
x=0
y=0
z=0

#open csvfile and append with inforamtion
with open (election_data_csv) as csvfile:
      csvreader = csv.reader(csvfile, delimiter=",")
      csvheader=next(csvfile)
      for row in csvreader:
         ballot_id.append(row[0])
         county.append(row[1])
         candidate.append(row[2])
         
      totalvotes = -1
      for row in open(election_data_csv):
         totalvotes+=1
      #find total votes
      i=0
      for candid in candidate:
        if candid not in new_candidates:
            new_candidates.append(str(candid))
n=len(new_candidates)

#calculate vote count
for x in range (n):
    vote_count.append(candidate.count(new_candidates[x]))

#calculate for percent
for y in range (n):
    percent.append(f'{round((vote_count[y]/totalvotes*100), 3)}%')

#calculate winner
    if vote_count[y]>winner_votes:
      winner_votes=vote_count[y]
      winner=new_candidates[y]

for z in range(n):
   results.append(f'{new_candidates[z]}: {percent[z]} ({vote_count[z]})')

#print(results)
results_print='\n'.join(results)

output_path=os.path.join("analysis","Election_Results.txt")
with open(output_path, "w") as txtfile:
    
    print("Election Results")
    txtfile.write("Election Results"'\n')
    print("------------------")
    txtfile.write("-----------------"'\n')
    print("Total Votes:", totalvotes)
    txtfile.write(f"Total Votes:{round(totalvotes)}"'\n')
    print("------------------")
    txtfile.write("------------------"'\n')
    print(results_print)
    txtfile.write(f"{(results_print)}"'\n')
    print("------------------")
    txtfile.write("------------------"'\n')
    print("Winner: ",winner)
    txtfile.write(f"Winner:{(winner)}"'\n')
    print("------------------")
    txtfile.write("------------------"'\n')





