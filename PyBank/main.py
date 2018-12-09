import os 
import csv


csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csv_path, 'r', newline='') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    
    max_profit = 0
    max_loss = 0
    max_month = []

    # skipping headers
    csv_header = next(csvfile)

   
    first_month = next(budget)
    months = 1
    total_profit = float(first_month[1])
    total_diff = 0
    last_months_profit = float(first_month[1])
    for row in budget:
        months += 1
        current_profit = float(row[1])
        total_profit += current_profit
        current_diff = current_profit - last_months_profit
        total_diff += current_diff
        last_months_profit = current_profit
        # print(current_diff)
        # print (row)
        if current_diff > max_profit:
            max_profit = current_diff
            max_profit_month = row[0]
        if current_diff < max_loss:
            max_loss = current_diff
            max_loss_month = row[0]

print(max_profit)
print(max_loss)

    # print(total_diff)

average_diff = round((total_diff)/(months - 1), 2)

    #print(months)
    #print(total_profit)
    #print(months)
    #print(profit_loss)

   # i = 1
    # for i, x in enumerate(profit_loss):
       #diff.append(profit_loss[i] - profit_loss[i-1])
        # print(i)


#max_month = max(row[1])
#print(max_month)

#print(diff)

print('Financial Analysis')
print('--------------------------------------------')

print(f'Total Months: {months}')
print(f'Total: ${total_profit}')
print(f'Average Change : ${average_diff}')
print(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})')
print(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})')
# average = sum(pl)/len(months)
# print(f'Average Profit: ${average}')
# print((sum(pl)/len(pl)))

# total_diff = diff.pop(0)
# print(f'Average Change: $ {total_diff/len(diff)}')
# print(f'Greatest Increase in Profits: (${max(diff)})')


 
# print(f'Greatest Decrease in Profits: (${min(diff)})')