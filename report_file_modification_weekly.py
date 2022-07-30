"""


                  Modified Files Report:


                    #################


This script generates a report of files modified in the previous week from a particular directory.
Customizable for any directory or folder - Write reports to user specified locations - Use from terminal or command line.
If investigating higher levels within directory structure, report will generate list of directories modified in previous 7 days.

"""
# pandas for working with dataframes and exporting report
import pandas as pd
# os interacts with directory structure and file information
import os
# glob for aggregating file label and modification informatoin
import glob
# datetime for working with file creation/modification dates and times
import datetime

# function to write report to csv
def outputtocsv(ffiledf):
    fileoutputpath = str(input('Enter the path for your report - no encapsulation necessary:'))
    ffiledf.to_csv(fileoutputpath)

# function to gather file label and modification info
def main_function(): 
 # variables lise
    moddate = []
    filenames = []
    finallist = []
    weekago = []
    zippedlist = []
    file_path = None

    # take user input for directory to search for modified files
    file_path = input("Enter folder/directory path - no encapsulation necessary:")
    # sets date range to one week prior
    weekago = datetime.date.today() - datetime.timedelta(days=7)
    # glob grabs the file information
    for x in glob.glob(file_path):
        filenames.append(x) 
    # datetime for file date modification
    for n in glob.glob(file_path): 
        moddate.append(datetime.date.fromtimestamp(os.stat(n).st_mtime))
        # zip the globs
    zippedlist = list(zip(filenames, moddate))
    # filter the zipped list
    for n in zippedlist:
        if n[1]>weekago: finallist.append(n)

    # transform datetime to string data type 
    finallist = [tuple(map(str, x)) for x in finallist]

    # transform to dataframe for reports
    filedf = pd.DataFrame([finallist])
    # creates series
    tfiledf = pd.DataFrame.transpose(filedf)
    # separate tuples in 0 col using .tolist() function
    ffiledf = pd.DataFrame(tfiledf[:][0].tolist())
    ffiledf.columns = ['File Name', 'Mod Date']
    # testing
    print(ffiledf)
    print(type(ffiledf))

    outputtocsv(ffiledf)


# call main function
main_function()




