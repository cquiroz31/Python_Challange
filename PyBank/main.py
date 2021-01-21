from statistics import mean
import os
import csv

monthly_change = []
values = []

Bank_csv = os.path.join('Resources','budget_data.csv')
write_csv = os.path.join('Analysis', 'output.csv')
months = 0



# CSV reader specifies delimiter and variable that holds contents
with open(Bank_csv) as csvfile: 
        
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)


    
    for c in csvreader:
    # Row counter
        months += 1

        values.append(int(c[1]))

# Calculating change in months rev
    for x, y in zip(values[0::], values[1::]):
        monthly_change.append(y-x)

    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ', months)
    print('Total: ', sum(values))
    print('Average  Change: ', round(mean(monthly_change), 2))
    print('Greatest Increase in Profits: ', max(monthly_change))
    print('Greatest Decrease in Profits: ', min(monthly_change))

with open(write_csv, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: ', months])
    csvwriter.writerow(['Total: ', sum(values)])
    csvwriter.writerow(['Average  Change: ', round(mean(monthly_change), 2)])
    csvwriter.writerow(['Greatest Increase in Profits: ', max(monthly_change)])
    csvwriter.writerow(['Greatest Decrease in Profits: ', min(monthly_change)])





    
    
     

