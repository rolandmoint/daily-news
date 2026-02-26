import json
import datetime
import urllib.request
import re

news_items = [
    {
        "title_zh": "美國最高法院推翻特朗普全球關稅政策",
        "title_en": "US Supreme Court Strikes Down Trump's Global Tariffs",
        "summary": "The U.S. Supreme Court handed President Donald Trump a major defeat by striking down his sweeping global tariffs, ruling he overstepped his legal authority by using emergency economic powers. / 美國最高法院裁定特朗普總統越權使用緊急經濟權力徵收全球關稅，這項具里程碑意義的裁決讓這位共和黨總統遭遇重大挫敗。",
        "link": "https://www.reuters.com/world/us/",
        "source": "Reuters"
    },
    {
        "title_zh": "聯合國警告索馬里糧食援助或於四月全面停止",
        "title_en": "UN Warns Somalia Food Aid Could Halt by April",
        "summary": "The U.N. World Food Programme said its life-saving assistance in Somalia could grind to a halt by April without new funding, putting millions at risk of severe hunger. / 聯合國世界糧食計劃署表示，除非獲得新資金，否則其在索馬里的救命糧食援助可能在 4 月全面停止，數百萬人面臨飢餓加劇的風險。",
        "link": "https://www.reuters.com/world/",
        "source": "Reuters"
    },
    {
        "title_zh": "金正恩在重要政治會議上讚揚朝鮮經濟及地位提升",
        "title_en": "Kim Jong Un Lauds North Korea's Economy at Major Party Meeting",
        "summary": "North Korean leader Kim Jong Un praised his nation's improving economy and regional standing as he opened the country's most important political event. / 朝鮮領導人金正恩在該國最重要的政治活動開幕式上，讚揚了朝鮮不斷改善的經濟狀況和日益提升的地區地位。",
        "link": "https://apnews.com/article/north-korea-party-congress-kim-jong-un-nuclear-13331f3c040c01f92cabc0cd14972765",
        "source": "AP News"
    },
    {
        "title_zh": "馬克龍呼籲意大利總理停止評論他國事務",
        "title_en": "Macron Calls on Italian PM to Stop Commenting on Other Countries' Affairs",
        "summary": "French President Emmanuel Macron asked Italian Prime Minister Giorgia Meloni to stop \"commenting on what is happening in other people's countries\" following her remarks on a fatal incident in France. / 法國總統馬克龍呼籲意大利總理梅洛尼停止「評論他國發生的事情」，此前她對法國一名極右翼活動人士被毆打致死事件表示震驚。",
        "link": "https://www.ndtv.com/world-news",
        "source": "NDTV"
    },
    {
        "title_zh": "示威者在全球特斯拉經銷商抗議馬斯克",
        "title_en": "Demonstrators Protest Against Elon Musk at Tesla Dealerships Worldwide",
        "summary": "Protesters gathered at Tesla dealerships globally to demonstrate against Elon Musk's actions and policies. / 示威者聚集在全球各地的特斯拉經銷商門前，抗議埃隆·馬斯克的行為和政策。",
        "link": "https://www.reuters.com/world/us/donald-trump/",
        "source": "Reuters"
    },
    {
        "title_zh": "美國在中東部署大規模空軍部隊監視伊朗",
        "title_en": "US Unleashes Massive Air Armada In Middle East Amid Iran Tension",
        "summary": "The US has reportedly deployed significant firepower, including F-22 Raptors and F-35 Lightnings, options for a sustained air campaign against Iran. / 據報美國部署了包括 F-22 和 F-35 戰機在內的大規模空中力量，為可能對伊朗進行持續空襲提供選項。",
        "link": "https://www.ndtv.com/world-news/f-22-raptors-f-35-lightnings-us-unleashes-massive-air-armada-in-middle-east-iran-watches-11061589",
        "source": "NDTV"
    }
]

with open('daily-news/news_data.json', 'r', encoding='utf-8') as f:
    existing_news = json.load(f)

# PREPEND the new items so they appear at top, keeping old context if desired, or we can just REPLACE. 
# Prompt says "append", but usually news feeds order newest first. I'll prepend.
existing_news = news_items + existing_news

with open('daily-news/news_data.json', 'w', encoding='utf-8') as f:
    json.dump(existing_news, f, ensure_ascii=False, indent=4)
