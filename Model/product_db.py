from Model.connect import create_connection
from tkinter import messagebox


class DataBaseProduct:
    def select_category():
        conn = create_connection()
        try:
            cur = conn.cursor()
            cur.execute('SELECT nome_categoria FROM market_db.categoria;')
            result_select = cur.fetchall()
            return result_select  
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na consulta: {e}')
            return None
        finally:
            cur.close()
            conn.close()
        
    def add_product(name, stock, price_p, category_id_p, description_c):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'insert into market_db.produto (nome_produto, qnt_estoque, preco, categoria_id, descricao) values (%s, %s, %s, %s, %s);'
            cur.execute(query, [name, stock, price_p, category_id_p, description_c,])  
            conn.commit() 
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao inserir o produto: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def add_category(category_c):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'insert into market_db.categoria (nome_categoria) values (%s);'
            cur.execute(query, [category_c,])  
            conn.commit() 
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao inserir a categoria: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def search_id_category(category):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select id_categoria from market_db.categoria WHERE nome_categoria = %s;'
            cur.execute(query, [category,])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro procura do id_categoria: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    def equal_category(name_category):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select nome_categoria from market_db.categoria WHERE nome_categoria ilike %s;'
            cur.execute(query, [name_category,])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro procura do id_categoria: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    
    def search_product():
        conn = create_connection()
        try:
            cur = conn.cursor()
            cur.execute('select nome_produto from market_db.produto;')  
            result_select = cur.fetchall()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na procura do produto.')
            return None
        finally:
            conn.close()
            cur.close()
    
    def select_product_all():
        conn = create_connection()
        try:
            cur = conn.cursor()
            cur.execute('select * from market_db.produto;')  
            result_select = cur.fetchall()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na procura do produto.')
            return None
        finally:
            conn.close()
            cur.close()
    
    def id_product_search(id_product):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select id_produto from market_db.produto WHERE id_produto = %s;'
            cur.execute(query, [id_product,])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro procura do id_categoria: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    def remove_product(id_product):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'delete from market_db.produto where id_produto = %s;'
            cur.execute(query, [id_product,])  
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao excluir produto: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    def edit_product(id_product, name_product, stock_product, price_product, description_product):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = '''
            UPDATE market_db.produto
            SET nome_produto = %s, qnt_estoque = %s, preco = %s, descricao = %s
            WHERE id_produto = %s;
            '''
            cur.execute(query, [name_product, stock_product, price_product, description_product, id_product])  
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao excluir produto: {e}')
            return None
        finally:
            conn.close()
            cur.close()