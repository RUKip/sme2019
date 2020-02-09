"""
Read the design smells .csv file and aggregate the results
into the main components. The results for the main components
are shown in the standard output.
"""

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("../designitejava-result/designCodeSmells.csv") 

# Store each component as a key. The value is another dictionary
# for which the key is the code smell and the value is the count
# of the code smell.
frequency = {}
for row in data.itertuples():
    packageName = row[2]
    codeSmell = row[4]

    if packageName in frequency:
        valueDictionary = frequency[packageName]
        if (codeSmell in valueDictionary):
            valueDictionary[codeSmell] = valueDictionary[codeSmell] + 1
        else:
            valueDictionary[codeSmell] = 1

        frequency[packageName] = valueDictionary
    else:
        frequency[packageName] = {codeSmell:1}


def printComponent(component, frequency):
    if (component in frequency):
        print(component)
        valueDictionary = dict(frequency[component])
        #print(value)
        for key in valueDictionary:
            print("    " + key.ljust(40) + ": " + str(valueDictionary[key]))
    else:
        print ("Component " + component + " no found!")
    print()

# All components analyzed have the following path base
component_base = "org.gjt.sp.jedit"

# Retrieve gui
current = ".gui"
printComponent(component_base + current, frequency)

# Retrieve textarea
current = ".textarea"
printComponent(component_base + current, frequency)

# Retrieve menu
current = ".menu"
printComponent(component_base + current, frequency)

# Retrieve options
current = ".options"
printComponent(component_base + current, frequency)

# Retrieve jEdit
current = ""
printComponent(component_base + current, frequency)

# Retrieve io
current = ".io"
printComponent(component_base + current, frequency)

# Retrieve bsh
current = ".bsh"
printComponent(component_base + current, frequency)


