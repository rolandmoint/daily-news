import json

extra = [
    {
        "title_zh": "國際奧林匹克委員會主席會見美國官員",
        "title_en": "IOC President Addresses 'Board of Peace' Meeting",
        "summary": "International Olympic Committee President Kirsty Coventry addressed the first meeting of The Board of Peace along with US officials and other global sporting leaders. / 國際奧林匹克委員會主席 Kirsty Coventry 與美國官員及其他全球體育領袖一起出席並在首屆「和平委員會」會議上致辭。",
        "link": "https://www.reuters.com/world/",
        "source": "Reuters"
    }
]

with open('daily-news/news_data.json', 'r', encoding='utf-8') as f:
    existing_news = json.load(f)

# The total number of recently added news is 6 + 3 + 1 = 10 items.
existing_news = existing_news[:9] + extra + existing_news[9:]

with open('daily-news/news_data.json', 'w', encoding='utf-8') as f:
    json.dump(existing_news, f, ensure_ascii=False, indent=4)
