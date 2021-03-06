from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com/').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('csm_scrape.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary_text','yt_link'])
for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline + '\n')
    summary_text = article.find('div',class_='entry-content').p.text
    print(summary_text + '\n')

    try:
        vid_src = article.find('iframe',class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link + '\n')
    csv_writer.writerow([headline,summary_text,yt_link])
csv_file.close()