import json
import time
from datetime import datetime

new_news = [
    {
        "category": "World",
        "cn_title": "巴基斯坦俾路支省反恐行動結束",
        "en_title": "Counter-terrorism Operations in Balochistan, Pakistan Conclude",
        "cn_summary": "巴基斯坦軍方宣佈結束在俾路支省為期 40 小時的反恐行動，共擊斃 145 名俾路支解放軍 (BLA) 武裝份子，行動中另有 18 名平民及 18 名安全人員喪生。",
        "en_summary": "Pakistani military forces concluded a 40-hour counter-terrorism operation in Balochistan, resulting in the deaths of 145 Baloch Liberation Army (BLA) insurgents, 18 civilians, and 18 security personnel.",
        "link": "https://apnews.com/article/pakistan-insurgency-balochistan-deadly-attacks-militants-killed-51af1ee3b96f6fac5d2abfa21a607ad8",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "俄羅斯無人機襲擊烏克蘭第聶伯羅",
        "en_title": "Russian Drone Strike Hits Dnipro, Ukraine",
        "cn_summary": "一架俄羅斯無人機擊中第聶伯羅一輛載有礦工的巴士，造成至少 15 人死亡， 7 人受傷。",
        "en_summary": "A Russian drone strike hit a minibus transporting mineworkers in Dnipro, Ukraine, killing at least 15 people and injuring seven others.",
        "link": "https://www.bbc.co.uk/news/articles/cdre7g2je63o",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "美國對全球徵收 10% 關稅首週情況",
        "en_title": "First Week of Trump's 10% Global Tariffs",
        "cn_summary": "特朗普政府的新 10% 全球關稅於 2 月 24 日生效。美國最高法院雖一度對此提出質疑，但總統誓言將透過其他手段維持大部分關稅。",
        "en_summary": "The Trump administration's new 10% global tariffs kicked in on Feb 24. Despite legal challenges, the administration pledges to maintain them via other means.",
        "link": "https://www.cnn.com/us/live-news/trump-administration-tariffs-iran-news-02-21-26",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "美伊日內瓦談判取得進展但軍事緊張持續",
        "en_title": "Progress in US-Iran Talks Amid Military Buildup",
        "cn_summary": "美國與伊朗代表在瑞士日內瓦的談判傳出進展，但美軍仍持續向中東增兵並擊落接近航母的無人機。",
        "en_summary": "Progress was reported in negotiations between US and Iranian officials in Geneva, even as the US military continues its buildup and downs drones near carriers.",
        "link": "https://www.npr.org/2026/02/20/nx-s1-5721117/the-news-roundup-for-february-20-2026",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "利比亞領導人之子賽義夫·卡扎菲遇刺",
        "en_title": "Assassination of Saif al-Islam Gaddafi in Libya",
        "cn_summary": "利比亞前領導人卡扎菲之子、總統候選人賽義夫·卡扎菲在津坦住處外遇刺身亡。",
        "en_summary": "Saif al-Islam Gaddafi, son of Libya's former leader and a presidential candidate, was assassinated outside his home in Zintan, Libya.",
        "link": "https://english.alarabiya.net/News/north-africa/2026/02/03/saif-alislam-gaddafi-has-been-killed-gaddafi-family-source-tells-al-arabiya",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "哥斯達黎加選出新任女總統",
        "en_title": "Costa Rica Elects Laura Fernández as President",
        "cn_summary": "主權人民黨的勞拉·費爾南德斯以 48% 的選票贏得哥斯達黎加總統大選。",
        "en_summary": "Laura Fernández of the Sovereign People's Party (PPSO) won the Costa Rican presidency with 48% of the vote.",
        "link": "https://www.bbc.com/news/articles/cdre7me407yo",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "巴基斯坦伊斯蘭堡清真寺自殺式襲擊",
        "en_title": "Suicide Bombing at Mosque in Islamabad, Pakistan",
        "cn_summary": "伊斯蘭堡一座什葉派清真寺遭到自殺式爆彈襲擊，造成 32 人死亡，170 人受傷。「伊斯蘭國」宣稱負責。",
        "en_summary": "A suicide bombing at a Shia mosque in Islamabad killed 32 people and wounded 170 others. ISIS claimed responsibility.",
        "link": "https://www.aljazeera.com/news/2026/2/7/thousands-mourn-32-victims-of-islamabad-shia-mosque-bombing-in-pakistan",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "星鏈停用在烏克蘭俄佔區的终端",
        "en_title": "SpaceX Deactivates Starlink in Russian-Occupied Ukraine",
        "cn_summary": "在烏克蘭壓力下，SpaceX 已停用俄佔區內的星鏈終端，以防止俄羅斯軍隊利用該網路。",
        "en_summary": "SpaceX has deactivated Starlink terminals in Russian-occupied territories of Ukraine to prevent their use by Russian forces.",
        "link": "https://www.reuters.com/world/europe/starlink-used-by-russian-forces-deactivated-battlefield-ukraine-says-2026-02-05/",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "《華盛頓郵報》重組裁員 300 人",
        "en_title": "Washington Post Lays Off 300 Journalists",
        "cn_summary": "作為重組的一部分，《華盛頓郵報》宣佈裁員約三分之一的員工，主要影響體育及國際新聞部門。",
        "en_summary": "The Washington Post announced layoffs for about 300 journalists, representing one-third of its staff, as part of a restructuring.",
        "link": "https://www.bbc.co.uk/news/articles/cwyn05d1494o",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    },
    {
        "category": "World",
        "cn_title": "日本開始鑽探深海稀土礦以減少對華依賴",
        "en_title": "Japan Drills for Rare Earth Minerals to Rival China",
        "cn_summary": "日本成功從南鳥島附近提取含稀土沉積物，旨在減少工業對中方關鍵礦產的依賴。",
        "en_summary": "Japan has begun retrieving deep-sea sediment containing rare earth minerals near Minamitorishima to reduce its reliance on China.",
        "link": "https://www.asahi.com/ajw/articles/16327883",
        "date": "2026-02-26",
        "timestamp": int(time.time())
    }
]

file_path = 'temp_repo/news_data.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sort new news to the top
combined_data = new_news + data
# Limit to reasonable amount if needed, or keep all
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=2)
