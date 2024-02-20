#!/usr/bin/env python
# coding: utf-8

# # Análise Exploratória com Python (Matplotlib)

# # Gráficos Simples com Pyplot
# 

# In[2]:


import matplotlib.pyplot as plt
plt.plot #pedir ajuda


# In[4]:


#Gráfico de Linha Simples
plt.plot([1,2,3,4]) #Vetor como entrada
plt.ylabel('Eixo y') #Rotulação com um texto como entrada
plt.xlabel('Eixo x')
plt.show;


# In[5]:


plt.plot([10,20,30,40], [100,200,300,400]) #Plotando determinando x e y
plt.plot([10,20,30,40], [100,200,300,400], 'o') #Definindo o tipo de  marcadores do gráfico
plt.plot([10,20,30,40], [100,200,300,400], 'bo') #Definindo o tipo de  marcadores do  e cor do marcador


# In[6]:


plt.plot([10,20,30,40], [100,200,300,400], 'go--') #Linha pontilhada
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title('Título do Grafico')
plt.axis([0,100,0,1000]) #Definindo máximo e mínimo do gráfico


# In[7]:


plt.plot([10,20,30,40], [100,200,300,400], marker='o' , color='red', linewidth=4)
plt.scatter([10,20,30,40], [500,600,700,800], color='blue') #Criação de um gráfico de dispersão
plt.bar([10,20,30,40], [90,90,70,40], color='yellow') # Criação de um gráfico de barra


# # Figure, Axes, Subplot

# In[8]:


# Definir o tamanho da figura
plt.figure(figsize=[10, 2]) # (figsize=(largura,altura))

# Dados de exemplo
y = [10, 20, 30, 40]

# Criar um gráfico de linha
plt.plot(y)

# Exibir o gráfico
plt.show()


# In[9]:


import numpy as np

# Dados de exemplo
data = np.random.randn(1000)  # Dados aleatórios para o exemplo

# Criar uma figura e adicionar eixos
fig, ax = plt.subplots()

# Criar um histograma nos eixos especificados
ax.hist(data, bins=30, facecolor='blue', alpha=0.7) #Alpha pdoe ser bom para marcar parte do gráfico

# Adicionar rótulos aos eixos
ax.set_xlabel('Valores')
ax.set_ylabel('Frequência')
ax.set_title('Histograma', fontsize=18)

# Personalizar os spines
ax.spines['top'].set_color('red')      # Cor do spine superior
ax.spines['top'].set_linewidth(2)      # Largura do spine superior
ax.spines['bottom'].set_color('red')  # Cor do spine inferior
ax.spines['top'].set_linewidth(2)      # Largura do spine inferior
ax.spines['left'].set_color('green')   # Cor do spine esquerdo
ax.spines['right'].set_visible(False)   # Remover spine direito

# Exibir a figura
plt.show()


# In[10]:


# Criar uma figura e adicionar eixos
fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_axes([0.1, 0.1, 1, 0.4])

# Gerar dados de exemplo (criam uma amostra de 500 pontos seguindo uma distribuição normal com média 60 e desvio padrão 10)
nu, sigma = 60, 10
x = nu + sigma * np.random.randn(500)

# Criar um histograma nos eixos especificados
ax2.hist(x[x>50], bins=50, facecolor= 'red', alpha =0.99); #bins é o número de retangulo
ax2.hist(x[x<=50], bins=50, facecolor= 'red', alpha =0.35);


# In[11]:


plt.hist(x);


# # 1. Explorando um DataSet

# In[24]:


import pandas as pd

# Caminho para a planilha
caminho_planilha = r'C:\Users\casa\Downloads\Cursos\Projeto Pandas\archive\marketing_campaign.csv'

# Carregando a planilha utilizando o pandas com o separador "\t" (tabulação)
df = pd.read_csv(caminho_planilha, sep='\t')

# Exibindo todos os registros da planilha
df.head()


# # 2. Importando as Bibiliotecas

# In[23]:


import pandas as pd
import plotly.offline as py #Biblioteca para visualização de gráficos internamente.
import plotly.graph_objs as go #Biblioteca para criação de gráficos.


# # 3. Principais Gráficos

# ## 3.1 Gráfico de Linha

# In[37]:


# Tratando as Datas
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

