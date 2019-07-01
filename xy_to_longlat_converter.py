# xy_to_longlat_converter.py
# Designed by Mihail Kaburis
# NJIT/HU Big Data Analytics REU Summer 2019

# This program converts xy coordinates from the NYPD's SQF DataSets into
# respective longitude and latitude values and appends them to the original
# dataset

# Utilizes the epsg 2263 - NAD83 / New York Long Island (ftUS) projection
# https://spatialreference.org/ref/epsg/nad83-new-york-long-island-ftus/


import sys
import pandas as pd
from pyproj import Proj

def main (input_csv, output_csv):
    # Variables
    longitude = []
    latitude = []

    # Load in the dataset
    file = open(input_csv, 'r')
    dataset = pd.read_csv(input_csv)

    # Create a data frame with the X and Y coords of stop locations
    df = pd.DataFrame(dataset, columns=['STOP_LOCATION_X', 'STOP_LOCATION_Y'])

    # Convert coords to an object of long/lat
    proj = Proj(
        '+proj=lcc +lat_1=41.03333333333333 +lat_2=40.66666666666666 +lat_0=40.16666666666666 +lon_0=-74 '
        '+x_0=300000.0000000001 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs')

    results = df.apply(lambda row: proj(row['STOP_LOCATION_X'], row['STOP_LOCATION_Y'], inverse=True), axis=1)


    # iterate through the long and lat values
    # in results and store in separate lists
    for i in range(len(results)):
        longitude.append(results[i][0])
        latitude.append(results[i][1])

    # Append longitude and latidude columns to the output.csv
    dataset = dataset.assign(longitude=longitude, latitude=latitude)

    # output the output.csv file so it is accessible for the user
    dataset.to_csv(output_csv, index = False)
    print("The coordinates conversion has been completed and stored in " + output_csv + "!")

def instructions():
    sys.stderr.write("Welcome to xy_to_longlat_converter.py\n")
    sys.stderr.write("Utilizing this program requires the following syntax:\n")
    sys.stderr.write("python xy_to_longlat_converter.py [input_name.csv] [output_name.csv]\n")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        instructions()
        sys.exit(1)
    elif not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
        instructions()
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
