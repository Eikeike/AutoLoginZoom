import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import calendar
import locale
import sys
import locale
locale.setlocale(locale.LC_ALL, 'de_DE')
def get_lectures():
    rapla = "https://rapla.dhbw-stuttgart.de/rapla?key=txB1FOi5xd1wUJBWuX8lJhGDUgtMSFmnKLgAG_NVMhB93u2tTCeML3e7RYaWBUP-&today=Heute"
    # rapla = sys.argv[0] + "&today=Heute"

    page = requests.get(rapla)
    content = BeautifulSoup(page.content, 'html.parser')
    week = content.find_all('td', {'class': 'week_block'})

    lectures = []
    dateStr = "" + str(datetime.today().date().isocalendar()[1] - 1 ) + " " + str(datetime.today().date().isocalendar()[0])
    #print(dateStr)

    #thisWeek = datetime.today
    for block in week:
        name = block.find('td', {'class':'value'}).getText()
        tooltip = block.find('span', {'class': 'tooltip'})
        date = tooltip.find('div', string=lambda text: 'erstellt' not in text.lower()).getText()
        start = date.split("-")[0].strip()
        if('wöchentlich' in date):
            dateStr = dateStr + " " + str(date.split("-")[0].split(" ")[0]) + " " + str(date.split("-")[0].split(" ")[1])
            print(dateStr)
            #time = "Moin"
            time = datetime.strptime(dateStr, "%U %Y %a %H:%M")
        else:
            time = datetime.strptime(start, "%a %d.%m.%y %H:%M")
        #print(time)
        lectures.append({name: time})
    return lectures



