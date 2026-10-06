import json

with open('D:/Mayoohka_demo/scratch/lh_index_baseline.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

reqs = data['audits']['network-requests']['details']['items']
print(f'Total requests: {len(reqs)}')
reqs_sorted = sorted(reqs, key=lambda x: x.get('transferSize', 0), reverse=True)
for r in reqs_sorted[:20]:
    name = r.get('url', '').split('/')[-1] or r.get('url', '')
    size = r.get('transferSize', 0) / 1024
    dur = (r.get('networkEndTime', 0) - r.get('networkRequestTime', 0))
    print(f"  {name[:40]}: {size:.1f} KB (mime: {r.get('mimeType', '')})")
