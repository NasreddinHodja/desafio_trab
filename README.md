
# Table of Contents

1.  [Configuração](#org07d1cb6)
2.  [IN](#orgad5f2a7)
3.  [OUT](#org7ac3ec1)
    1.  [Gráficos](#orgb4485be)
    2.  [Lista de setores](#orgbedc48c)



<a id="org07d1cb6"></a>

# Configuração

1.  No terminal, navemagos para a pasta onde queremos guardar nosso código
2.  Em seguida, executamos  
    
        git clone https://github.com/NasreddinHodja/desafio_trab.git
3.  O código faz uso do módulo pandas do python, que deve ser instalado com  
    
        pip install pandas
4.  O código está contido no arquivo `etl.py` que ser permitido para executar. Para isso, fazemos  
    
        chmod +x etl.py
5.  Finalmente, para executar o arquivo, fazemos  
    
        ./etl.py


<a id="orgad5f2a7"></a>

# IN

-   `deals.contactId -> contacts`
-   `deals.companyId -> companies`
-   `companies.sectorId -> sectors`


<a id="org7ac3ec1"></a>

# OUT


<a id="orgb4485be"></a>

## Gráficos

Primeiro output deve servir de base para dois gráficos: núm de vendar por contato e valor total vendido por mês.  


<a id="orgbedc48c"></a>

## Lista de setores

Segundo output deve ser uma lista de setores de empresa, ordenado por quanto esse setor representa no total vendido pela empresa no mês.  

