<img width=80% src="https://capsule-render.vercel.app/api?type=waving&color=0:00BFFF,50:6A5ACD,100:800080&text=Documentação&fontSize=70&height=180&section=header"/>

# Projeto ADA: Engenharia de Dados e Garantia de Qualidade no Conjunto de Dados do Airbnb no Rio de Janeiro


> [!NOTE]
>
>![Colaboradores](https://img.shields.io/badge/Colaboradores-007BFF?style=flat&logo=people&logoColor=white)
>
>Letícia Bertoldi
>
>José Pedro Morgado
>
>Hallynny
>
>Jonathan
>

---

> [!IMPORTANT]
>
>## Pergunta de mercado:
>
>### Trazer os seguintes dados organizados por bairro:
>
>    * Demanda mensal de reservas
>    * Média de preço
>    * Quantidade de avaliações
>    * Média das avaliações
>

---

> [!NOTE]
>
> Os bancos de dados bronze.duckdb e silver_1.duckdb foram zipados na pasta 'bancos de dados zipados' para serem enviados para o GitHub por conta do limite de armazenamento por arquivo
>

---

# Relatório do Projeto

## Projeto criado com a utilização do DBT e DUCKDB utilizando python e SQL, após a inicialização do dbt foram seguidos os seguintes passos:

---

## Banco de dados:

1. Criação do arquivo profiles.yml com o target dos seguintes bancos de dados com seus caminhos de destino designados: bronze.duckdb, silver_1.duckdb, silver_2.duckdb, gold.duckdb

2. Edição do arquivo dbt_project.yml para adição da configuração do schema de cada banco de dados

3. Criação dos bancos de dados com as configurações acima por meio do dbt run

## Camada Bronze:

1. Download e unzip dos arquivos CSV - calendar, listings e reviews - referente a cidade do Rio de Janeiro

[airbnb - todos os arquivos](https://insideairbnb.com/get-the-data/)

[Link para Download direto do arquivo listings - Rio de Janeiro](https://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2024-06-27/data/listings.csv.gz)

[Link para Download direto do arquivo calendar - Rio de Janeiro](https://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2024-06-27/data/calendar.csv.gz)

[Link para Download direto do arquivo reviews - Rio de Janeiro](https://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2024-06-27/data/reviews.csv.gz)

2. Carregamento dos arquivos CSV pelos arquivos - bronze_calendar.py, bronze_listings.py, bronze_reviews.py - para a camada bronze situada no banco de dados bronze.duckdb

3. Criação do schema da camada bronze em models/bronze/schema.yml

4. Validação com Pandera da camada bronze em models/bronze/validacao_calendar.ipynb e models/bronze/validacao_listings.ipynb com os erros encontrados comentados no final do arquivo, se houver.

5. Resumo das tabelas com tipagem e primeiras linhas das tabelas em models/bronze/resumo_tabelas.ipynb

---

## Camada Silver_1:

1. Criação do schema da camada silver_1 em models/silver_1/schema.yml

2. Cópia das tabelas calendar, listings, reviews do banco bronze.duckdb para o banco silver_1.duckdb pelos arquivos silver_calendar.py, silver_listings.py, silver_reviews.py

3. Na tabela listings no banco de dados bronze.duckdb os dados foram inseridos duplicados por engano, no terminal do duckdb foi criado nova tabela sem duplicadas, a tabela listings foi removida e a nova tabela renomeada para listings

4. Validação com Pandera da camada silver_1 em models/silver_1/validacao_calendar.ipynb e models/silver_1/validacao_listings.ipynb com os erros encontrados comentados no final do arquivo, se houver.

5. Resumo das tabelas com tipagem e primeiras linhas das tabelas em models/silver_1/resumo_tabelas.ipynb

---

## Camada Silver_2:

1. Criação do schema da camada silver_2 em models/silver_2/schema.yml

2. Criação da tabela calendar_silver vazia no banco de dados silver_2.duckdb apenas com colunas que serão utilizadas e com tipagem das colunas: listing_id - bigint, date - datetime, available - boolean em models/silver_2/silver_calendar_silver.py

3. Criação da tabela listings_silver vazia no banco de dados silver_2.duckdb apenas com colunas que serão utilizadas e com tipagem das colunas: id - bigint, neighbourhood_cleansed - varchar, price - double, number_of_reviews - integer, review_scores_rating - double em models/silver_2/silver_listings_silver.py

4. Extração dos dados da tabela calendar do banco de dados silver_1.duckdb das colunas criadas acima para a tabela calendar_silver no banco de dados silver_2.duckdb, em models/silver_2/tratamento_calendar_silver.ipynb. Não foi necessário modificações.

5. Extração dos dados da tabela listings do banco de dados silver_1.duckdb das colunas criadas acima para a tabela listings_silver no banco de dados silver_2.duckdb, em models/silver_2/tratamento_listings_silver.ipynb, foi aplicado o seguinte tratamento:

    * Na coluna price foi removido o $
    * Na coluna price os nulos foram substituídos por 0 para facilitar a soma/média dos valores na próxima etapa
    * Na coluna review_scores_rating os nulos foram substituídos por 0 para facilitar a soma/média dos valores na próxima etapa

6. Validação com Pandera da camada silver_2 em models/silver_2/validacao_calendar_silver.ipynb e models/silver_2/validacao_listings_silver.ipynb com os erros encontrados comentados no final do arquivo, se houver.

7. Resumo das tabelas com tipagem e primeiras linhas das tabelas em models/silver_2/resumo_tabelas.ipynb

---

## Camada Gold:

1. Criação do schema da camada gold em models/gold/schema.yml

2. Criação da tabela demanda_por_bairro vazia no banco de dados gold.duckdb com as colunas definidas pela pergunta de mercado com as seguintes tipagens, pelo arquivo em models/gold/demanda_por_bairro.py: 

    * bairro VARCHAR,                    -- Bairro é a coluna principal, seus valores são únicos
    * demanda_jan - INTEGER,             -- Demanda de reservas para janeiro
    * demanda_fev - INTEGER,             -- Demanda de reservas para fevereiro
    * demanda_mar - INTEGER,             -- Demanda de reservas para março
    * demanda_abr - INTEGER,             -- Demanda de reservas para abril
    * demanda_mai - INTEGER,             -- Demanda de reservas para maio
    * demanda_jun - INTEGER,             -- Demanda de reservas para junho
    * demanda_jul - INTEGER,             -- Demanda de reservas para julho
    * demanda_ago - INTEGER,             -- Demanda de reservas para agosto
    * demanda_set - INTEGER,             -- Demanda de reservas para setembro
    * demanda_out - INTEGER,             -- Demanda de reservas para outubro
    * demanda_nov - INTEGER,             -- Demanda de reservas para novembro
    * demanda_dez - INTEGER,             -- Demanda de reservas para dezembro
    * media_preco - DOUBLE,              -- Média de preço do bairro
    * quantidade_avaliacoes - INTEGER,   -- Quantidade total de avaliações
    * media_avaliacoes - DOUBLE,         -- Média das avaliações

3. No arquivo models/gold/tratamento_gold.ipynb foram aplicados os seguintes filtros para carregamento dos dados nas suas respectivas colunas na tabela demanda_por_bairro do banco de dados gold.duckdb:

    * Foi selecionado todos os bairros da tabela listings_silver do banco silver_2 e os valores foram adicionados de forma única na coluna bairro da tabela demanda_por_bairro do banco gold
    * Foi feito o filtro de quantas reservas foram feitas para cada mês, dando join das tabelas listings_silver pela coluna id e da tabela calendar_silver pela coluna listing_id, ambas do banco de dados silver_2, filtrando a coluna neighbourhood_cleansed da tabela listings_silver por bairro, e da tabela calendar_silver as colunas available como False, e date para o mês desejado. A quantidade de reservas encontradas para o filtro foi contada com count e registrada na tabela demanda_por_bairro do banco de dados gold na coluna respectiva do mês inserido no filtro em date. Foi criado um código separado para cada mês, sendo ajustado apenas o mês do filtro e a coluna na qual os dados seriam inseridos.
    * Foi filtrado a média de preço da coluna price por bairro da coluna neighbourhood_cleansed da tabela listings_silver do banco de dados silver_2 e os dados foram registrados na coluna media_preco no bairro correspondente na tabela demanda_por_bairro do banco de dados gold
    * Foi somado os valores da coluna number_of_reviews por bairro da coluna neighbourhood_cleansed da tabela listings_silver do banco de dados silver_2 e os dados foram registrados na coluna total_avaliacoes no bairro correspondente na tabela demanda_por_bairro do banco de dados gold
    * Foi feito a média das avaliações da coluna review_scores_rating por bairro da coluna neighbourhood_cleansed da tabela listings_silver do banco de dados silver_2 e os dados foram registrados na coluna media_avaliacoes no bairro correspondente na tabela demanda_por_bairro do banco de dados gold

4. Por ter sido criado uma nova tabela no banco de dados gold com dados filtrados do banco de dados silver_2, também foi criado uma validação para a tabela demanda_por_bairro do banco de dados gold.duckdb, em models/gold/validacao_gold.ipynb, por segurança. Não foram encontrados erros na validação.

5. Criação do arquivo models/gold/resumo_gold.ipynb com os dados pedidos na pergunta de mercado da seguinte forma:

    * Nome das colunas e sua tipagem
    * Todos os dados da tabela demanda_por_bairro
    * Filtro da tabela demanda_por_bairro dos bairros com maior demanda por mês e menor demanda por mês
    * Filtro da tabela demanda_por_bairro dos bairros com maior preço, menor preço, maior avaliação, menor avaliação

---
