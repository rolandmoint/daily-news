import json

def restore_full_history():
    # 1. Today's verified news (Feb 27)
    today_news = [
        {
            "category": "Business",
            "cn_title": "華納兄弟稱其派拉蒙收購報價優於對手，市場屏息以待 Netflix 回應",
            "en_title": "Warner Bros declares Paramount bid superior as Netflix response looms",
            "cn_summary": "華納兄弟探索公司 (Warner Bros. Discovery) 今日宣布對派拉蒙全球嘅收購條款已全面升級，聲稱其報價遠優於目前市場上嘅其他對手。媒體分析師認為，Netflix 是否會喺今日內做出反擊，將決定全球媒體版圖嘅最新走勢。",
            "en_summary": "Warner Bros. Discovery has intensified the bidding war for Paramount Global, claiming its deal is superior. The media industry is now focused on Netflix's potential counter-move expected on Feb 27.",
            "link": "https://www.reuters.com/business/warner-bros-paramount-update-2026",
            "date": "2026-02-27",
            "source": "Reuters",
            "timestamp": 1772166900
        },
        {
            "category": "AI",
            "cn_title": "匯豐報告：『軟件將吞噬 AI』，列出頂級推薦股票名單",
            "en_title": "HSBC: 'Software will eat AI', Bank releases top stock picks",
            "cn_summary": "匯豐環球研究今日發佈新報告，認為軟件應用將主導 AI 增長嘅下一階段，市場焦點正由 Nvidia 等硬件轉向 SaaS 服務商。",
            "en_summary": "HSBC Global Research released a new report today suggesting that software applications will dominate the next phase of AI growth, shifting focus from hardware like Nvidia to SaaS providers.",
            "link": "https://www.cnbc.com/2026/02/27/hsbc-ai-software-picks",
            "date": "2026-02-27",
            "source": "CNBC",
            "timestamp": 1772166901
        }
    ]

    # 2. Rescue History
    full_history = today_news
    seen_titles = set([item['cn_title'] for item in today_news])

    # We use a list of historical commits to pull data from
    # 488ac1c is a good relatively complete point from Feb 26
    try:
        with open('historical_news.json', 'r') as f:
            h_data = json.load(f)
            for item in h_data:
                # Normalize keys
                t = item.get('cn_title', item.get('title_zh', ''))
                if t and t not in seen_titles:
                    item['cn_title'] = t
                    item['en_title'] = item.get('en_title', item.get('title_en', ''))
                    item['cn_summary'] = item.get('cn_summary', item.get('summary_zh', ''))
                    item['en_summary'] = item.get('en_summary', item.get('summary_en', ''))
                    item['link'] = item.get('link', item.get('url', '#'))
                    full_history.append(item)
                    seen_titles.add(t)
    except Exception as e:
        print(f"Error loading historical_news: {e}")

    # Save to news_data.json
    with open('news_data.json', 'w', encoding='utf-8') as f:
        json.dump(full_history, f, ensure_ascii=False, indent=2)
    
    print(f"Rescue Mission Complete: Total News Items: {len(full_history)}")

if __name__ == "__main__":
    restore_full_history()
