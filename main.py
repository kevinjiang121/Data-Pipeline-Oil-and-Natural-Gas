from io import BytesIO
import openpyxl as ox
import pandas as pd
import numpy as np
import requests
import csv
import os


def scrape_site(dates):
    """
    Scraps excel file from targeted website and converts to csv files.
    Reads data into master data frame for use for calculations
    Arguments:
        dates: dates for excel file
    Outputs:
        master_df: Pandas dataframe.
        csv: saved in indicated folder
    Source: Heavily modified version of code found by Techrando.com
    Site: https://techrando.com/2019/06/26/how-to-web-scrape-oil-and-gas-data-from-the-north-dakota-oil-and-gas-division-website/
    """
    base_url = "https://www.dmr.nd.gov/oilgas/mpr/"
    df = pd.DataFrame()

    for date in dates:
        desired_url = base_url + date + '.xlsx'
        r = requests.get(desired_url)

        # Load excel into a numpy array. Uses the oil page only.
        workbook = ox.load_workbook(filename=BytesIO(r.content))
        worksheet = workbook['Oil']
        oil_arr = np.asarray(list(worksheet.values))

        # Loads numpy in csv file. Saves csv into desired location
        file = r'C:\Users\'' + date + '.csv'
        if not os.path.exists(file):
            open(file, 'a').close()
        csv_file = open(file, 'w', newline='')
        wr = csv.writer(csv_file)
        for i in range(worksheet.max_row):
            wr.writerow(oil_arr[i])
        csv_file.close()

        # Read csv to dataframes
        dataframe = pd.read_csv(file)
        df = df.append(dataframe)

    return df


def main():
    path = r'C:\Users\Oil Test'
    if not os.path.exists(path):
        os.makedirs(path)

    # Generates a list of dates given the year and month of start and stop dates
    dates = ['2016_12']
    j = 12
    for i in range(2016, 2019 + 1):
        k = 1
        while j < 12:
            if j < k or i < 2019:
                j = j + 1
                month = str(j)
                if j < 10:
                    month = str(0) + str(j)
                dates.append(str(i) + '_' + month)
            if j == k and i == 2019:
                break
        j = 0

    # puts all data into a dataframe then converts it to a CSV
    df_all_data = scrape_site(dates)
    df_all_data.to_csv(path + '\df_all_data.csv')


if __name__ == "__main__":
    main()
