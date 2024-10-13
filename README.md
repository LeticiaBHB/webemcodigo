# Web Inspector

Este projeto é um script Python que inspeciona uma página web, exibe seu HTML e extrai o conteúdo dos arquivos CSS referenciados. Ele utiliza as bibliotecas `requests` e `BeautifulSoup` para fazer a requisição HTTP e analisar o conteúdo HTML da página.

## Funcionalidades

- Realiza requisições HTTP para uma URL especificada.
- Exibe o HTML da página de forma estruturada (prettified).
- Busca todos os links de arquivos CSS referenciados no HTML.
- Faz requisições para cada arquivo CSS e exibe seu conteúdo.

## Tecnologias Utilizadas

- **Python 3.x**
- **BeautifulSoup**: Utilizada para análise e extração do HTML.
- **Requests**: Utilizada para fazer requisições HTTP.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/web-inspector.git
2. Instale as dependências:

pip install -r requirements.txt
Modifique o código-fonte para usar a URL que você deseja inspecionar. No arquivo main.py, altere a variável url:

url = "https://www.exemplo.com"
Execute o script:
python main.py

O HTML da página será exibido no console, seguido pelos conteúdos de cada arquivo CSS referenciado.
