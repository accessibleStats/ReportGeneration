'''


                     Reportgen App
           * check for recently modified files

'''
# pandas for working with dataframes and exporting report
import pandas as pd
# os interacts with directory structure and file information
import os
# glob for aggregating file label and modification informatoin
import glob
# datetime for working with file creation/modification dates and times
import datetime
# Kive modules - must import for each kivy instantiation
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config 
# textinput module to capture user input
from kivy.uix.textinput import TextInput    
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Canvas, Color, Rectangle

#override default graphics settings, allow resize with window
Config.set('graphics', 'resizable', True)

# points to associated kv file - another option is to name your "App" with the same name as your kv file.
Builder.load_file('reportgen.kv')


class MyLayout(Widget):
    # function to write report to csv
    def outputtocsv(moddf):
        fileoutputpath = str(input('Enter the path for your report - no encapsulation necessary:'))
        moddf.to_csv(fileoutputpath + "mod")
    
    def click(self):
         # variables list
        moddate = []
        filenames = []
        finallist = []
        weekago = []
        zippedlist = []
        #variable to store path from text input box
        p = StringProperty()
        p = self.ids.path_input.text

        # sets date range to one week prior
        weekago = datetime.date.today() - datetime.timedelta(days=7)
        # glob grabs the file information
        for x in glob.glob(p):
            filenames.append(x) 
        # datetime for file date modification
        for n in glob.glob(p): 
            moddate.append(datetime.date.fromtimestamp(os.stat(n).st_mtime))
            # zip the globs
        zippedlist = list(zip(filenames, moddate))
        # filter the zipped list
        for n in zippedlist:
            if n[1]>weekago: finallist.append(n)
        # transform datetime to string data type - must iterate over list of tuples
        finallist = [tuple(map(str, x)) for x in finallist]

        # transform to dataframe for reports
        filedf = pd.DataFrame([finallist])
        # creates series
        tfiledf = pd.DataFrame.transpose(filedf)
        # separate tuples in 0 col using .tolist() function
        moddf = pd.DataFrame(tfiledf[:][0].tolist())
        moddf.columns = ['File Name', 'Mod Date']
        # testing
        print(moddf)
        print(type(moddf))
        #variable to store path from text input box
        o = StringProperty()
        o = self.ids.path_input2.text 
        #output csv report
        moddf.to_csv(o)
   


# creating the App class
class ReportApp(App):       
    # returning the instance of root class
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    ReportApp().run()
