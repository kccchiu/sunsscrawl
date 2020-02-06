# Crawler for gun violence in Chicago Suns Times News
The project contains 2 crawler. One for text and one for images.
Text crawler store the results in a json file, and the image crawler store the downloaded images in a folder called news_image.

To respect the server, both crawler have settings that slow down the scraping process. If you want to test the crawler, enter a small page number when you start the crawler.

#### Prereq / Dependencies
1. Python 3.7
2. install Scrapy in your virtual environment via terminal/command prompt.
```
pip install scrapy
```

### Running the crawler
There are 2 crawler in this project. One for scraping text/article, and one for scraping images.

Make sure the news_image folder is empty and the desired .json file name is not present in the project.
Navigate to sunsscrawl/sunscrawl/settings.py and set your absolute on the line with IMAGES_STORE =
In my case is
##### IMAGES_STORE = r'C:\PyProjects\sunsscrawl\news_image'

Run the following command:
```
scrapy crawl images & scrapy crawl news -o scraped_news.json
```
Then entered the desired number of pages to scrape.

### Bug: You have to enter the number multiple times. (Total 4 times)



#### Text Crawler
To run the text crawler and store the results in a json file, run the following command (scraped results will concat onto the json file that has the same file name) :
```
scrapy crawl news -o my_scraped_results.json
```


#### Image Crawler
To run the images crawler and download the images, first make sure the news_image folder is empty, and run the following command:
```
scrapy crawl images
```
