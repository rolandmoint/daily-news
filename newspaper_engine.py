import json
import os
from datetime import datetime, timedelta

DATA_FILE = 'news_data.json'
HTML_FILE = 'index.html'

def update_news(news_list):
    # news_list should be a list of dicts: {"category": "...", "en_title": "...", "cn_title": "...", ...}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    for entry in news_list:
        entry["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry["timestamp"] = datetime.now().timestamp()
        data.insert(0, entry)

    # 1. 唯一性檢查 (基於連結)
    seen_links = set()
    unique_data = []
    for item in data:
        if item['link'] not in seen_links:
            unique_data.append(item)
            seen_links.add(item['link'])
    
    # 2. 移除超過 7 天
    seven_days_ago = (datetime.now() - timedelta(days=7)).timestamp()
    unique_data = [item for item in unique_data if item.get('timestamp', 0) > seven_days_ago]

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=2)

    render_html(unique_data)

def render_html(data):
    html_template = """
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Roland's Daily Intelligence</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #f1f5f9; font-family: 'Inter', sans-serif; }
            .feed-card { border-left: 4px solid transparent; transition: all 0.2s; }
            .category-world { border-left-color: #3b82f6; }
            .category-ai { border-left-color: #10b981; }
            .category-sec { border-left-color: #ef4444; }
        </style>
    </head>
    <body class="p-4 md:p-12">
        <header class="max-w-4xl mx-auto mb-16 text-center">
            <h1 class="text-5xl font-black text-slate-900 tracking-tight mb-4">RW 智能簡報</h1>
            <p class="text-xl text-slate-500 font-medium">為 Roland 提供的每日自動新聞追蹤 • 僅保留最近 7 天</p>
            <div class="mt-6 flex justify-center gap-4">
                <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold uppercase">World</span>
                <span class="px-3 py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs font-bold uppercase">AI / Fintech</span>
                <span class="px-3 py-1 bg-red-100 text-red-700 rounded-full text-xs font-bold uppercase">Cyber Security</span>
            </div>
        </header>

        <main class="max-w-4xl mx-auto space-y-8">
            {%CONTENT%}
        </main>

        <footer class="max-w-4xl mx-auto mt-24 py-12 border-t border-slate-200 text-center text-slate-400 text-sm">
            &copy; 2026 Designed & Handled by RW AI Assistant. Updated via GitHub Actions.
        </footer>
    </body>
    </html>
    """
    
    content_html = ""
    for item in data:
        cat_class = "category-world"
        cat_name = "🌏 世界重點"
        if "AI" in item['category']: 
            cat_class = "category-ai"
            cat_name = "🤖 AI & Fintech"
        elif "Cyber" in item['category']: 
            cat_class = "category-sec"
            cat_name = "🛡️ 網絡安全"

        content_html += f"""
        <article class="bg-white p-8 rounded-2xl shadow-sm border border-slate-100 feed-card {cat_class}">
            <div class="flex justify-between items-center mb-4">
                <span class="text-sm font-bold uppercase tracking-wider text-slate-400">{item['date']}</span>
                <span class="px-2 py-1 bg-slate-100 text-slate-600 rounded text-[10px] font-black uppercase">{cat_name}</span>
            </div>
            <h3 class="text-xl font-black text-slate-800 leading-tight mb-2">{item['en_title']}</h3>
            <h3 class="text-xl font-bold text-slate-700 leading-tight mb-6">{item['cn_title']}</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-600 text-sm leading-relaxed mb-6">
                <div>{item['en_summary']}</div>
                <div class="text-slate-500 border-l border-slate-100 pl-6 italic">{item['cn_summary']}</div>
            </div>
            <div class="flex justify-between items-center pt-4 border-t border-slate-50">
                <span class="text-xs text-slate-400 font-medium">Source: {item['source']}</span>
                <a href="{item['link']}" target="_blank" class="text-slate-900 font-bold hover:underline">Read Full Article &rarr;</a>
            </div>
        </article>
        """
    
    final_html = html_template.replace("{%CONTENT%}", content_html)
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == "__main__":
    # Test call could go here
    pass
