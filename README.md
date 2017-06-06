# Github-Trending

demo : [https://trend.pythonanywhere.com/](https://trend.pythonanywhere.com/)


![list view screenshot](/screenshot/list.png)
![detail view screen shot](/screenshot/detail.png)

## Requirements

- Python3


## Usage
### Installation
```bash
$ git clone https://github.com/csbok/github-trending
github-trending$ cd github-trending
github-trending$ pip install -r requirements.txt
github-trending$ cd trend_django
github-trending/trend_django$ python manage.py migrate
```

### Data Crawling
```bash
github-trending$ cd trend_scrapy
github-trending/trend_scrapy$ scrapy crawl trend
```

### Run Server 
```base
github-trending$ cd trend_django
github-trending/trend_django$ python manage.py runserver
```


