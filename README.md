
# Read Me

Glints scraping is scraper that aims data from Glints to xlsx, this scraper works in about 1 - 2 mins / page depends on the internet & driver.


## Deployment

To deploy this you will need :

[chromewebdriver](https://chromedriver.chromium.org/downloads)



## Run Locally

Clone the project

```bash
  git clone https://github.com/haydarmiezanie/glints_scraping.git
```

Install dependencies

```bash
  pip install selenium
  pip install pandas
  pip install beautifulsoup
```

Start the scraper

```bash
  python -m glints_scraping [start_page] [end_page]
```
Example :

```bash
  python -m glints_scraping 1 36
```
## Scraper Flow

![image](https://user-images.githubusercontent.com/39428898/202619482-35766f8a-e361-48ee-ae37-e990a2b833e0.png)



## Limitation

This scraper is only example how to scrape data from some website. This method work's very slow. We need to find API if we want to get the data faster.

## Authors

- [Haydar Miezanie](https://github.com/haydarmiezanie)

