import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import selenium

query = input('Digite o produto que deseja pesquisar: ')


response = requests.get(f'https://www.magazineluiza.com.br/busca/{query}')

list_products = []

content = response.content

site = BeautifulSoup(content, 'html.parser')

case_product = site.find('div', attrs={'class': 'productShowCaseContent'})
products = case_product.findAll('li', attrs={'class': 'product'})

for product in products:
   #print("Produto----->")
   title_product =  product.find('h3', attrs={'class': 'productTitle'})
   #print(title_product.text)
   nome = title_product.text
   link_product = product.find('a', attrs={'class': 'product-li'})
   #print(link_product['href'])
   link = link_product['href']
   product_price = product.find('span', attrs={'class': 'price-value'})
   if (product_price):
      #print(product_price.text)
      preço = product_price.text
   else:
      product_price = product.find('span', attrs={'class': 'price'})
      #print(product_price.text)  
      preço = product_price.text
   list_products.append([nome, link, preço])

#print(list_products)

tab_products = pd.DataFrame(list_products, columns=['Nome do Produto', 'Link do Produto', 'Preço'])
#tab_products.to_excel('Planilha_Magalu.xlsx', index=False)

print(tab_products)