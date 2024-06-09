import sys
import requests

def probe(out_file):
    url = sys.stdin.read().splitlines()
    
    res_urls = []
    bad_urls = []
    
    for link in url: 
        try:
            response = requests.head(link)
            if response.status_code == 200:
                res_urls.append(link)
            else: 
                bad_urls.append(link)
        except requests.exceptions.MissingSchema:
            bad_urls.append(link)
            continue

    with open(out_file, 'w') as file:
        file.write('\n'.join(res_urls))

    print(f'Saved Urls {out_file}')

out_file = 'filtered_urls.txt'
probe(out_file)
