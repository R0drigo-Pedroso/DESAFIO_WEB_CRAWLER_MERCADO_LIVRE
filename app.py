import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup

def buscar_produtos(query, nome, num_paginas=1):
    produtos = []

    for pagina in range(1, num_paginas + 1):
        url = f'https://lista.mercadolivre.com.br/{query}_{nome}_Desde_{pagina}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrando todos os itens da lista de produtos
        for item in soup.find_all('div', class_="ui-search-result__content-wrapper"):
            # Extraindo informações de cada item
            titulo = item.find('h2', class_='ui-search-item__title').text.strip()
            url_produto = item.find('a', class_='ui-search-link')['href']
            preco_produto = item.find('span', class_='andes-money-amount__fraction').text.strip()
            vendedor_nome = item.find('span', class_='ui-search-item__group__element').text.strip()
            url_vendedor = item.find('a', class_='ui-search-link')['href']
            
            # Aqui vamos acessar o link do produto para obter o nome do vendedor
            response_produto = requests.get(url_produto)
            soup_produto = BeautifulSoup(response_produto.text, 'html.parser')
            vendedor_nome = soup_produto.find('span', class_='ui-pdp-color--BLUE ui-pdp-family--REGULAR').text.strip()
            
            url_vendedor = item.find('a', class_='ui-search-link')['href']
            
            produtos.append({
                'Título do produto': titulo,
                'URL do produto': url_produto,
                'Preço do Produto': preco_produto,
                'Nome do Vendedor': vendedor_nome,
                'URL do Vendedor': url_vendedor
            })
        
        return produtos

def salvar_em_xlsx(produtos):
    wb = Workbook()
    ws = wb.active
    ws.append(['Título do produto', 'URL do produto', 'Preço do Produto', 'Nome do Vendedor', 'URL do Vendedor'])
    
    for produto in produtos:
        ws.append([produto['Título do produto'], produto['URL do produto'], produto['Preço do Produto'], produto['Nome do Vendedor'], produto['URL do Vendedor']])
    
    wb.save('produtos.xlsx')

def buscar_e_salvar():
    query = entry_query.get()
    nome = entry_nome.get()
    try:
        num_paginas = int(entry_num_paginas.get())
        produtos = buscar_produtos(query, nome, num_paginas)
        salvar_em_xlsx(produtos)
        messagebox.showinfo("Sucesso", "Os dados foram salvos em produtos.xlsx")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o número de páginas.")

# Configuração da janela principal
root = tk.Tk()
root.title("Busca de Produtos")

# Frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels e Entradas
label_query = ttk.Label(frame, text="Termo de busca:")
label_query.grid(row=0, column=0, sticky=tk.W)
entry_query = ttk.Entry(frame, width=30)
entry_query.grid(row=0, column=1, sticky=tk.W, pady=4)

label_nome = ttk.Label(frame, text="Nome específico do produto:")
label_nome.grid(row=1, column=0, sticky=tk.W)
entry_nome = ttk.Entry(frame, width=30)
entry_nome.grid(row=1, column=1, sticky=tk.W, pady=4)

label_num_paginas = ttk.Label(frame, text="Número de páginas:")
label_num_paginas.grid(row=2, column=0, sticky=tk.W)
entry_num_paginas = ttk.Entry(frame, width=5)
entry_num_paginas.grid(row=2, column=1, sticky=tk.W, pady=4)

# Botão de busca e salvamento
button_buscar = ttk.Button(frame, text="Buscar e Salvar", command=buscar_e_salvar)
button_buscar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
