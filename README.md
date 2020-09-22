
# Table of Contents

1.  [Configuração](#org9a5fe3b)
2.  [IN](#org7b4b61b)
3.  [OUT](#org499f3e1)
    1.  [Gráficos](#orga1cd6cf)
    2.  [Lista de setores](#org1de9312)



<a id="org9a5fe3b"></a>

# Configuração

1.  No terminal, navemagos para a pasta onde queremos guardar nosso código
2.  Em seguida, executamos  
    
        git clone https://github.com/NasreddinHodja/desafio_trab.git
3.  O código faz uso do módulo pandas do python, que deve ser instalado com  
    
        pip install pandas
4.  O código está contido no arquivo `etl.py` que deve ser permitido para ser executado. Para isso, fazemos  
    
        chmod +x etl.py
5.  Finalmente, para executar o arquivo, fazemos  
    
        ./etl.py


<a id="org7b4b61b"></a>

# IN

-   `deals.contactId -> contacts`
-   `deals.companyId -> companies`
-   `companies.sectorId -> sectors`


<a id="org499f3e1"></a>

# OUT


<a id="orga1cd6cf"></a>

## Gráficos

Primeiro output deve servir de base para dois gráficos: núm de vendar por contato e valor total vendido por mês.  


<a id="org1de9312"></a>

## Lista de setores

Segundo output deve ser uma lista de setores de empresa, ordenado por quanto esse setor representa no total vendido pela empresa no mês.  

