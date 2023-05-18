import os
import csv

budget_data_csv = os.path.join('resources','budget_data.csv')

#establish needed varibles
date=[]
profit_losses=[]
monthly_change=[]
total_change_profits=0.00
start_profit=1088983

#open csv file and append data
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvfile)
    for row in csvreader:
       date.append(row[0])
       profit_losses.append(row[1])
#Total Month Count
rowcount  = -1
for row in open(budget_data_csv):
  rowcount+= 1
#Net Total Number of Profit/Losses
sum = 0
with open(budget_data_csv) as csvfile:
    for row in profit_losses:
       sum=sum+int(row)
       #Average Change 
       final_profit=int(row)
       monthly_change_stored=final_profit - start_profit
       monthly_change.append(monthly_change_stored)
       total_change_profits = total_change_profits + monthly_change_stored
       start_profit=final_profit
       #Max Change/Min Change and Date
       maxincrease=max(monthly_change)
       minincrease=min(monthly_change)
       datemax=date[monthly_change.index(maxincrease)]
       datemin=date[monthly_change.index(minincrease)]
    average_change_profits=(total_change_profits/(rowcount-1))

#print to txtfile
output_path=os.path.join("analysis","Financial Analysis.txt")
with open(output_path, "w") as txtfile:

    print("Financial Analysis")
    txtfile.write("Financial Analysis"'\n')
    print("-------------------")
    txtfile.write("-----------------"'\n')
    print("Total Months:",rowcount)
    txtfile.write(f"Total Months:{round(rowcount)}"'\n')
    print(f"Total: ${round(sum)}")
    txtfile.write(f"Total: ${round(sum)}"'\n')
    print(f"Average Change:${round(average_change_profits)}")
    txtfile.write(f"Average Change:${round(average_change_profits)}"'\n')
    print(f"Greatest Increase in Profits: {datemax} (${round(maxincrease)})")
    txtfile.write(f"Greatest Increase in Profits: {datemax}(${round(maxincrease)})"'\n')
    print(f"Greatest Decrease in Profits: {datemin} (${round(minincrease)})")
    txtfile.write(f"Greatest Decrease in Profits: {datemin}(${round(minincrease)})"'\n')

