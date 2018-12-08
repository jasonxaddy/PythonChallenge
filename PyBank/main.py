import os 
import csv


csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csv_path, 'r', newline='') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    
    # creating empty sets to append to later
    months = []
    profit_loss = []
    change = []
    diff = []
    max_month = []

    # skipping headers
    csv_header = next(csvfile)

   
# using <row[0].split(',')[0]> to pull month/year values. I had to copy and paste raw data into Excel to put it into csv format. 
# using <int(row[0].split(',')[1]) to pull Profit/Loss values because the .csv file did not split at the comma.  
# Because it didn't split, the numbers weren't formatted as integers. 
    
    for row in budget:
        months.append(row[0].split(',')[0])
        profit_loss.append(int(row[0].split(',')[1]))

    i = 1
    for i, x in enumerate(profit_loss):
        diff.append(profit_loss[i] - profit_loss[i-1])


print('Financial Analysis')
print('--------------------------------------------')

print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profit_loss)}')

#average = sum(pl)/len(months)
#print(f'Average Profit: ${average}')
#print((sum(pl)/len(pl)))

total_diff = diff.pop(0)
print(f'Average Change: $ {total_diff/len(diff)}')
print(f'Greatest Increase in Profits: (${max(diff)})')


 
print(f'Greatest Decrease in Profits: (${min(diff)})')