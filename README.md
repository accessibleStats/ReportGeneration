# ReportGeneration

* Kivy application with multiple screens + navigation buttons

* App currently will check system/directories for recently modified files and generate a csv report of modified files in a specified location.

To use the kivy report generation app, install python and kivy, then create a virtual environment to launch the app. For instructions see the following link: https://kivy.org/doc/stable/gettingstarted/installation.html?highlight=virtual%20env.

The first instantiation takes user input for a directory to investigate for recently modified files and a path to export the report.

Note - the timeframe for "recently" modified files can be adjusted by changing the "days" value in the datetime.timedelta() assignment.

Note - Special Thanks to Pexels, Simon Berger, and Photomix Company for producing and hosting many free-to-use photos; the background images can be found at https://www.pexels.com/search/report/ and https://www.pexels.com/search/sunrise/.

Suggestions for improvements are welcomed and appreciated.
