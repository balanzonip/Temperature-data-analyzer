# Temperature-data-analyzer

A beginner python project that analyzes temperature measurements stored in a CSV file.

##Features
-Reads timestamp and temperature values from  a CSV file.
-Calculates the mean, minimum and maximum  temperature.
-Flags measurements outside configurable thresholds.
-Creates a line chart and saves it as 'temperature_plot.png'.

##Requirements
-Python 3
-matplotlib

Install the dependency:
'''bash
pip install -r requirements.txt


##Run
Place 'temperature.csv in the project folder,then run:
'''bash
python main.py

##Sample data
The included CSV contains example measurements for testing. The data are illustrative, not real sensor readings.

##What i learned
-Reading structured CSV data in Python
-Working with lists, loops, conditions and functions
-Calculating summary statistics
-Plotting data with matplotlib

##Possible improvements
-Validate missing or invalid values
-Read threshholds from a configurations file
-Export the summary to a text or CSV report
