import requests
from bs4 import BeautifulSoup
import csv
import time

categories = [
    {'url': 'https://vnexpress.net/thoi-su', 'label': 'thoi_su'},
    {'url': 'https://vnexpress.net/the-thao', 'label': 'the_thao'},
    {'url': 'https://vnexpress.net/giao-duc', 'label': 'giao_duc'},
    {'url': 'https://vnexpress.net/kinh-doanh', 'label': 'kinh_doanh'},
    {'url': 'https://vnexpress.net/goc-nhin', 'label': 'goc_nhin'},
    {'url': 'https://vnexpress.net/the-gioi', 'label': 'the_gioi'},
    {'url': 'https://vnexpress.net/bat-dong-san', 'label': 'bat_dong_san'},
    {'url': 'https://vnexpress.net/khoa-hoc', 'label': 'khoa_hoc'},
    {'url': 'https://vnexpress.net/giai-tri', 'label': 'giai_tri'},
    {'url': 'https://vnexpress.net/phap-luat', 'label': 'phap_luat'},
    {'url': 'https://vnexpress.net/du-lich', 'label': 'du_lich'},
    {'url': 'https://vnexpress.net/so-hoa', 'label': 'so_hoa'},
    {'url': 'https://vnexpress.net/oto-xe-may', 'label': 'xe'},
    {'url': 'https://vnexpress.net/suc-khoe', 'label': 'suc_khoe'},
]

# page 1 - 9
page1_9_categories = []
for category in categories:
    url = category['url']
    page1_9_categories.append(category)
    page1_9_categories.append({'url': f'{url}-p2', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p3', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p4', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p5', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p6', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p7', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p8', 'label': category['label']})
    page1_9_categories.append({'url': f'{url}-p9', 'label': category['label']})

# creat data file and add name column
with open('./data/vnexpress_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['label', 'title', 'abstract', 'content', 'author', 'date'])

# start time to crawl data
start_time = time.time()

# open data file and add data
with open('./data/vnexpress_data.csv', 'a+', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for category in page1_9_categories:
        category_url = category['url']
        category_label = category['label']

        # take data
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # all news
        titles = soup.findAll('h3', class_='title-news')

        # get all the articles
        for title in titles:
            link = title.find('a').attrs["href"]
            news = requests.get(link)
            soup = BeautifulSoup(news.content, "html.parser")

            title_detail = soup.find('h1', class_='title-detail')
            abstract = soup.find('p', class_="description")

            # get authors
            authors = soup.findAll('strong') if soup.find('strong') else ''
            if authors != '':
                author = authors[-1].get_text()
            else: author = authors
            
            # get date
            date_span = soup.find('span', class_='date')
            if date_span:
                date = date_span.get_text(strip=True).split(',')[1].strip()
            else: date=''
            
            if title_detail and abstract:
                # get title and abstract
                title_text = title_detail.text.strip()
                abstract_text = abstract.text.strip()

                # get content
                paragraphs = soup.find_all('p', class_='Normal')
                content = '\n'.join(p.text.strip() for p in paragraphs)
                
                if not category_label or not title_text or not abstract_text or not content: continue
                
                # write data to CSV with corresponding labels
                csv_writer.writerow([category_label, title_text, abstract_text, content, author, date])
                print(f'+ 1 {category_label}: {title_text} - Tác giả: {author}')

# end time to crawl data                
crawl_time = (time.time()-start_time)/60

print("Done!")
print(f"Crawl time: {round(crawl_time)} minutes.")  # Crawl time: 42 minutes.