import os
import csv

csvpath = os.path.join ('C:/', 'Users', 'hongy','Desktop','python-challenge', 'PyBank', 'Budget_data.csv')

#print(csvpath)

print ("Financial Analysis")
print ("-------------------------------")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    header = next(csvreader)    
    number_of_months = len(list(csvreader))
    print(f'Total Months: ' + str(number_of_months))

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    header = next(csvreader)
    total_profit = 0
    for row in csvreader:
        total_profit = total_profit + int(row[1]) 
    print (f'Total Profit: $' + str(total_profit))


month_of_change = [ ]
net_change_list = [ ]
greatest_inc = [" ", 0]
greatest_dec = [" ", 99999999999]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    header = next(csvreader)
    new_value =0
    current_value = 0
    previous_value = 0
    for row in csvreader:
        current_value = int(row [1])
        new_value = current_value - previous_value
        previous_value = current_value
        month_of_change.append(new_value)

        if (new_value > greatest_inc[1]):
            greatest_inc [0] = row [0]
            greatest_inc [1] = new_value
        if (new_value < greatest_dec[1]):
            greatest_dec [0] = row [0]
            greatest_dec [1] = new_value
    
        new_value = 0
    month_of_change.pop(0)
    import statistics
    average_change = statistics.mean(month_of_change)
    average_change = round(average_change, 2)
    print(f'Average Change: $' + str(average_change))
    print(f'Greatest Increase in Profits: ' + str(greatest_inc[0]) + " ($" + str(greatest_inc[1]) + ")")
    print(f'Greatest Decrease in Profits: ' + str(greatest_dec[0]) + " ($" + str(greatest_dec[1]) + ")")