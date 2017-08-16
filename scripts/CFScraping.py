import cfscrape

request_flare = cfscrape.create_scraper()
re = request_flare.get("https://www.mapbox.com/")
print(re.text)