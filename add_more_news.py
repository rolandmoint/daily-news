import json

more_news = [
    {
        "title_zh": "美最高法院推翻關稅，全球領袖反應積極",
        "title_en": "Global Leaders React Positively to Supreme Court Tariffs Ruling",
        "summary": "Global leaders and international markets reacted positively after the US Supreme Court ruled that President Trump does not have the authority to enforce sweeping global tariffs. / 在美國最高法院裁定特朗普總統無權實施全面性的全球關稅後，全球領袖和國際市場均作出了積極的反應。",
        "link": "https://eu.usatoday.com/news/world/",
        "source": "USA Today"
    },
    {
        "title_zh": "科學家發現南極冰融化削弱主要碳匯",
        "title_en": "Melting Antarctic Ice May Weaken a Major Carbon Sink",
        "summary": "Researchers found that iron from melting West Antarctic ice is in a form marine life cannot easily use, potentially weakening a major oceanic carbon sink contrary to previous expectations. / 研究人員發現，從西南極冰層融化釋出的鐵份無法被海洋生物輕易利用，這與先前的預期相反，可能會削弱海洋作為主要碳匯的作用。",
        "link": "https://www.sciencedaily.com/",
        "source": "ScienceDaily"
    },
    {
        "title_zh": "蘋果修復iOS和macOS零日漏洞",
        "title_en": "Apple Fixes Exploit for iOS and macOS Zero-Day Vulnerability",
        "summary": "Apple released urgent security updates for iOS and macOS to address a critical zero-day vulnerability that was actively exploited by attackers globally. / 蘋果發布了針對iOS和macOS的緊急安全更新，以修復一個在全球範圍內被攻擊者積極利用的嚴重零日漏洞。",
        "link": "https://thehackernews.com/2026/02/apple-fixes-exploited-zero-day.html",
        "source": "The Hacker News"
    }
]

with open('daily-news/news_data.json', 'r', encoding='utf-8') as f:
    existing_news = json.load(f)

# Combine the new ones too
existing_news = existing_news[:7] + more_news + existing_news[7:] # insert at topish (just need 10 total)

# Let's ensure top 10 are completely fresh items for today: 
# Wait, I am building the final output. The prompt asks me to fetch 10 major global news.
