import requests
import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from db_func import *


SITE_NAME = 'foodtime.am'
SITE_PROTOCOL = 'http://'


def get_content(url):
    try:
        data = requests.get(url)
        if data.status_code == 200:
            soup = BeautifulSoup(data.text, 'html.parser')
        else:
            print(f"Something went wrong. Status code - {data.status_code}")
            return None
    except requests.ConnectionError:
        sys.exit('Connection failed')
    return soup


def get_full_url(obj):
    return obj['protocol'] + obj['domain'] + obj['path']


def get_page_links(soup):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        o = urlparse(href)
        if o.path:
            flag = False
            if (o.netloc == SITE_NAME or not o.netloc):
                flag = True
                if len(links):
                    if any([data.get('path') == o.path for data in links]):
                            flag = False
                else:
                    flag = True
            if flag:
                links.append({'protocol': SITE_PROTOCOL, 'domain': SITE_NAME, 'path': o.path})
    return links


all_links = []
frontier = []


def get_all_links(link):
    global all_links
    global frontier
    frontier.append(link)
    all_links.append(link)
    with open('main.html', "w") as f:
        f.write(requests.get(get_full_url(link)).text)

    while frontier:
        soup = get_content(get_full_url(frontier[0]))
        if soup is not None:
            page_links = get_page_links(soup)
            for link in page_links:
                if link not in all_links and link not in frontier:
                    if link['path'] == "void(0)":
                        continue
                    print(len(all_links))
                    frontier.append(link)
                    all_links.append(link)
                    with open(f'web_page_{len(all_links) - 1}.html', 'w') as f:
                        f.write(requests.get(get_full_url(link)).text)

            del frontier[0]
        else:
            continue
    print("The End!")
    return None


def main():
    conn = create_connection(DATABASE)
    if conn is not None:
        create_table(conn, sql_create_links_table)

        get_all_links({"protocol": SITE_PROTOCOL, "domain": SITE_NAME, "path": "/"})

        print("Starting DB process")
        for data in all_links:
            link_data = (data.get('path'), data.get('domain'), data.get('protocol'))
            lastrowid = create_link(conn, link_data)
            print(lastrowid)


if __name__ == "__main__":
    main()