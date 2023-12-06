-- consultando dados do postresql
SELECT * 
FROM 
    OPENROWSET(
        BULK 'link do banco', -- /publicfinancialdata.txt
        FORMAT = 'CSV',
        FIELDTERMINATOR = ';',
        FIELDQUOTE = '"',
        FIRSTROW = 1,
        HEADER_ROW = TRUE,
        ROWTERMINATOR = '\n',
        PARSER_VERSION = '2.0'
    ) AS financas_paises;


-- consultando do mongo
SELECT *
FROM
    OPENROWSET(
        BULK 'link do banco', -- /educacaopaises.txt
        FORMAT = 'CSV',
        FIELDTERMINATOR = ',',
        FIELDQUOTE = '"',
        FIRSTROW = 1,
        HEADER_ROW = TRUE,
        ROWTERMINATOR = '\n',
        PARSER_VERSION = '2.0'
    ) AS educacao_paises;


-- com join
SELECT *
FROM 
    OPENROWSET(
        BULK 'link do banco', -- /publiceducationdata.txt
        FORMAT = 'CSV',
        FIELDTERMINATOR = ';',
        FIELDQUOTE = '"',
        FIRSTROW = 1,
        HEADER_ROW = TRUE,
        ROWTERMINATOR = '\n',
        PARSER_VERSION = '2.0'
    ) AS geral_paises
LEFT OUTER JOIN 
    OPENROWSET(
        BULK 'link do banco', -- /educacaopaises.txt
        FORMAT = 'CSV',
        FIELDTERMINATOR = ',',
        FIELDQUOTE = '"',
        FIRSTROW = 1,
        HEADER_ROW = TRUE,
        ROWTERMINATOR = '\n',
        PARSER_VERSION = '2.0'
    ) AS educacao_paises
ON geral_paises.country_name = educacao_paises.name;



