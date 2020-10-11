from bs4 import BeautifulSoup
import pandas as pd
import requests


""" TAKES AN URL AS A PARAMETERS, CREATES PAGE OBJECT FROM THAT URL,
    CREATES SOUP OBJECT USING BEAUTIFULSOUP() METHOD PARSING THE PAGE'S CONTENT TO HTML,
    CREATES WEEK OBJECT CONTAINING EVERY ELEMENTS THAT HAVE THE ID 0F SEVEN-DAY-FORECAST-BODY,
    CREATES ITEMS OBJECT CONTAINING EVERY ELEMENTS THAT HAVE THE CLASS OF TOMBSTONE-CONTAINER
    FOR EACH ELEMENT THAT HAVE PERIOD-NAME, SHORT-DESC, TEMP AS CLASSES, CREATES 3 OBJECTS: PERIOD, DESC, TEMP
    CREATES WEATHER OBJECT, CONVERTS IT TO A DATA FRAME USING PANDAS DATAFRAME() METHOD, FORMAT IT
    PRINTS WEATHER OBJECT, THEN CREATES A CSV FILE AND CONVERTS RESULTS INTO IT """


def scrape(url):

    url = str(url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id='seven-day-forecast-body')

    items = week.find_all(class_='tombstone-container')

    period = [item.find(class_='period-name').get_text() for item in items]
    desc = [item.find(class_='short-desc').get_text() for item in items]
    temp = [item.find(class_='temp').get_text() for item in items]

    results = pd.DataFrame(
        {
            'period': period,
            'description': desc,
            'temperature': temp
        }
    )

    print(results)

    accepted_answers = ['y', 'Y', 'yes', 'YES', 'Yes']
    answer = input('Convert data to CSV file? [y/n]')

    if answer in accepted_answers:
        results.to_csv('results.csv')
