from tkinter import messagebox
from Model.connect import create_connection

class DataBaseUser:

    def record_list_user(email):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'SELECT email_cliente FROM market_db.cliente WHERE email_cliente = %s;'
            cur.execute(query, [email])
            result_select = cur.fetchone()
            return result_select  
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na consulta: {e}')
            return None
        finally:
            cur.close()
            conn.close()

    def login_list_user(email):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select email_cliente, senha from market_db.cliente WHERE email_cliente = %s;'
            cur.execute(query, [email])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    def insert_user(name, email, password):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'insert into market_db.cliente (nome_cliente, email_cliente, senha) values (%s, %s, %s);'
            cur.execute(query, [name, email, password,])  
            conn.commit() 
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao inserir o usuario: {e}')
            return None
        finally:
            conn.close()
            cur.close()