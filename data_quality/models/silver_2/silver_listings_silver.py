import duckdb

# Variável para o caminho do banco de dados DuckDB
db_path = 'D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\silver_2.duckdb'

# Conectar ao banco de dados DuckDB
conn = duckdb.connect(database=db_path)

# Comando SQL para criar a tabela listings_silver
create_table_query = """
CREATE TABLE IF NOT EXISTS listings_silver (
    id INTEGER,
    neighbourhood_cleansed VARCHAR,
    price DOUBLE,
    number_of_reviews INTEGER,
    review_scores_rating DOUBLE
);
"""

# Executar o comando para criar a tabela
conn.execute(create_table_query)
print("Tabela 'listings_silver' criada com sucesso.")

# Fechar a conexão
conn.close()
