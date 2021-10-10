from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
#it's a driver that will help us open chrome browser with selenium
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    #Table Caulem Headers
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    #find all the ul tags with class = expoplanet
    for i in range(0, 452):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []

            '''
            we can see that the li tags have the name of the planet inside an anchor tag,
            and other details directly as HTML. For this,
            we need to make sure that we treat the first li tag differently and others differently.
            '''

            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                   #try cheaks for errors in a piece of code. 
                    try:
                        temp_list.append(li_tag.contents[0])
                   #except accepts the error and handles it.      
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            #XPath can be used to navigate through elements and attributes in an XML document. XPath is a syntax for defining parts of an XML document.
            #//*[@id="results"]/ul[1]/li[1]
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
