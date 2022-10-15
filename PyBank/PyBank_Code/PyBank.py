import os
import csv

Budget_data_path= os.path.join("..", "Resources", "Budget_data.csv")

with open (Budget_data_path) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    csvheader= next(csvfile)

    date = []
    profit_loss = []
    monthly_profit_loss = []
    total_month = 0
    total_profit_loss = 0
   
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

    total_month = len(date)
    total_profit_loss = sum(profit_loss)

    for x in range(1,len(profit_loss)):
        monthly_profit_loss.append(profit_loss[x] - profit_loss[x-1])

    average_change = sum(monthly_profit_loss) / (total_month - 1)
    greatest_increase_profit = max(monthly_profit_loss)
    greatest_decrease_profit = min(monthly_profit_loss)

    date_greatest_increase_profit = date[monthly_profit_loss.index(greatest_increase_profit) + 1]
    date_greatest_decrease_profit = date[monthly_profit_loss.index(greatest_decrease_profit) + 1]


print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: {total_profit_loss}")
print(f'Average Change: ${format(average_change,".2f")}')
print(f"Greatest Increase in Profits: {date_greatest_increase_profit} (${greatest_increase_profit})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease_profit} (${greatest_decrease_profit})")


bank_result = os.path.join("..","Analysis","results.txt")

with open(bank_result, 'w') as txtfile:
    txtfile.write("Financial Analysis"+ "\n")
    txtfile.write("-----------------------------"+ "\n")
    txtfile.write(f"Total Months: {total_month}"+ "\n")
    txtfile.write(f"Total: {total_profit_loss}"+ "\n")
    txtfile.write(f'Average Change: ${format(average_change,".2f")}'+ '\n')
    txtfile.write(f"Greatest Increase in Profits: {date_greatest_increase_profit} (${greatest_increase_profit}) "+ "\n")
    txtfile.write(f"Greatest Decrease in Profits: {date_greatest_decrease_profit} (${greatest_decrease_profit}) ")