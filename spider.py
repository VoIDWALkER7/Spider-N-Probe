import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()

def spider(url,keyword):
    try:
        res = requests.get(url)
    except: 
        print(f"Invalid URL {url}")
        return

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")

        a_tag = soup.find_all("a")

        urls = []
        for tag in a_tag:
            h_ref = tag.get("href")
            if h_ref is not None and h_ref != "":
                urls.append(h_ref)
        #print(urls, "\n")
        
        for link in urls: 
            if link not in visited_urls:
                visited_urls.add(link)
                url_join = urljoin(url, link)
                if keyword in url_join:
                    print(url_join)
                    spider(url_join, keyword)




spider(input("Enter the URL you want to scrape:"),input("Enter the Keyword to search for in the URL provided:"))

