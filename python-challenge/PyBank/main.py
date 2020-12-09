import os
import csv 

budget_data = os.path.join("Resources", "budget_data.csv")
financial_analysis = os.path.join("Analysis", "Financial_Analysis_output.txt")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader) #skip header (first) row
    #print(csv_header)

    #create lists for appenderd looped values in
    pl_change = []
    month_change = []
    total_change = []
    #define and start values
    total_months = 0
    total_pl = 0
    average_change = 0
    i = 0
    max_profit = 0
    min_profit = 0
   
    #First loop runs through totals 
    for row in csv_reader:
        total_months = total_months + 1
        #print(total_months)
        total_pl += int(row[1])
        #print(total_pl)
        
        total_change = [] 
        pl_change.append(int(row[1]))
        month_change.append(row[0]) 
        
        for i in range(1 , len(pl_change)): #second loop to calulculate average change and look at previous change
            #https://stackoverflow.com/questions/7172933/calculate-difference-between-adjacent-items-in-a-python-list
             total_change.append(pl_change[i]-(pl_change[i-1])) #append values from previous to curent looped value
 
average_change = round(sum(total_change)/ len(total_change),2)
#print(average_change)

max_profit = max(total_change) #find min and max values
min_profit = min(total_change)
max_month = total_change.index(max_profit) #index the max and min months to max and min profits
min_month = total_change.index(min_profit)
#print(total_months)
#print(total_pl)
#print(max_profit)
#print(min_profit)
#print(max_month)
#print(min_month)

analysis = ("Financial Analysis\n" 
"-------------------------------------------------\n"
f"Total Months: {total_months}\n"
f"Change Over Period: {total_pl}\n"
f"Average Change: {average_change}\n"
f"Greatest Increase in Profit: {month_change[max_month]} : {max_profit}\n"
f"Greatest Decrease in Profit: {month_change[min_month]} : {min_profit}")

print(analysis)

#make a text file with the Financial Analysis
with open(financial_analysis, "w") as txt_file: 
    txt_file.write(analysis)