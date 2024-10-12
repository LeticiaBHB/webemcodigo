import requests
from bs4 import BeautifulSoup

# URL da página que você quer inspecionar
url = "https://github.com/"

# Enviar uma requisição GET para a URL
response = requests.get(url)

# Analisar (parse) o conteúdo da página com BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Exibir o HTML da página
print("HTML da página:")
print(soup.prettify())

# Encontrar todos os links para arquivos CSS
css_links = soup.find_all('link', rel='stylesheet')

# Exibir o conteúdo de cada arquivo CSS
for link in css_links:
    # Verificar se a tag <link> tem o atributo 'href'
    if 'href' in link.attrs:
        css_url = link['href']

        # Verificar se o link CSS é relativo ou absoluto
        if not css_url.startswith('http'):
            css_url = url + css_url

        # Fazer requisição para obter o CSS
        css_response = requests.get(css_url)

        # Exibir o conteúdo do CSS
        print(f"\nConteúdo do CSS ({css_url}):")
        print(css_response.text)
    else:
        print("Link encontrado sem o atributo 'href'.")
