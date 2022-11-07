from WebScrape import WebScrape as Ws
import os


def main():
    path = input("Enter CSV path location: ")
    path = r'' + path
    if not os.path.exists(path):
        os.makedirs(path)

    dates = Ws.date_list(12, 2016, 1, 2019)

    # puts all data into a dataframe then converts it to a CSV
    df_all_data = Ws.scrape_site(dates, path)
    df_all_data.to_csv(path + '\\df_all_data.csv')


if __name__ == "__main__":
    main()
