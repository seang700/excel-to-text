

#function to convert excel entries into usable data
def integer(entry): #integer turns "5" into 5
    return int(entry)

def percent(entry): #percent turns "25.00%" into 25.00
    return float( entry[0:-1] )

rows_one = ['Revenue', 'Gross Profit', 'Gross Margin', 'Adj. EBITDA', 'Adj. EBITDA Margin'] #row titles on index 1; which rows are we interested in
convs = [integer, integer, percent, integer, percent]
dates = [] #dates will be before/after as found on line 1 of the csv, columns 2 and 3
f = open('C:/Users/Sean/Desktop/CFG Documents/2018.09 CFG FIle_v5.csv') #open the file
for line in f: #reading through each line
    line = line.strip().split(',') #split the csv by comma
    if dates == []: #first line should contain dates, if there are no dates, we are on the first line
        dates.append(line[2]) #storing index 2 and 3 as first and second entry to dates list
        dates.append(line[3])

    if line[1] in rows_one: # if line's index 1 (B column) is found in the list of our rows of interest
        row_index = rows_one.index(line[1]) #numeric position/index of row keyword ("Gross Profit" would be 1, for example)
        conv_func = convs[row_index]
        before = conv_func(line[2]) #columns 2 and 3 (C and D) correspond to dates from index 2 and 3 (C and D)
        after = conv_func(line[3])
        diff = after - before #math!
        #outputing findings:
        label = "increasing" if diff >= 0 else "decreasing"
        print(line[1] + " during the period went from " + str(before) + " on " + dates[0] + " to " + str(after) + " on " + dates[1] + " " + label + " by " + str(diff) + ". " + line[1] + " during the period went from " + str(before) + " on " + dates[0] + " to " + str(after) + " on " + dates[1] + " " + label + " by " + str(diff) + ".")
        # pring exmaple new way print("%s during the period went from %d on %s to %d on %s %s by %d" % (line[1], before, dates[0], after, dates[1], label, diff)) # printf formating

#function to convert excel entries into usable data
def integer(entry): #integer turns "5" into 5
    return int(entry)

def percent(entry): #percent turns "25.00%" into 25.00
    return float( entry[0:-1] )

rows_two = ['Senior Leverage', 'Total Leverage', 'Cash Balance'] #row titles on index 1; which rows are we interested in
convs = [integer, integer, integer]
dates = [] #dates will be before/after as found on line 1 of the csv, columns 2 and 3
f = open('C:/Users/Sean/Desktop/CFG Documents/2018.09 CFG FIle_v5.csv') #open the file
for line in f: #reading through each line
    line = line.strip().split(',') #split the csv by comma
    if dates == []: #first line should contain dates, if there are no dates, we are on the first line
        dates.append(line[2]) #storing index 2 and 3 as first and second entry to dates list
        dates.append(line[3])

    if line[1] in rows_two: # if line's index 1 (B column) is found in the list of our rows of interest
        row_index = rows_two.index(line[1]) #numeric position/index of row keyword ("Gross Profit" would be 1, for example)
        conv_func = convs[row_index]
        before = conv_func(line[2]) #columns 2 and 3 (C and D) correspond to dates from index 2 and 3 (C and D)
        after = conv_func(line[3])
        diff = after - before #math!
        #outputing findings:
        label = "increasing" if diff >= 0 else "decreasing"
        print(line[1] + " during the period went from " + str(before) + " on " + dates[0] + " to " + str(after) + " on " + dates[1] + " " + label + " by " + str(diff) + ". ")
        # pring exmaple new way print("%s during the period went from %d on %s to %d on %s %s by %d" % (line[1], before, dates[0], after, dates[1], label, diff)) # printf formating

