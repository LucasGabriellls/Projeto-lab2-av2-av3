import psycopg2
from tkinter import messagebox

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
            messagebox.showerror('ERRO', f'Erro: {e}')
            return None