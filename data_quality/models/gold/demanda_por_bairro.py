import duckdb

# Caminho para o banco de dados DuckDB
db_path = 'D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\gold.duckdb'

# Conectar ao banco de dados
conn = duckdb.connect(database=db_path)

# Comando SQL para criar a tabela 'demanda_por_bairro'
create_table_query = """
CREATE TABLE IF NOT EXISTS demanda_por_bairro (
    bairro VARCHAR,                  -- Bairro é a coluna principal
    demanda_jan INTEGER,             -- Demanda de reservas para janeiro
    demanda_fev INTEGER,             -- Demanda de reservas para fevereiro
    demanda_mar INTEGER,             -- Demanda de reservas para março
    demanda_abr INTEGER,             -- Demanda de reservas para abril
    demanda_mai INTEGER,             -- Demanda de reservas para maio
    demanda_jun INTEGER,             -- Demanda de reservas para junho
    demanda_jul INTEGER,             -- Demanda de reservas para julho
    demanda_ago INTEGER,             -- Demanda de reservas para agosto
    demanda_set INTEGER,             -- Demanda de reservas para setembro
    demanda_out INTEGER,             -- Demanda de reservas para outubro
    demanda_nov INTEGER,             -- Demanda de reservas para novembro
    demanda_dez INTEGER,             -- Demanda de reservas para dezembro
    media_preco DOUBLE,              -- Média de preço do bairro
    quantidade_avaliacoes INTEGER,   -- Quantidade total de avaliações
    media_avaliacoes DOUBLE          -- Média das avaliações
);
"""

try:
    # Executar o comando SQL para criar a tabela
    conn.execute(create_table_query)
    print("Tabela 'demanda_por_bairro' criada com sucesso.")
except duckdb.Error as e:
    print("Erro ao criar a tabela:", e)
finally:
    # Fechar a conexão com o banco de dados
    conn.close()
