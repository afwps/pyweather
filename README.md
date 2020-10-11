# pyweather

A rudimentary CLI weather scraper made with bs4, requests and pandas

## Informations
- Target: [Forecast Weather](https://www.weather.gov/)
- URL Pattern: `'<url>/<page>/<lat>=><value>&<lon>=<value>'`
  - An URL can be passed anually, such as `scrape(url), where `url` is treated as a **string**
  - You can store multiples URLs using **lists**, such as:
  ```python
  urls = ['url', 'url', 'url', ...]
  ```
  *as a **dictionary (Recommended):***
  ```python
  urls = {
    'target_city': 'url',
    'target_city': 'url',
    'target_city': 'url',
    ...
  }
  ```
- Data is stored inside **`results`** variable and can be converted into a `CSV file`
  
## Loop through URLs

```python
  # Loop through `urls` list
  for url in urls:
    scrape(url)
    
    
  # Looping through `urls` dictionary
  for url in urls:
    scrape(urls[url])
```

## Example
```python
  url = 'https://forecast.weather.gov/MapClick.php?lat=45.511790000000076&lon=-122.67562999999996'
  
  scrape(url)
```

## Requirement(s)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://fr.python-requests.org/en/latest/)
- [Pandas](https://pandas.pydata.org/docs/index.html)
