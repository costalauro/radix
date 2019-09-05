create table vendedor (
vendedor_id	integer,
vendedor_nome varchar(64)
);

create table venda (
venda_id	integer,
vendedor_id	integer,
venda_data	DATETIME,
venda_valor	float
);

INSERT INTO vendedor VALUES
(2, 'Michael'),
(3, 'Linda'),
(4, 'Jillian'),
(5, 'Garrett');

INSERT INTO venda VALUES
(2,2, '20160618 10:34:09 AM',1.700),
(3,2, '20160618 10:34:09 AM',11.500),
(4,5, '20160618 10:34:09 AM',22.900),
(5,3, '20160618 10:34:09 AM',27.800),
(6,2, '20160618 10:34:09 AM',1.700),
(7,2, '20160618 10:34:09 AM',10.500),
(8,5, '20160618 10:34:09 AM',10.900),
(9,3, '20160618 10:34:09 AM',18.800),
(10,4, '20170618 10:34:09 AM',12.800);

SELECT * FROM (  
SELECT ROW_NUMBER() OVER (ORDER BY venda_valor DESC) AS v2.vendedor_nome,v1.venda_valor  
FROM venda as v1
       INNER JOIN vendedor as v2
       ON v2.vendedor_id = v1.vendedor_id 
where year(venda_data) = 2016)  
AS foo  
       
--Liste	os	valores	mais	altos	de	venda	por	vendedor	para	o	ano	de	2016.	Não	utilize	as	
--funções	Min/Ma