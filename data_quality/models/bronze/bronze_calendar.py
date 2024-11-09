import duckdb

# Caminho completo do arquivo CSV
arquivo = "D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\seeds\\calendar.csv"

# Nome da tabela no DuckDB
nome = "calendar"

try:
    # Conectar ao banco de dados DuckDB
    con = duckdb.connect(database='D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\bronze.duckdb', read_only=False)
    print("Conexão com o DuckDB estabelecida com sucesso.")

# Criar a tabela caso ela não exista e tranfere o CSV
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {nome} AS
    SELECT * FROM read_csv_auto('{arquivo}');
    """ # Cria a tabela ou ignora se já existir
    con.execute(create_table_query)  
    print(f"Tabela '{nome}' criada ou já existente.")

    #query para carregar o CSV para a tabela 
    query = f"""
    COPY {nome} FROM '{arquivo}' (DELIMITER ',', HEADER TRUE);
    """
    con.execute(query)  # Executa o comando SQL para carregar o CSV

    print(f"Dados do arquivo '{arquivo}' carregados com sucesso na tabela {nome}.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Um erro ocorreu: {e}")

finally:
    # Fechar a conexão com o banco de dados
    try:
        con.close()
        print("Conexão com o DuckDB fechada.")
    except Exception as e:
        print(f"Erro ao fechar a conexão com o DuckDB: {e}")