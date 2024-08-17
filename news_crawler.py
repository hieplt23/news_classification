import requests
from bs4 import BeautifulSoup
import csv
import time

# Define the categories and their URLs to scrape
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

# Generate URLs for the first 9 pages of each category
page1_9_categories = []
for category in categories:
    url = category['url']
    page1_9_categories.append(category)
    for page_num in range(2, 10):
        page1_9_categories.append({'url': f'{url}-p{page_num}', 'label': category['label']})

# Create the CSV file and write the header
with open('./data/vnexpress_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['label', 'title', 'abstract', 'content', 'author', 'date'])

# Record the start time of the data scraping
start_time = time.time()

# Open the CSV file to append data
with open('./data/vnexpress_data.csv', 'a+', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Iterate through each category and page
    for category in page1_9_categories:
        category_url = category['url']
        category_label = category['label']

        # Fetch the content of the category page
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all news articles on the page
        titles = soup.findAll('h3', class_='title-news')

        # Extract details for each article
        for title in titles:
            link = title.find('a').attrs["href"]
            news = requests.get(link)
            soup = BeautifulSoup(news.content, "html.parser")

            # Get the title and abstract of the article
            title_detail = soup.find('h1', class_='title-detail')
            abstract = soup.find('p', class_="description")

            # Extract author information
            authors = soup.findAll('strong') if soup.find('strong') else ''
            author = authors[-1].get_text() if authors else ''
            
            # Extract the publication date
            date_span = soup.find('span', class_='date')
            date = date_span.get_text(strip=True).split(',')[1].strip() if date_span else ''
            
            if title_detail and abstract:
                title_text = title_detail.text.strip()
                abstract_text = abstract.text.strip()

                # Extract the content of the article
                paragraphs = soup.find_all('p', class_='Normal')
                content = '\n'.join(p.text.strip() for p in paragraphs)
                
                # Skip if any essential information is missing
                if not category_label or not title_text or not abstract_text or not content:
                    continue
                
                # Write the extracted data to the CSV file
                csv_writer.writerow([category_label, title_text, abstract_text, content, author, date])
                print(f'+ 1 {category_label}: {title_text} - Author: {author}')

# Calculate and display the total crawl time
crawl_time = (time.time() - start_time) / 60
print("Done!")
print(f"Crawl time: {round(crawl_time)} minutes.")  # Example output: Crawl time: 42 minutes.
