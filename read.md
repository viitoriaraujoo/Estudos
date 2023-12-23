# PYTHON PARA DATA SCIENCE

Para instalar ou atualizar uma biblioteca no Python, podemos recorrer ao `pip` que é um gerenciador de bibliotecas no Python. 

````python
# Instalando a biblioteca matplotlib pelo pip
!pip install matplotlib
````
Existe também o PYPI que é um repositório de bibliotecas Python que traz as bibliotecas mais utilizadas pela comunidade junto a informações de como usar e acesso as documentações de cada uma delas.
PYPI ([https://pypi.org/](https://pypi.org/))
````python
# Importando uma biblioteca com alias
import matplotlib.pyplot as plt
````

## 1.1 Utilizando pacotes/bibliotecas
#### Exemplo 1: Vamos testar a biblioteca Matplotlib para um exemplo de médias de estudantes de uma classe.

(https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

````python
estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]
plt.bar(x = estudantes, height = notas) --- gerar gráfico
````

#### Exemplo 2: Vamos selecionar aleatoriamente um aluno para apresentar o seu trabalho de ciência de dados usando a biblioteca Random
````python
estudantes_2 = ["João", "Maria", "José", "Ana"]
# Importando uma função específica de uma biblioteca
from random import choice
````
