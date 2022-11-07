from io import BytesIO
import openpyxl as ox
import pandas as pd
import numpy as np
import requests
import csv
import os


class WebScrape:

    def __init__(self):
        pass

    @staticmethod
    def scrape_site(dates, path):
        """
        Scraps Excel file from targeted website and converts to csv files.
        Reads data into master data frame for use for calculations
        Arguments:
            dates: dates for Excel file
            path: location for CSV file
        Outputs:
            master_df: Pandas dataframe.
            csv: saved in indicated folder
        Source: Heavily modified version of code found by Techrando.com
        Site:
        https://techrando.com/2019/06/26/how-to-web-scrape-oil-and-gas-data-from-the-north-dakota-oil-and-gas-division-website/
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
            file = path + '\\' + date + '.csv'
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

    @staticmethod
    def date_list(start_month, start_year, end_month, end_year):
        """
        Generates a list of dates that would be used to scrap the target website. The list of dates will be formatted
        as year_month. Here are the list of dates used to test web scraping.
        start_month - 12, start_year - 2016, end_month - 1, end_year - 2019
        Arguments:
            start_month: month of start date
            start_year: year of start date
            end_month: month of end date
            end_year: year of end date
        Outputs:
            dates: list of dates used to scrap website
        """
        # Generates a list of dates given the year and month of start and stop dates
        start_date = str(start_year) + '_' + str(start_month)
        dates = [start_date]
        j = 12
        for i in range(start_year, end_year + 1):
            while j < 12:
                if j < end_month or i < end_year:
                    j = j + 1
                    month = str(j)
                    if j < 10:
                        month = str(0) + str(j)
                    dates.append(str(i) + '_' + month)
                if j == end_month and i == end_year:
                    break
            j = 0
        return dates
