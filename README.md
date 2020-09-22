
# Table of Contents

1.  [Configuração](#orgc1913bd)
2.  [IN](#org4faf4dd)
3.  [OUT](#orgcbdf4f9)
    1.  [Gráficos](#org8b04850)
    2.  [Lista de setores](#orgd3146bd)



<a id="orgc1913bd"></a>

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


<a id="org4faf4dd"></a>

# IN

-   `deals.contactId -> contacts`
-   `deals.companyId -> companies`
-   `companies.sectorId -> sectors`


<a id="orgcbdf4f9"></a>

# OUT


<a id="org8b04850"></a>

## Gráficos

Primeiro output deve servir de base para dois gráficos: núm de vendar por contato e valor total vendido por mes.  


<a id="orgd3146bd"></a>

## Lista de setores

Segundo output deve ser uma lista de setores de empresa, ordenado por quanto esse setor representa no total vendido pela empresa no mês.  

