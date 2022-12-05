import sys
from WebScrape import WebScrape as Ws
from LoadDatabase import LoadDatabase as ld
from UIWindow import UIWindow as ui
import pygame as pg

import os


def main():
    pg.init()
    ui.render()
    pg.display.update()
    position = [0, 0]
    path = ''

    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                position = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONUP:
                if 250 < position[0] < 550 and 50 < position[1] < 200:
                    path = input("Enter CSV path location: ")
                    path = r'' + path
                    if not os.path.exists(path):
                        os.makedirs(path)

                    dates = Ws.date_list(12, 2016, 1, 2019)

                    # puts all data into a dataframe then converts it to a CSV
                    df_all_data = Ws.scrape_site(dates, path)
                    df_all_data.to_csv(path + '\\df_all_data.csv')

                if 250 < position[0] < 550 and 300 < position[1] < 550:
                    print('Transform')

                if 250 < position[0] < 550 and 550 < position[1] < 700:
                    ld.load_database(path)

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)


if __name__ == "__main__":
    main()
