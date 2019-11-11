# List dependencies for os.path.join
import os
import csv

# Create lists for month and profit/ loss columns
# Create list for the monthly difference in the profit/ losses columns.  
# The first month has no difference so input 0 as the first list item 
list_of_months = []
total_profit_list = []
change_list = [0]

# Read in a .csv file to open the file
csvpath = os.path.join('C:/Users/adm/Desktop/bootcamp/RU-JER-DATA-PT-10-2019-U-C/Homework/03-Python Homework/PyBank/Resources', 'budget_data.csv')

# Open the file
with open(csvpath, newline='') as csvfile:
    
    # Read the dataset
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header 
    csv_header = next(csvfile)

    # Create loop for each row in the dataset
    for row in csvreader:
        
        # Put the months of each row into the list of months
        # Get the total number of months in the list 
        list_of_months.append(row[0])
        total_months = len(list_of_months)
        
        # Put all the profits/ losses of each row into the total profit list
        # Get the the total sum of all the profit/ losses in the dataset
        total_profit_list.append(int(row[1]))
        total_amount = sum(total_profit_list)

    # Create loop for the total number of months with changes in profit/ losses
    for x in range(total_months - 1):

        # Math formula to be looped for the changes in profit/ losses for each month
        change = total_profit_list[x + 1] - total_profit_list[x]
        # Put all the changes for each month into change list.
        change_list.append(change)
        # Sum up the total changes in profit/ losses for every month 
        total_change = sum(change_list)
        # Calculate the average changes over the total months of changes
        average_change = total_change / (total_months - 1)

    # Zip the list of changes with the list of months 
    max_date_change = zip(change_list, list_of_months)
    min_date_change = zip(change_list, list_of_months)

    # Find the greatest increase of changes with the month
    greatest_increase = max(max_date_change)
    # Find the greatest decrease of changes with the month
    greatest_decrease = min(min_date_change)

    # Print Financial Analysis results to the terminal
    print("Financial Analysis")
    print("-----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_amount}')   
    print(f'Average: ${round(average_change, 2)}')
    print(f'Greatest Increase in Profits: {greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease}')

    # Export Financial Analysis results into a text file
    csvwriter = open("Financial Analysis.txt", "w+")
    csvwriter.write("Financial Anaylsis\n")
    csvwriter.write("-----------------------------\n")
    csvwriter.write(f'Total Months: ${total_months}\n')   
    csvwriter.write(f'Total: ${total_amount}\n')   
    csvwriter.write(f'Average: ${round(average_change, 2)}\n')
    csvwriter.write(f'Greatest Increase in Profits: {greatest_increase}\n')
    csvwriter.write(f'Greatest Decrease in Profits: {greatest_decrease}\n')