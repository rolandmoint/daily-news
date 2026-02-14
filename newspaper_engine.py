import json
import os
from datetime import datetime, timedelta

DATA_FILE = 'news_data.json'
HTML_FILE = 'index.html'

def update_news(news_list):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    for entry in news_list:
        entry["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry["timestamp"] = datetime.now().timestamp()
        data.insert(0, entry)

    seen_links = set()
    unique_data = []
    for item in data:
        if item['link'] not in seen_links:
            unique_data.append(item)
            seen_links.add(item['link'])
    
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
        <title>Intelligence Briefing Core</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }
            .feed-card { border-left: 4px solid transparent; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
            .feed-card:hover { transform: scale(1.01); background-color: #1e293b; }
            .category-world { border-left-color: #3b82f6; }
            .category-ai { border-left-color: #10b981; }
            .category-sec { border-left-color: #ef4444; }
            .filter-btn { cursor: pointer; transition: all 0.2s; }
            .filter-active { outline: 2px solid white; outline-offset: 2px; }
        </style>
    </head>
    <body class="p-4 md:p-12">
        <header class="max-w-5xl mx-auto mb-16 border-b border-slate-800 pb-12">
            <div class="flex justify-between items-end">
                <div>
                    <h1 class="text-4xl font-black tracking-tighter mb-2 italic">INTELLIGENCE CORE</h1>
                    <p class="text-slate-500 font-mono text-sm uppercase tracking-widest">Automatic Feed • 7-Day Rolling Window</p>
                </div>
                <div class="text-right font-mono text-xs text-slate-600">
                    SECURED_PROTOCOL_V2<br>ANONYMOUS_SESSION
                </div>
            </div>
            
            <nav class="mt-12 flex flex-wrap gap-3">
                <button onclick="filter('all')" class="filter-btn px-4 py-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-bold uppercase tracking-tighter">View All</button>
                <button onclick="filter('world')" class="filter-btn px-4 py-2 bg-blue-900/40 text-blue-400 hover:bg-blue-900/60 rounded-lg text-xs font-bold uppercase tracking-tighter border border-blue-800/50">World</button>
                <button onclick="filter('ai')" class="filter-btn px-4 py-2 bg-emerald-900/40 text-emerald-400 hover:bg-emerald-900/60 rounded-lg text-xs font-bold uppercase tracking-tighter border border-emerald-800/50">AI & Fintech</button>
                <button onclick="filter('sec')" class="filter-btn px-4 py-2 bg-red-900/40 text-red-400 hover:bg-red-900/60 rounded-lg text-xs font-bold uppercase tracking-tighter border border-red-800/50">Cyber Security</button>
            </nav>
        </header>

        <main id="news-container" class="max-w-5xl mx-auto space-y-6">
            {%CONTENT%}
        </main>

        <footer class="max-w-5xl mx-auto mt-24 py-12 border-t border-slate-800 text-center text-slate-600 font-mono text-[10px] uppercase tracking-[0.2em]">
            Automated Briefing System • End-to-End Generated content
        </footer>

        <script>
            function filter(type) {
                const cards = document.querySelectorAll('.feed-card');
                cards.forEach(card => {
                    if (type === 'all') {
                        card.style.display = 'block';
                    } else if (type === 'world' && card.classList.contains('category-world')) {
                        card.style.display = 'block';
                    } else if (type === 'ai' && card.classList.contains('category-ai')) {
                        card.style.display = 'block';
                    } else if (type === 'sec' && card.classList.contains('category-sec')) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
        </script>
    </body>
    </html>
    """
    
    content_html = ""
    for item in data:
        cat_class = "category-world"
        cat_name = "World Update"
        if "AI" in item['category']: 
            cat_class = "category-ai"
            cat_name = "AI / Fintech"
        elif "Cyber" in item['category']: 
            cat_class = "category-sec"
            cat_name = "Security"

        content_html += f"""
        <article class="bg-slate-900/50 p-8 rounded-2xl border border-slate-800/50 feed-card {cat_class}">
            <div class="flex justify-between items-center mb-6">
                <span class="font-mono text-[10px] text-slate-500 uppercase tracking-widest">{item['date']}</span>
                <span class="px-2 py-0.5 bg-slate-800 text-slate-400 border border-slate-700 rounded text-[9px] font-bold uppercase tracking-tighter">{cat_name}</span>
            </div>
            <div class="space-y-4">
                <h3 class="text-2xl font-bold text-slate-100 tracking-tight leading-tight uppercase font-mono">{item['en_title']}</h3>
                <h3 class="text-xl font-bold text-slate-300 leading-tight border-l-2 border-slate-700 pl-4">{item['cn_title']}</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 my-8 text-sm leading-relaxed">
                <div class="text-slate-400">{item['en_summary']}</div>
                <div class="text-slate-500 italic border-l border-slate-800 pl-6">{item['cn_summary']}</div>
            </div>
            <div class="flex justify-between items-center pt-6 border-t border-slate-800">
                <span class="text-[10px] text-slate-600 font-mono italic">REF_ORIGIN: {item['source']}</span>
                <a href="{item['link']}" target="_blank" rel="noopener noreferrer" class="bg-slate-100 text-slate-900 px-4 py-2 rounded-lg text-xs font-black uppercase hover:bg-white transition-colors">Source_Access &rarr;</a>
            </div>
        </article>
        """
    
    final_html = html_template.replace("{%CONTENT%}", content_html)
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)
