import requests

response = requests.get("https://lntu.edu.ua/uk/studentu-0/navchannya/rozklad-zanyat-ta-ispytiv-lntu")

decoded_text = response.content.decode('unicode_escape').replace('\\/', '/')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(decoded_text)

