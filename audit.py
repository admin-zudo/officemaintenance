import os
import re

dir_path = r'c:\Users\svpgl\OneDrive\Documents\GitHub\officemaintenance'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html') and os.path.isfile(os.path.join(dir_path, f))]

for file in html_files:
    with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip().replace('\n', ' ') if title_match else 'MISSING'
    
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, re.IGNORECASE | re.DOTALL)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']\s*/?>', content, re.IGNORECASE | re.DOTALL)
    desc = desc_match.group(1).strip().replace('\n', ' ') if desc_match else 'MISSING'
    
    print(f'FILE: {file}')
    print(f'TITLE: {title}')
    print(f'DESC: {desc}')
    print('-' * 40)
