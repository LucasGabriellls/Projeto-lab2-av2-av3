from tkinter import messagebox


from Model.connect import create_connection


class DataBaseOrder:
    @staticmethod
    def insert_order(id, date_buy, status):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'insert into market_db.pedido (cliente_id, data_pedido, status) values (%s, %s, %s) RETURNING id_pedido;'
            cur.execute(query, [id, date_buy, status,])  
            conn.commit()
            return cur.fetchone()
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao inserir o pedido: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def order(amount, id_product, id_order):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'insert into market_db.detalhe_pedido (quantidade, produto_id, pedido_id) values (%s, %s, %s) RETURNING quantidade;'
            cur.execute(query, [amount, id_product, id_order,])  
            conn.commit()
            return cur.fetchone()
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao inserir o detalhe pedido: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    @staticmethod
    def list_id(id_order):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select pedido_id from market_db.detalhe_pedido WHERE pedido_id = %s;'
            cur.execute(query, [id_order])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao listar: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def quit(id_order):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = """
                    UPDATE market_db.pedido
                    SET status = 'cancelado'
                    WHERE id_pedido = %s;
                    """
            cur.execute(query, [id_order,])  
            conn.commit()
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao fazer o update: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def get_orders(orders):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = query = '''
                                SELECT 
                                    p.nome_produto, 
                                    dp.quantidade
                                FROM 
                                    market_db.detalhe_pedido dp
                                INNER JOIN 
                                    market_db.produto p ON dp.produto_id = p.id_produto
                                WHERE 
                                    dp.pedido_id = %s;
                            '''
            cur.execute(query, [orders])  
            result_select = cur.fetchall()  
            print(result_select)
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro na verificação de login: {e}')
            return None
        finally:
            conn.close()
            cur.close()
    
    @staticmethod
    def select_id_user(id):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = 'select cliente_id from market_db.pedido WHERE id_pedido = %s;'
            cur.execute(query, [id])  
            result_select = cur.fetchone()  
            return result_select
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao listar: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def order_payment(id, payment_method, status):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = '''UPDATE market_db.pedido
                    SET status = %s, 
                        metodo_pagamento = %s
                    WHERE id_pedido = %s
                    '''
            cur.execute(query, [status, payment_method, id])  
            conn.commit()
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro ao fazer update em pedido: {e}')
            return None
        finally:
            conn.close()
            cur.close()

    @staticmethod
    def delete_stock_db(id_prod, qndt):
        conn = create_connection()
        try:
            cur = conn.cursor()
            query = '''UPDATE market_db.produto
                        SET qnt_estoque = qnt_estoque - %s
                        WHERE id_produto = %s
                    '''
            cur.execute(query, [qndt, id_prod])  
            conn.commit()
        except Exception as e:
            messagebox.showerror('ERRO', f'Erro remover estoque: {e}')
            return None
        finally:
            conn.close()
            cur.close()