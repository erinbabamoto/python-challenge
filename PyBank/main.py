import pathlib
import csv

budget_data_csv = pathlib.Path("/Users/erinbabamoto/Desktop/USC_Bootcamp/Homework/python-challenge/PyBank/Resources/budget_data.csv")

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_months = 1
    total_profitlosses = 0
    previous_profitlosses = 0

    # header row
    csv_header = next(csvreader)
    first_row = next(csvreader)
    previous_profitlosses = int(first_row[1])
    changes = []
    months = []

    for row in csvreader:
## The total number of months included in the dataset
        total_months += 1
        months.append(row[0])

## The net total amount of "Profit/Losses" over the entire period
    profitlosses = int(row[1])
    total_profitlosses += profitlosses

## The average of the changes in "Profit/Losses" over the entire period
    profitlosses_change = profitlosses - previous_profitlosses
    changes.append(profitlosses_change)
    previous_profitlosses = profitlosses
    
average_change = sum(changes) / (total_months-1)
formatted_average_change = "{:.2f}".format(average_change)

## The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index]
print(greatest_increase_month)

## The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index]
print(greatest_decrease_month)


# export to text file
financial_analysis_csv = pathlib.Path("/Users/erinbabamoto/Desktop/USC_Bootcamp/Homework/python-challenge/PyBank/Analysis/pybank_analysis.txt")

with open(financial_analysis_csv,"w") as outputfile:
    #csvwriter = csv.writer(outputfile)
    financial_analysis = (
    f"\n\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profitlosses}\n"
    f"Average Change: ${formatted_average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )
    print(financial_analysis, end = "")

    outputfile.write(financial_analysis)