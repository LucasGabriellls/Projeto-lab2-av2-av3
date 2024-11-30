create table cliente(
	id_cliente serial primary key,
	nome_cliente varchar(70) not null,
	endereco varchar(250),
	pais varchar(80),
	senha bytea not null unique,
	codigo_postal varchar(100),
	email_cliente VARCHAR(250) not null unique,
	telefone VARCHAR(30),
	cpf varchar(11) unique
);

create table pedido(
	id_pedido serial primary key,
	cliente_id int references cliente(id_cliente),
	data_pedido date,
	status varchar(50) NOT NULL,
	metodo_pagamento varchar(150)
);


create table detalhe_pedido(
	id_detalhe_pedido serial primary key,
	quantidade smallint not null,
	produto_id int references produto(id_produto),
	pedido_id int references pedido(id_pedido)
);

create table produto(
	id_produto serial primary key,
	nome_produto varchar(250) not null,
	qnt_estoque smallint default 0,
	preco decimal(10, 2) check(preco > 0) not null,
	categoria_id int references categoria(id_categoria),
	descricao varchar(5000) 
);

create table categoria(
	id_categoria serial primary key,
	nome_categoria varchar(250) not null,
);
