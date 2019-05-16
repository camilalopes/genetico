## Iris

#### KNN

A base de dados Iris já apresenta os dados previamente classificados e utilizando de 80% do dataset foi possível obter 100% de acerto ao passar para o KNN as 4 dimensões de cada flor.
```
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      1.00      1.00        10
           2       1.00      1.00      1.00        10

   micro avg       1.00      1.00      1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30
```

#### K-means

Ao utilizar o algoritmo de agrupamento k-means o resultado obtido é o da imagem abaixo:  
![Resultado do Agrupamento](https://i.imgur.com/PBswS4i.png)  

Para efeito de comparação, esta é a divisão original:  
![Imagem Original](https://i.imgur.com/SwOH4PD.png)  

É possível perceber as diferenças claramente mas no geral o algoritmo teve um bom desempenho.

## Boston

A base de dados de boston necessita uma exploração inicial para que seja possível aplicar de maneira eficiente os algoritmos.

#### Exploração

Para começar a exploração chutamos a primeira relação que poderia ser interessante dentro dos dados oferecidos pelo conjunto de dados. Esta seria a relação entre criminalidade e valor médio:  
![Criminalidade X Valor Médio](https://i.imgur.com/7f4LVLR.png)  

Posteriormente seguimos a tabela de correlação da base para as próximas análises:  
![Tabela de Correlação](https://i.imgur.com/kkUIxXI.png)  

Os maiores índices encontrados em relação ao preço médio foram, respectivamente: % de pessoas com status mais baixo, número de cômodos na casa e relação aluno/professor no bairro.  
![% de pessoas com status mais baixo](https://i.imgur.com/6o1TMOj.png)  
![número de cômodos na casa](https://i.imgur.com/A5PWHUs.png)  
![relação aluno/professor no bairro](https://i.imgur.com/11DIbow.png)  

Estas serão as relações priorizadas durante a aplicação do algoritmo.

#### KNN



#### K-means




