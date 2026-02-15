import json
import os
from datetime import datetime, timedelta

DATA_FILE = 'news_data.json'
HTML_FILE = 'index.html'

def update_news(new_entries):
    # 1. Load existing data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    # 2. Add new entries
    for entry in new_entries:
        entry["timestamp"] = datetime.now().timestamp()
        entry["date"] = datetime.now().strftime("%Y-%m-%d")
        data.insert(0, entry)

    # 3. Security Check: Deduplication by link
    seen_links = set()
    unique_data = []
    for item in data:
        if item['link'] not in seen_links:
            unique_data.append(item)
            seen_links.add(item['link'])
    
    # 4. Global Sort: Newest First
    # Assuming the date field exists or using the timestamp we added
    unique_data.sort(key=lambda x: x.get('timestamp', 0), reverse=True)

    # 5. Remove older than 7 days
    seven_days_ago = (datetime.now() - timedelta(days=7)).timestamp()
    unique_data = [item for item in unique_data if item.get('timestamp', 0) > seven_days_ago]

    # 6. Save back to database
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=2)

    render_html(unique_data)

def render_html(data):
    # Separate data into categories
    world_news = [i for i in data if i['category'] == 'World']
    cyber_news = [i for i in data if i['category'] == 'Cyber Security']
    ai_news = [i for i in data if i['category'] == 'AI & Fintech']

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
            .section-label { writing-mode: vertical-rl; text-orientation: mixed; }
            .card { background: #1e293b; border: 1px solid #334155; transition: all 0.2s; }
            .card:hover { border-color: #3b82f6; transform: translateY(-2px); }
        </style>
    </head>
    <body class="p-4 md:p-12">
        <header class="max-w-7xl mx-auto mb-16 border-b border-slate-800 pb-12">
            <h1 class="text-5xl font-black tracking-tighter italic text-blue-500 uppercase">Intelligence Briefing</h1>
            <p class="text-slate-500 font-mono text-sm mt-2">SECURED FEED • SORTED BY LATEST</p>
        </header>

        <main class="max-w-7xl mx-auto grid grid-cols-1 xl:grid-cols-3 gap-12">
            
            <!-- WORLD NEWS COLUMN -->
            <section class="space-y-6">
                <div class="flex items-center gap-4 mb-8">
                    <span class="text-3xl">🌐</span>
                    <h2 class="text-2xl font-black uppercase text-blue-400 tracking-widest">World Updates</h2>
                </div>
                <div class="space-y-6">{%WORLD%}</div>
            </section>

            <!-- CYBER SECURITY COLUMN -->
            <section class="space-y-6">
                <div class="flex items-center gap-4 mb-8">
                    <span class="text-3xl">🛡️</span>
                    <h2 class="text-2xl font-black uppercase text-red-400 tracking-widest">Cyber Security</h2>
                </div>
                <div class="space-y-6">{%CYBER%}</div>
            </section>

            <!-- AI & FINTECH COLUMN -->
            <section class="space-y-6">
                <div class="flex items-center gap-4 mb-8">
                    <span class="text-3xl">🤖</span>
                    <h2 class="text-2xl font-black uppercase text-emerald-400 tracking-widest">AI / Fintech</h2>
                </div>
                <div class="space-y-6">{%AI%}</div>
            </section>

        </main>

        <footer class="max-w-7xl mx-auto mt-24 py-12 border-t border-slate-800 text-center text-slate-600 font-mono text-xs italic">
            END-TO-END AUTOMATED GENERATION • NO_IDENTIFIERS_STORED
        </footer>
    </body>
    </html>
    """

    def build_articles(subset):
        output = ""
        for item in subset:
            output += f"""
            <article class="card p-6 rounded-2xl">
                <div class="flex justify-between items-center mb-4">
                    <span class="text-[10px] font-bold bg-slate-800 px-2 py-1 rounded text-slate-400 tracking-widest uppercase">📅 {item['date']}</span>
                    <span class="text-[9px] text-slate-600 font-mono italic">{item['source']}</span>
                </div>
                <h3 class="text-lg font-bold text-slate-100 leading-snug mb-2">{item['en_title']}</h3>
                <h3 class="text-md font-bold text-slate-400 leading-snug mb-6 border-l-2 border-slate-700 pl-4">{item['cn_title']}</h3>
                <div class="space-y-4 text-xs leading-relaxed text-slate-500 mb-6">
                    <p>{item['en_summary']}</p>
                    <p class="text-slate-600 italic">{item['cn_summary']}</p>
                </div>
                <div class="flex justify-end">
                    <a href="{item['link']}" target="_blank" rel="noopener" class="text-blue-500 font-bold hover:underline text-[10px]">ORIGIN_ACCESS &rarr;</a>
                </div>
            </article>
            """
        return output

    html = html_template.replace("{%WORLD%}", build_articles(world_news))
    html = html.replace("{%CYBER%}", build_articles(cyber_news))
    html = html.replace("{%AI%}", build_articles(ai_news))

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
