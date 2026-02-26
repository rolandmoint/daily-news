import json
import os

new_entries = [
    {
        "category": "AI",
        "cn_title": "法官暫時駁回 xAI 對競爭對手 OpenAI 的商業秘密賠償訴訟",
        "en_title": "Judge Dismisses xAI Trade-Secrets Suit Against Rival OpenAI",
        "cn_summary": "舊金山聯邦法官駁回了 Elon Musk 旗下 xAI 對 OpenAI 的訴訟，裁定其目前未能具體證明 OpenAI 存在不當行為，但允許 xAI 在完善指控後重新起訴。",
        "en_summary": "A U.S. District Judge in San Francisco dismissed a lawsuit filed by Elon Musk's xAI against OpenAI, ruling that it failed to demonstrate specific misconduct, though xAI is permitted to refile its claims.",
        "date": "2026-02-25",
        "link": "https://www.claimsjournal.com/news/national/2026/02/25/335899.htm",
        "timestamp": 1772001000
    },
    {
        "category": "AI",
        "cn_title": "OpenAI 調整支出預期：2030 年算力投入目標約為 6000 億美元",
        "en_title": "OpenAI Resets Spending Expectations:  Billion by 2030",
        "cn_summary": "OpenAI 向投資者明確了其算力規劃，預計到 2030 年的總算力支出約為 6000 億美元，此前曾有報導稱其目標高達 1.4 萬億美元。",
        "en_summary": "OpenAI has signaled a shift in its long-term financial planning, clarifying that it targets roughly  billion in total compute spend by 2030, a reduction from earlier trillion-dollar projections.",
        "date": "2026-02-25",
        "link": "https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html",
        "timestamp": 1772001000
    },
    {
        "category": "Fintech",
        "cn_title": "2026 福布斯金融科技 50 強：Polymarket 與 Hyperliquid 榜上有名",
        "en_title": "Forbes Fintech 50 2026: Polymarket and Hyperliquid Make the List",
        "cn_summary": "2026 年福布斯金融科技 50 強名單發佈，包括 Polymarket 和 Hyperliquid 在內的市場平台因其在數字金融領域的領先地位而入選。",
        "en_summary": "The prestigious Forbes Fintech 50 for 2026 has been released, highlighting market platforms like Polymarket and Hyperliquid as leaders in the current digital financial landscape.",
        "date": "2026-02-25",
        "link": "https://www.weex.com/news/detail/polymarket-hyperliquid-and-others-make-the-2026-forbes-fintech-50-346563",
        "timestamp": 1772001000
    },
    {
        "category": "AI",
        "cn_title": "OpenAI 深化與諮詢巨頭合作，推動企業級 AI 應用",
        "en_title": "OpenAI Deepens Partnerships with Consulting Giants for Enterprise AI",
        "cn_summary": "OpenAI 與 BCG、麥肯錫、埃森哲及凱捷諮詢等巨頭建立「前沿聯盟」(Frontier Alliance)，旨在協助企業將 AI 項目從初步試點推向全面部署。",
        "en_summary": "OpenAI launched the \"Frontier Alliance\" with BCG, McKinsey, Accenture, and Capgemini to help enterprises move AI projects from limited pilots to full-scale deployment.",
        "date": "2026-02-25",
        "link": "https://www.reuters.com/business/openai-deepens-partnerships-with-consulting-giants-push-enterprise-ai-beyond-2026-02-23/",
        "timestamp": 1772001000
    },
    {
        "category": "Fintech/AI",
        "cn_title": "Greenlite AI 更名為 Bretton AI 並完成 7500 萬美元 B 輪融資",
        "en_title": "Greenlite AI Rebrands as Bretton AI, Secures m Series B",
        "cn_summary": "金融科技初創公司 Greenlite AI 在完成 7500 萬美元 B 輪融資後正式更名為 Bretton AI，專注於提供 AI 原生合規解決方案。",
        "en_summary": "Fintech startup Greenlite AI has officially rebranded to Bretton AI following a successful  million Series B funding round, focusing on AI-native compliance solutions.",
        "date": "2026-02-25",
        "link": "https://www.fintechfutures.com/fintech",
        "timestamp": 1772001000
    }
]

file_path = 'temp_news_repo/news_data.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Prepend new entries to keep it sorted by latest
data = new_entries + data

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully updated news_data.json")
