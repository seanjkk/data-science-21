# Raw Data Munging

## Overview
Here, I try to make usable a real data source: **NASA's historic measurements of the Earth's surface temperatures**.  In order to do analysis of this data, some preparation work is necessary.
1. Download raw data.
1. Write a Python program to clean up (i.e. munge) the data and save it into a standard Comma-Separated Values (CSV) format text file.
1. Write a second Python program to do some simple analysis of the data in the CSV file.

### Part 1: Download the data
NASA's [GISS Surface Temperature Analysis web site](https://data.giss.nasa.gov/gistemp/) gives an overview of the data set - they publish recordings in the change of the Earth's surface temperature going back to the year 1880.  
- The numbers do not represent actual temperature readings, but rather represent temperature *anomalies*.
- Their [FAQ page](https://data.giss.nasa.gov/gistemp/faq/#q101) includes some additional explanations that might be helpful.

Download [the raw data in fixed-width column format](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt).

### Part 2: Munge it
The raw data has some some features that make it difficult to analyze with a program. 

Issues:
- there are many lines at the top and bottom of the file that contain notes and not the raw data - **all lines with notes must be removed**.
- the column headings are repeated on multiple lines throughout the file - **remove all but the first line of column headings**.
- there are some blank lines in the middle of the data - **remove all blank lines**.
- there is missing data indicated with `***` - figure out how to **handle missing data so that your analyses are correct**.
- the temperature anomalies in this data are given in 0.01 degrees Celsius.  **Convert temperature anomalies to Farenheit**, the US standard unit of temperature:
    - the formula to do this can be found within the data set
    - format the results so that there's one decimal place (use [format](https://docs.python.org/3/library/functions.html#format) with `.1f` as the second argument)
- since this data is in *fixed-width column format*, there are inconsistent numbers of spaces separating the numeric values

Running munge.py will create a cleaned data file called `clean_data.csv`

### Part 3: Analysis

`analyze.py` does the following:
- opens up your cleaned up data file, `clean_data.csv` and imports it using Python's `csv` module.
- outputs the average temperature anomaly in degrees Farenheit for each decade since 1880.  For example, output the average temperature anomaly for the decades:
    - 1880 to 1889
    - 1890 to 1899
    - 1900 to 1909
    - ...and so on.