# Criando Novas Colunas
df['Year_Customer']= df['Dt_Customer'].dt.year
df['Month_Customer']= df['Dt_Customer'].dt.month
df['Day_Customer']= df['Dt_Customer'].dt.day


# In[44]:


# Convertendo a coluna 'Income' para tipo numérico (float)
df['Income'] = pd.to_numeric(df['Income'], errors='coerce')

# Criando uma Series onde o index é o mês e o valor é o avg_income
data = df[df['Year_Customer'] == 2013].groupby('Month_Customer')['Income'].mean()

# Obtendo as variáveis
months = data.index  # Os meses para os quais a média de 'Income' foi calculada.
avg_income = data.values  # Média dos salários para cada mês em 2013


# ### Gráfico 1

# In[46]:


# Criando o gráfico com o graph_objs
lineal = go.Scatter(x=months, y=avg_income, mode='lines', name='Ligado por Linha')

# Definindo o Layout
layout = go.Layout(title='Salário médio dos clientes que entraram nos meses de 2013',
                   xaxis={'title': 'Mês'},
                   yaxis={'title': 'Salário Médio'}
                   )
# Criando a figura
fig = go.Figure(data=[lineal], layout=layout)

# Plotando a figura
py.iplot(fig)


# ### Gráfico 2

# In[50]:


# Criando o gráfico com o graph_objs
lineal = go.Scatter(x=months, y=avg_income, mode='markers', name='Ligado por Linha')

# Definindo o Layout
layout = go.Layout(title='Salário médio dos clientes que entraram nos meses de 2013',
                   xaxis={'title': 'Mês'},
                   yaxis={'title': 'Salário Médio'}
                   )
# Criando a figura
fig = go.Figure(data=[lineal], layout=layout)

# Plotando a figura
py.iplot(fig)


# ### Gráfico 3

# In[52]:


# Criando o gráfico com o graph_objs - Pontilhado
pontilhado= go.Scatter (x = [2019, 2020, 2021, 2022,2023], y =[60e4, 90e4, 100e4, 80e4, 101e4], mode= 'lines', # 'mode' define o tipo de linha e 'line' as propriedades da linhas
                       line= {'color' : '#999932', 'dash' :'dot'}, name ='Pontilhado')

# Criando o gráfico com o graph_objs - Tracejado
tracejado= go.Scatter (x = [2019, 2020, 2021, 2022,2023], y =[30e4, 50e4, 10e4, 35e4, 42e4], mode= 'lines',
                       line= {'color' :'#100032', 'dash' :'dash'}, name ='Tracejado')
# Definindo o Layout
layout = go.Layout(title="Faturamento por ano da Empresa X",
                   xaxis={'title': 'Ano'},
                   yaxis={'title': 'Faturamento'})

# Criando a figura
fig = go.Figure(data=[pontilhado, tracejado], layout=layout)

# Plotando a figura
py.iplot(fig)


# ## 3.2 Gráfico de Dispersão

# In[53]:


# Visualizando todos os parâmetros
get_ipython().run_line_magic('pinfo', 'go.Scatter')


# In[55]:


#Criando o gráfico com graph_objs
scatter= go.Scatter ( x= df.Year_Birth, y=df.Income, mode='markers',
                    #Configuração do Marker
                    marker= {'color': '#000053'}, opacity = 0.5, hovertemplate = 'Salário: U$ %{y}')

# Definindo o Layout
layout = go.Layout(title="Salários por ano de nascimento",
                   # Configuração do título
                   title_font= {'family': 'Gotham', 'size': 25, 'color': '#0e78a3'},
                   xaxis={'title': 'Ano de Nascimento'},
                   yaxis={'title': 'Salário'})


# Criando a figura
fig = go.Figure(data=[scatter], layout=layout)

# Plotando a figura
py.iplot(fig)


# ## 3.3 Gráfico de Barras

# ### Gráfico 1

# In[59]:


# Definindo as váriaveis
educational_level= df['Education'].value_counts().sort_values(ascending= True).index
quantity= df['Education'].value_counts().sort_values(ascending= True).values


# Criando o gráfico com o graph_objs
barra= go.Bar( x= educational_level, 
              y= quantity, 
              marker = {'color':'#ff9f43'})
# Definindo o Layout
layout = go.Layout(title="Quantidade de pessoas por nível educacional",
                   # Configuração do título
                   title_font={'family': 'Gotham', 'size': 25, 'color': '#0e78a3'},
                   title_x=0.5,  # Centraliza o título
                   xaxis={'title': 'Nível Educacional'},
                   yaxis={'title': 'Qnt de Pessoas'})
                        
