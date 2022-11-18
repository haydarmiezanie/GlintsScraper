# Import library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, requests, json, openpyxl, sys, timeit
from bs4 import BeautifulSoup
import pandas as pd

# Call chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define empty list
name    = []
address = []

# Define Function
def scrape_function(top_range, bot_range):
    """
    Function for start scraping.7

    Params :
    top_range (int) |   Required : Start Page
    bot_range (int) |   Required : End Page

    Sample :
    scrape_function(1,36)
    """
    # Looping page in range that user needed
    print("Scraping start")
    for page_url in range(top_range,bot_range):
        url = f"https://glints.com/id/companies?countries=ID&page={page_url}"
        driver.get(url)
        time.sleep(5)
        print("Currently on page :{}".format(page_url))
        
        # Loop item on 1 page
        for item_list in range(1,31):
            if item_list == 20:
                time.sleep(10)
                driver.get(url)
            
            # Find element using CSS Selector ( Can be Xpath )
            selector_item = f'#__next > div > div.NavigationComponentssc__DrawerContainer-sc-vokz7d-0.daViyw > div.MainContainersc__MainLayout-sc-iy5ixg-0.llLQXs > div.MainContainersc__MainBody-sc-iy5ixg-2.dyvvBG > div:nth-child(2) > div.CompaniesPagesc__CompanyCardGrid-sc-4oq9hz-6.bNwwZr > a:nth-child({item_list})'
            item          = driver.find_element("css selector",selector_item).get_attribute('href')
            
            # Check if item response is None
            if item == None:
                continue

            # Get data
            id_company      = item.split("/")[-1]
            page            = requests.get(item)
            soup            = BeautifulSoup(page.content, "html.parser")
            get_data        = soup.find(id="__NEXT_DATA__").get_text()
            load_data       = json.loads(get_data)
            
            # Loan into empty List
            try :
                company_address = load_data['props']['initialReduxState']["entities"]["company"][id_company]['address']
                address.append(company_address)
                company_name = load_data['props']['initialReduxState']["entities"]["company"][id_company]['name']
                name.append(company_name)
            except:
                pass
            
    # Make dataframe & dump to excel
    df = pd.DataFrame(list(zip(name,address)),columns=['Company Name','Adress'])
    print(f"df row : {df[df.columns[0]].count()}")
    df.to_excel("glints.xlsx")

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d jam, %02d menit, %02d detik" % (hour, minutes, seconds)

if __name__ == "__main__":
    start = timeit.default_timer()
    scrape_function(int(sys.argv[1]), int(sys.argv[2]))
    stop = timeit.default_timer()
    print(f"Scraping is Done in {convert(stop-start)}")
