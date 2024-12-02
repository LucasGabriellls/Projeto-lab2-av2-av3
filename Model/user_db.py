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
            query = 'select senha from market_db.cliente WHERE email_cliente = %s;'
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
            messagebox.showerror('ERRO', f'Erro ao inserir o usuario.')
            return None
        finally:
            conn.close()
            cur.close()
    
    def select_user():
        conn = create_connection()
        try:
            cur = conn.cursor()
            cur.execute('select id_cliente from market_db.cliente;')  
            result_select = cur.fetchall()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao selecionar os usuários.')
            return None
        finally:
            conn.close()
            cur.close()

    def get_id(email):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select id_cliente from market_db.cliente WHERE email_cliente = %s;'
            cur.execute(query, [email])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    def remove_user(id):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'DELETE FROM market_db.cliente WHERE id_cliente = %s;'
            cur.execute(query, [id])  
            conn.commit()
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def valid_id(id):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select id_cliente from market_db.cliente WHERE id_cliente = %s;'
            cur.execute(query, [id])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def get_user():
        conn = create_connection()
        try:
            cur = conn.cursor()
            cur.execute('select id_cliente, nome_cliente, email_cliente from market_db.cliente;')  
            result_select = cur.fetchall()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    def  edit_user(name, address, nation, email, id):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = '''
            UPDATE market_db.cliente
            SET nome_cliente = %s, endereco = %s, pais = %s, email_cliente = %s
            WHERE id_cliente = %s;
            '''
            cur.execute(query, [name, address, nation, email, id])  
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao excluir produto: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def update_user(id, address, nation, cep, phone, cpf):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = """
                    UPDATE market_db.cliente
                    SET
                        endereco = %s,
                        pais = %s,
                        codigo_postal = %s,
                        telefone = %s,
                        cpf = %s
                    WHERE id_cliente = %s;
                    """
            cur.execute(query, [address, nation, cep, phone, cpf,id])  
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao excluir produto: {e}')
            return None
        finally:
            conn.close()
            cur.close()