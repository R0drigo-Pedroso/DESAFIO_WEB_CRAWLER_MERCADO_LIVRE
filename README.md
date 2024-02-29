# Busca de Produtos no Mercado Livre

Este é um aplicativo de desktop simples desenvolvido em Python usando Tkinter que permite ao usuário buscar produtos no Mercado Livre, especificando um termo de busca, um nome específico do produto e o número de páginas a serem pesquisadas. Os dados dos produtos encontrados são salvos em um arquivo Excel.

## Pré-requisitos

Antes de executar o aplicativo, certifique-se de ter as seguintes bibliotecas Python instaladas:

- `requests`
- `beautifulsoup4`
- `openpyxl`

Você pode instalar essas dependências usando o pip:

```
pip install requests beautifulsoup4 openpyxl
```

## Como usar

Para iniciar o aplicativo, execute o arquivo `busca_produtos.py`. Isso abrirá uma janela onde você pode inserir os seguintes detalhes:

- **Termo de busca:** O termo geral para a pesquisa, por exemplo, "celular".
- **Nome específico do produto:** Um nome específico do produto que deseja pesquisar, por exemplo, "iphone 12".
- **Número de páginas:** O número de páginas de resultados de pesquisa que deseja buscar.

Depois de inserir esses detalhes, clique no botão "Buscar e Salvar". O aplicativo buscará os produtos no Mercado Livre com base nos critérios especificados e salvará os dados encontrados em um arquivo Excel chamado `produtos.xlsx` no diretório atual.

## Explicação do Código

- `buscar_produtos(query, nome, num_paginas)`: Esta função realiza a busca dos produtos no Mercado Livre com base nos detalhes fornecidos pelo usuário. Ele usa a biblioteca `requests` para fazer solicitações HTTP para a página de resultados de pesquisa e `BeautifulSoup` para analisar o HTML da página e extrair os dados dos produtos.
  
- `salvar_em_xlsx(produtos)`: Esta função recebe uma lista de produtos e os salva em um arquivo Excel usando a biblioteca `openpyxl`.

- `buscar_e_salvar()`: Esta função é chamada quando o usuário clica no botão "Buscar e Salvar". Ele obtém os detalhes fornecidos pelo usuário, chama a função `buscar_produtos` para buscar os produtos e a função `salvar_em_xlsx` para salvar os dados encontrados em um arquivo Excel.

- A interface gráfica é criada usando a biblioteca Tkinter. Ela possui campos de entrada para o termo de busca, o nome específico do produto e o número de páginas, bem como um botão para iniciar a busca e salvamento.

Espero que isso ajude a entender o funcionamento do aplicativo. Se você tiver alguma dúvida, não hesite em entrar em contato.
