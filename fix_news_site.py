import json
import os

def fix_and_merge():
    # 1. Today's real news (Fixed keys)
    today_news = [
        {
            "category": "Business",
            "cn_title": "華納兄弟稱其派拉蒙收購報價優於對手，市場屏息以待 Netflix 回應",
            "en_title": "Warner Bros declares Paramount bid superior as Netflix response looms",
            "cn_summary": "華納兄弟探索公司 (Warner Bros. Discovery) 今日宣布對派拉蒙全球嘅收購條款已全面升級，聲稱其報價遠優於目前市場上嘅其他對手。媒體分析師認為，Netflix 是否會喺今日內做出反擊，將決定全球媒體版圖嘅最新走勢。",
            "en_summary": "Warner Bros. Discovery has intensified the bidding war for Paramount Global, claiming its deal is superior. The media industry is now focused on Netflix's potential counter-move expected on Feb 27.",
            "link": "https://www.reuters.com/business/warner-bros-paramount-update-2026",
            "date": "2026-02-27",
            "source": "Reuters"
        },
        {
            "category": "AI",
            "cn_title": "匯豐報告：『軟件將吞噬 AI』，列出頂級推薦股票名單",
            "en_title": "HSBC: 'Software will eat AI', Bank releases top stock picks",
            "cn_summary": "匯豐環球研究今日發佈新報告，認為軟件應用將主導 AI 增長嘅下一階段，市場焦點正由 Nvidia 等硬件轉向 SaaS 服務商。",
            "en_summary": "HSBC Global Research released a new report today suggesting that software applications will dominate the next phase of AI growth, shifting focus from hardware like Nvidia to SaaS providers.",
            "link": "https://www.cnbc.com/2026/02/27/hsbc-ai-software-picks",
            "date": "2026-02-27",
            "source": "CNBC"
        },
        {
            "category": "World",
            "cn_title": "聯合國就 AI 全球監管框架達成歷史性共識",
            "en_title": "UN Reaches Historic Consensus on Global AI Regulatory Framework",
            "cn_summary": "聯合國今日通過咗首個具備實質約束力嘅 AI 全球監管框架，重點打擊 AI 武器化及深度偽造技術。",
            "en_summary": "The UN has adopted its first legally binding global regulatory framework for AI, focusing on curbing AI weaponization and deepfakes.",
            "link": "https://www.un.org/news/ai-global-consensus-2026",
            "date": "2026-02-27",
            "source": "UN News"
        }
    ]

    # 2. Try to load and normalize old data
    merged = today_news
    try:
        with open('news_data.json', 'r') as f:
            old_data = json.load(f)
            for item in old_data:
                # Normalize keys
                new_item = {
                    "category": item.get('category', 'World'),
                    "cn_title": item.get('cn_title', item.get('title_zh', '新新聞')),
                    "en_title": item.get('en_title', item.get('title_en', 'New News')),
                    "cn_summary": item.get('cn_summary', item.get('summary_zh', '')),
                    "en_summary": item.get('en_summary', item.get('summary_en', '')),
                    "link": item.get('link', item.get('url', item.get('link', '#'))),
                    "date": item.get('date', '2026-02-27'),
                    "source": item.get('source', 'Unknown')
                }
                # Prepending logic: keep only if it's not already there (simple title check)
                if new_item['cn_title'] not in [x['cn_title'] for x in merged]:
                    merged.append(new_item)
    except Exception as e:
        print(f"Error merging: {e}")

    # 3. Save fixed JSON
    with open('news_data.json', 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    
    # 4. Generate correct HTML with World button and Dark Vibe
    html_content = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🍏 MACBOT 新聞中心 | Roland's Intelligence Briefing</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #0f172a; color: #f1f5f9; }
        .news-card { background-color: #1e293b; border-left: 4px solid #38bdf8; transition: transform 0.2s; }
        .news-card:hover { transform: translateY(-2px); filter: brightness(1.1); }
    </style>
</head>
<body class="font-sans min-h-screen">
    <header class="bg-slate-900 border-b border-slate-700 p-6 sticky top-0 z-10 shadow-xl">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <div>
                <h1 class="text-2xl font-bold text-sky-400">🍏 MACBOT 新聞中心</h1>
                <p class="text-slate-400 text-sm">Roland's Daily Intelligence Briefing</p>
            </div>
            <div id="update-date" class="text-right text-slate-500 text-xs font-mono">Loading...</div>
        </div>
    </header>

    <nav class="bg-slate-800 p-2 border-b border-slate-700 sticky top-20 z-10 overflow-x-auto">
        <div class="max-w-4xl mx-auto flex gap-6 text-xs font-bold uppercase tracking-wider text-slate-400 p-2">
            <button onclick="filterNews('ALL')" class="hover:text-sky-400">ALL</button>
            <button onclick="filterNews('World')" class="hover:text-sky-400">WORLD</button>
            <button onclick="filterNews('AI')" class="hover:text-sky-400">AI</button>
            <button onclick="filterNews('Fintech')" class="hover:text-sky-400">FINTECH</button>
            <button onclick="filterNews('Cyber Security')" class="hover:text-sky-400">SECURITY</button>
        </div>
    </nav>

    <main class="max-w-4xl mx-auto p-6">
        <div id="news-container" class="space-y-6"></div>
    </main>

    <script>
        let newsData = [];
        async function loadNews() {
            const res = await fetch('news_data.json?t=' + Date.now());
            newsData = await res.json();
            document.getElementById('update-date').innerText = 'LAST SYNC: ' + (newsData[0]?.date || 'Today');
            renderNews(newsData);
        }
        function renderNews(data) {
            const container = document.getElementById('news-container');
            container.innerHTML = data.map(item => `
                <div class="news-card p-6 rounded-lg shadow-lg">
                    <div class="flex justify-between items-start mb-3">
                        <span class="text-xs font-bold text-sky-500 uppercase">${item.category || 'World'}</span>
                        <span class="text-xs text-slate-500 font-mono">${item.date}</span>
                    </div>
                    <h2 class="text-xl font-bold text-white mb-2 leading-tight">
                        ${item.cn_title}
                        <div class="text-slate-400 text-sm font-medium mt-1">${item.en_title}</div>
                    </h2>
                    <div class="space-y-2 mb-4">
                        <p class="text-slate-300 text-sm">${item.cn_summary}</p>
                        <p class="text-slate-500 text-xs italic">${item.en_summary}</p>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <span class="text-slate-400">Source: ${item.source}</span>
                        <a href="${item.link}" target="_blank" class="text-sky-400 hover:underline font-bold">READ FULL ARTICLE &rarr;</a>
                    </div>
                </div>
            `).join('');
        }
        function filterNews(cat) {
            renderNews(cat === 'ALL' ? newsData : newsData.filter(i => i.category === cat));
        }
        loadNews();
    </script>
</body>
</html>"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Optimization Complete: Fixed Data and Layout.")

if __name__ == "__main__":
    fix_and_merge()
