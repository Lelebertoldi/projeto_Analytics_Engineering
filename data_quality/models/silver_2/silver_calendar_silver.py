import duckdb

# Variável para o caminho do banco de dados DuckDB
db_path = 'D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\silver_2.duckdb'

# Conectar ao banco de dados DuckDB
conn = duckdb.connect(database=db_path)

# Comando SQL para criar a tabela calendar_silver
create_table_query = """
CREATE TABLE IF NOT EXISTS calendar_silver (
    listing_id BIGINT,
    date TIMESTAMP,
    available BOOLEAN
);
"""

# Executar o comando para criar a tabela
conn.execute(create_table_query)
print("Tabela 'calendar_silver' criada com sucesso.")

# Fechar a conexão
conn.close()
