import requests
import re
import urllib.parse as urlparse

target_url = input('Enter the target url: ')
print('Crawling started')
print('-'*50)
target_links = []

def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))

def crawl(url):
        href_links = extract_links(url)
        for links in href_links:
            link = urlparse.urljoin(url, links)

            if '#' in link:
                link = link.split('#')[0]

            if target_url in link not in target_links:
                target_links.append(link)
                print(link)
                crawl(link)
    
try:
    crawl(target_url)
except KeyboardInterrupt:
    print('Crawling stopped')