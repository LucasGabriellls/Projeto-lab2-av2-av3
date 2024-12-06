# Super Kernel - Sistema de Gerenciamento de Mercado

## Descrição

O **Super Kernel** é um sistema de gerenciamento de mercado desenvolvido em Python, utilizando a biblioteca Tkinter para criar a interface gráfica. O sistema possui funcionalidades completas de gerenciamento de mercado, como login, cadastro de clientes e produtos, compras e pagamentos. 

A parte administrativa permite a gestão de clientes e produtos, com opções para listar, editar, adicionar e remover itens. Toda a estrutura foi projetada com a arquitetura **MVC (Model-View-Controller)**, que separa eficientemente os dados, a lógica de negócios e a interface. O sistema utiliza o **PostgreSQL** como banco de dados, garantindo robustez e confiabilidade.

## Funcionalidades

- **Login e Cadastro de Usuários**
  - Sistema de login para clientes e administradores.
  - Cadastro de novos clientes.
  
- **Gerenciamento de Produtos**
  - Admin pode adicionar, editar e remover produtos.
  - Listagem de produtos com detalhes como preço, descrição e quantidade em estoque.

- **Compras e Pagamentos**
  - Sistema de compras para os clientes, com opções de pagamento.
  - Registro e controle de transações realizadas.

- **Área Administrativa**
  - Administração completa para editar, listar e remover produtos e clientes.
  - Acesso exclusivo para usuários com permissão de administrador.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para criação da interface gráfica.
- **PostgreSQL**: Banco de dados para armazenar informações de clientes, produtos e transações.
- **MVC (Model-View-Controller)**: Arquitetura adotada para separar a lógica de negócios, dados e interface.

## Bibliotecas Utilizadas

- `bcrypt==4.2.0` – Para criptografia de senhas e autenticação segura.
- `colorama==0.4.6` – Para adicionar cores e estilo ao terminal.
- `pillow==11.0.0` – Para manipulação de imagens (ex: gerar QR codes).
- `psycopg2==2.9.10` – Conector do PostgreSQL com Python.
- `pyotp==2.9.0` – Para autenticação de dois fatores (2FA).
- `qrcode==8.0` – Para geração de QR codes.

## Instalação

### Requisitos

- Python 3.12.6 
- PostgreSQL
- Bibliotecas Python:
  - `tkinter` (já incluída no Python)
  - `psycopg2`
  - `bcrypt`
  - `colorama`
  - `pillow`
  - `pyotp`
  - `qrcode`

### Passos para instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/LucasGabriellls/Projeto-lab2-av2-av3.git
   cd Projeto-lab2-av2-av3