# Criando a figura
fig = go.Figure(data=[barra], layout=layout)

# Plotando a figura
py.iplot(fig)


# ### Gráfico 2

# In[67]:


# Criando o gráfico com o graph_objs - Solteiros
barra_single = go.Bar(x=index_single,
                     y=quantity_single,
                     marker={'color': '#ff9f43'},
                     name='Solteiros',
                     hovertemplate='Porcentagem: %{y:.3f}%')

# Criando o gráfico com o graph_objs - Não Solteiros
barra_notsingle = go.Bar(x=index_not_single,
                        y=quantity_not_single,
                        marker={'color': '#feca57'},
                        name='Não Solteiros',
                        hovertemplate='Porcentagem: %{y:.3f}%')

# Definindo o Layout
layout = go.Layout(title="Quantidade de pessoas por nível educacional",
                   # Configuração do título
                   title_font={'family': 'Gotham', 'size': 25, 'color': '#0e78a3'},
                   title_x=0.5,  # Centraliza o título
                   xaxis={'title': 'Nível Educacional'},
                   yaxis={'title': 'Qnt de Pessoas (%)'})

# Criando a figura
fig = go.Figure(data=[barra_single, barra_notsingle], layout=layout)

# Plotando a figura
py.iplot(fig)


# ### Gráfico 3 (Gráfico de Barras Empilhado)

# In[66]:


# Criando o gráfico com o graph_objs - Solteiros
barra_single = go.Bar(x=index_single,
                     y=quantity_single,
                     marker={'color': '#ff9f43'},
                     name='Solteiros',
                     hovertemplate='Porcentagem: %{y:.3f}%')

# Criando o gráfico com o graph_objs - Não Solteiros
barra_notsingle = go.Bar(x=index_not_single,
                        y=quantity_not_single,
                        marker={'color': '#feca57'},
                        name='Não Solteiros',
                        hovertemplate='Porcentagem: %{y:.3f}%')

# Definindo o Layout
layout = go.Layout(title="Quantidade de pessoas por nível educacional",
                   # Configuração do título
                   title_font={'family': 'Gotham', 'size': 25, 'color': '#0e78a3'},
                   title_x=0.5,  # Centraliza o título
                   xaxis={'title': 'Nível Educacional'},
                   yaxis={'title': 'Qnt de Pessoas (%)'},
                   barmode='stack')  # Adicionando o parâmetro para barras empilhadas

# Criando a figura
fig = go.Figure(data=[barra_single, barra_notsingle], layout=layout)

# Plotando a figura
py.iplot(fig)


# # Boxplot

# In[75]:


# Criando o gráfico com o graph_objs
boxplot_2ncycle = go.Box(y=df.loc[df['Education'] == '2n Cycle', 'Income'],
                        marker={'color': '#00CED1'},
                        name='2n Cycle')

boxplot_basic = go.Box(y=df.loc[df['Education'] == 'Basic', 'Income'],
                      marker={'color': '#FF6F61'},
                      name='Basic')

boxplot_graduation = go.Box(y=df.loc[df['Education'] == 'Graduation', 'Income'],
                           marker={'color': '#FFD700'},
                           name='Graduation')

boxplot_master = go.Box(y=df.loc[df['Education'] == 'Master', 'Income'],
                        marker={'color': '#C71585'},
                        name='Master')

boxplot_phd = go.Box(y=df.loc[df['Education'] == 'PhD', 'Income'],
                     marker={'color': '#778899'},
                     name='PhD')

# Definindo o Layout
layout = go.Layout(title="Quantidade de pessoas por nível educacional",
                   # Configuração do título
                   title_font={'family': 'Gotham', 'size': 25, 'color': '#0e78a3'},
                   xaxis={'title': 'Nível Educacional'},
                   yaxis={'title': 'Quantidade de pessoas (%)'},
                   barmode='stack')  # Adicionando o parâmetro para barras empilhadas

# Criando a figura
fig = go.Figure(data=[boxplot_2ncycle, boxplot_basic, boxplot_graduation, boxplot_master, boxplot_phd], layout=layout)

# Plotando o gráfico
py.iplot(fig)


# In[ ]:




