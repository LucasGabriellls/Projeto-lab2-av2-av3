import psycopg2

class DataBase:
    def create_connection():
        try:
            conn = psycopg2.connect(
                dbname = 'postgres',
                user = 'postgres',
                password = 'post',
                host = 'localhost',
                port = '5432'
            )
            return conn
        except Exception as e:
            print(f'Erro: {e}')
            return None
            
    def list_user():
        conn = DataBase.create_connection()
        try:
            cur = conn.cursor()
            cur.execute('select * from cliente')
            result = cur.fetchall       
            return result
        except Exception as e:
            print(f'Erro: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    def record_list_user(email):
        conn = DataBase.create_connection()
        try:
            cur = conn.cursor()
            query = 'SELECT email_cliente FROM market_db.cliente WHERE email_cliente = %s;'
            cur.execute(query, [email])
            result_select = cur.fetchone()
            return result_select  # Retorna None se não encontrar
        except Exception as e:
            print(f"Erro na consulta: {e}")
            return None
        finally:
            cur.close()
            conn.close()

    def login_list_user(email):
        conn = DataBase.create_connection()
        try:
            cur = conn.cursor()
            query = 'select email_cliente, senha from market_db.cliente WHERE email_cliente = %s;'
            cur.execute(query, [email])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            print(f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def insert_user(name, email, password):
        conn = DataBase.create_connection()
        try:
            cur = conn.cursor()
            query = 'insert into market_db.cliente (nome_cliente, email_cliente, senha) values (%s, %s, %s);'
            cur.execute(query, [name, email, password,])  
            conn.commit() 
        except Exception as e:
            print(f'Erro ao inserir o usuario: {e}')
            return None
        finally:
            conn.close()
            cur.close()