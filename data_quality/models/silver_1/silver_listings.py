import duckdb
import pyarrow as pa

bronze_db_path = "D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\bronze.duckdb"

silver_db_path = "D:\\GitHub\\projeto_Analytics_Engineering\\data_quality\\silver_1.duckdb"

# Definir o tamanho do lote
BATCH_SIZE = 1000

try:
    # Conectar ao banco de dados bronze e extrair os dados como um PyArrow Table
    bronze_conn = duckdb.connect(database=bronze_db_path)
    query = "SELECT * FROM listings;"
    data_arrow = bronze_conn.execute(query).arrow()
    bronze_conn.close()
    print("Dados extraídos com sucesso do banco bronze como PyArrow Table.")

    # Conectar ao banco de dados silver_1
    silver_conn = duckdb.connect(database=silver_db_path)
    silver_conn.execute("PRAGMA disable_object_cache")

    # Inserir os dados em lotes na tabela 'listings'
    for i in range(0, data_arrow.num_rows, BATCH_SIZE):
        # Extrair um lote dos dados
        batch = data_arrow.slice(i, BATCH_SIZE)
        
        # Registrar o lote temporariamente e inserir na tabela
        silver_conn.register("batch_data", batch)
        insert_query = "INSERT INTO listings SELECT * FROM batch_data;"
        silver_conn.execute(insert_query)
        
        print(f"Lote {i // BATCH_SIZE + 1} inserido com sucesso.")

    print("Todos os dados foram inseridos com sucesso na tabela 'listings' do banco silver_1.")

except duckdb.Error as e:
    print("Ocorreu um erro ao acessar o banco de dados:", e)

except Exception as e:
    print("Ocorreu um erro inesperado:", e)

finally:
    # Fechar a conexão
    try:
        silver_conn.close()
    except:
        pass