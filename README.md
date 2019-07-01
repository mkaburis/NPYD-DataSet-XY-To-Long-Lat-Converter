# NPYD-DataSet-XY-To-Long-Lat-Converter

##### Designed by Mihail Kaburis for the NJIT/HU REU (Summer 2019)

###### Adapted from https://github.com/mattpiccolella/stop-and-frisk/blob/

## Getting Started

The NYPD_DataSet-XY-TO-Long-Lat-Converter contains all necessary files (aside from the dependencies).

## Installing the NYPD_DataSet-XY-TO-Long-Lat-Converter

Change your working directory to the folder in which you have *xy_to_long_lat_conveter.py*

To install all necessary packages to run *xy_to_long_lat_conveter.py* please utilize the following command: 

`install -r requirements.txt`

## Utilizing the NYPD_DataSet-XY-TO-Long-Lat-Converter

Once you have successfully setup *xy_to_long_lat_conveter.py*, you may use the following command to convert
an input .csv file from the [NYPD's Stop Question and Frisk Data](https://www1.nyc.gov/site/nypd/stats/reports-analysis/stopfrisk.page):

`python xy_to_long_lat_conveter.py [input_file.csv] [output_file.csv]`

*Note that not all files from the NYPD's Stop Question and Frisk Data Website are in a .csv format. You will need to convert them to be compatible with this program. You may do so via Microsoft's Excel or any other .csv conversion program.*

## Built With

* [pandas](https://github.com/pandas-dev/pandas) - a data analysis / manipulation library for Python
* [pyproj](https://github.com/pyproj4/pyproj) - cartographic projects and coordinate transformations library


