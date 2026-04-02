import sqlite3
#Arquitetura da base de dados para intersecção com python:
#Criar banco de dados
conexao=sqlite3.connect('Banco_dados')
#Apontar para o banco de dados
cursor=conexao.cursor()
#Criar tabela:
cursor.execute(
    'CREATE TABLE Tabela_teste(Data text, Nome text, Idade real)'
) #execute faz açoes na tabela
conexao.commit() #salva permanentemente a tabela no banco de dados
#Inserir valores na tabela
cursor.execute("INSERT INTO Tabela_teste VALUES('1/1/2021','Odemir','30')")
cursor.execute("INSERT INTO Tabela_teste VALUES('2/5/2021','Lucas','23')")
#importar números aleatórios
import random
#Criar loop para rodar o comando 10 vezes
for loop in range(10):
#gerando número aleatório
    numero=random.randint(10,20)
    #inserir na tabela usando f = print formatado
    cursor.execute(f"INSERT INTO Tabela_teste VALUES('2/5/2021','Lucas',{numero})")

#query de consulta
cursor.execute("SELECT * FROM Tabela_teste")
resultados = cursor.fetchall() #busca os dados
print(resultados)
#ou
resultados = cursor.execute("SELECT * FROM Tabela_teste").fetchall()
print(resultados)

#query de consulta - colunas específicas
resultados = cursor.execute("SELECT Nome, Idade FROM Tabela_teste").fetchall()
#criar loop para printar cada linha da lista resultados
for linha in resultados:
    print(linha)

#query com =
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome = 'Odemir'
    '''
).fetchall()
print(resultados)
#query com >
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade > 25
    '''
).fetchall()
print(resultados)

#query com <
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade < 25
    '''
).fetchall()
print(resultados)

#query com <=
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade <= 15
    '''
).fetchall()
print(resultados)

#query com <> (diferente)
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome <> 'Odemir'
    '''
).fetchall()
for linha in resultados:
    print(linha)    

#query com BETWEEN
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade BETWEEN 15 AND 20
    '''
).fetchall()
for linha in resultados:
    print(linha)    

#query com LIKE - encontrar nomes que começam com letra L
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome LIKE 'L%'
    '''
).fetchall()
for linha in resultados:
    print(linha)    
#encontrar nomes que terminam com letra r
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome LIKE '%R'
    '''
).fetchall()
for linha in resultados:
    print(linha)  
#encontrar nomes que possuem uca em qualquer posição
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome LIKE '%UCA%'
    '''
).fetchall()
for linha in resultados:
    print(linha)  
#encontrar nomes que possuem d na segunda posição
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome LIKE '_D%'
    '''
).fetchall()
for linha in resultados:
    print(linha)  
#encontrar nomes que começam com O e tem pelo menos 3 caracteres
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome LIKE 'O__%'
    '''
).fetchall()
for linha in resultados:
    print(linha) 
#encontrar nomes que começam com O e terminam com r
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome LIKE 'O%R'
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#query com IN
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade IN (14,16,30)
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#query com AND
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome = 'Lucas' AND Idade < 20
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#query com OR
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade = 15 OR Nome = 'Odemir'
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#query com NOT 
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE NOT Nome = 'Lucas'
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#combinando operadores
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Nome = 'Lucas' AND (Idade > 12 OR Idade < 20) AND NOT Idade = 18
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#query com ORDER BY - descendente
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    ORDER BY Idade DESC
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#NULL
#inserindo valor null
cursor.execute("INSERT INTO Tabela_teste VALUES ('12/07/2022','Cauan', NULL)")
#consultando valores null
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade IS NULL
    '''
).fetchall()
for linha in resultados:
    print(linha) 
#filtrando valores nulos da tabela
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade IS NOT NULL
    '''
).fetchall()
for linha in resultados:
    print(linha) 
#verificando outros valores
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    WHERE Idade > 25 AND Idade IS NOT NULL
    '''
).fetchall()
for linha in resultados:
    print(linha) 

#UPDATE
cursor.execute(
    '''
    UPDATE Tabela_teste 
    SET Idade = 19
    WHERE Idade IS NULL
    '''
).fetchall()
for linha in resultados:
    print(linha)

#DELETE
cursor.execute(
    '''
    DELETE FROM Tabela_teste 
    WHERE Nome = 'Lucas' AND Idade = 19
    '''
).fetchall()
for linha in resultados:
    print(linha)

#SELECT TOP N - selecionar os n primeiros registros em sistemas microsoft
#cursor.execute(
   # '''
    #SELECT TOP 5 FROM Tabela_teste 
    #'''
#).fetchall()
#for linha in resultados:
    #print(linha)

#LIMIT - selecionar os n primeiros registros em sistemas sqlite
cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    LIMIT 5
    '''
).fetchall()
for linha in resultados:
    print(linha)
#SELECIONAR A PARTIR DA N-ÉSIMA LINHA - OFFSET
cursor.execute(
    '''
    SELECT * FROM Tabela_teste 
    LIMIT 5 OFFSET 2
    '''
).fetchall()
for linha in resultados:
    print(linha)
#MIN E MAX
cursor.execute(
    '''
    SELECT MAX(Idade), MIN(Idade) FROM Tabela_teste 
    '''
).fetchall()
for linha in resultados:
    print(linha)

#COUNT - contar quantos registros existem na tabela
cursor.execute(
    '''
    SELECT COUNT(Idade) FROM Tabela_teste 
    '''
).fetchall()
for linha in resultados:
    print(linha)
#AVG - média
cursor.execute(
    '''
    SELECT AVG(Idade) FROM Tabela_teste 
    '''
).fetchall()
for linha in resultados:
    print(linha)
#SUM - soma
cursor.execute(
    '''
    SELECT SUM(Idade) FROM Tabela_teste 
    '''
).fetchall()
for linha in resultados:
    print(linha)

#ALIAS (AS)- renomear colunas temporariamente
cursor.execute(
    '''
    SELECT Idade AS Idade_Usuario, Nome AS Nome_Usuario FROM Tabela_teste
    '''
).fetchall()
for linha in resultados:
    print(linha)

#JOIN - unir tabelas
#INNER JOIN - retorna apenas os registros que possuem correspondência em ambas as tabelas
#LEFT JOIN - retorna todos os registros da tabela da esquerda e os correspondentes da tabela da direita
#RIGHT JOIN - retorna todos os registros da tabela da direita e os correspondentes da tabela da esquerda- nao suportado no sqlite
#FULL JOIN - retorna todos os registros quando há uma correspondência em uma das tabelas - nao suportado sqlite

#criar novas tabela pra exemplo prático
#tabela de informações sobre vendas: id do vendedor e valor da venda
cursor.execute(
    '''
    CREATE TABLE Tabela_vendas (id real, valor real)
    '''
).fetchall()
for linha in resultados:
    print(linha)
conexao.commit() 
#tabela de informações sobre vendedores: id do vendedor e nome
cursor.execute(
    '''
    CREATE TABLE Tabela_vendedores (id real, nome text)
    '''
).fetchall()
for linha in resultados:
    print(linha)
conexao.commit()
#inserir dados nas tabelas
cursor.execute("INSERT INTO Tabela_vendas VALUES (1, 100), (1, 150), (1,200),(2, 450), (2,600), (2,900)")
cursor.execute("INSERT INTO Tabela_vendedores VALUES (1, 'Odemir'), (2, 'Lucas')")
#unir tabela vendas com vendedores usando INNER JOIN; o ON define a coluna em comum no formato tabela1.coluna = tabela2.coluna
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_vendas
    INNER JOIN Tabela_vendedores
    ON Tabela_vendas.id = Tabela_vendedores.id
    '''
).fetchall()
for linha in resultados:
    print(linha)

#LEFT JOIN
#inserir novo dado na tabela vendas
cursor.execute("INSERT INTO Tabela_vendas VALUES (3, 856)")
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_vendas
    LEFT JOIN Tabela_vendedores
    ON Tabela_vendas.id = Tabela_vendedores.id
    '''
).fetchall()
for linha in resultados:
    print(linha)

#UNION - combinar resultados de duas ou mais consultas SELECT em um único conjunto de resultados
#criando duas novas tabelas
cursor.execute("CREATE TABLE Tabela_X (id real, nome text)")
conexao.commit()
cursor.execute("CREATE TABLE Tabela_Y (id real, nome text)")
conexao.commit()
#inserir dados nas tabelas
cursor.execute("INSERT INTO Tabela_X VALUES (1, 'Odemir'), (2, 'Maria'), (3, 'João')")
cursor.execute("INSERT INTO Tabela_Y VALUES (1, 'Mario'), (2, 'Luigi'), (3, 'Peach')")
#combinar resultados usando UNION
resultados=cursor.execute(
    '''
    SELECT * FROM Tabela_X
    UNION ALL
    SELECT * FROM Tabela_Y
    '''
).fetchall()
for linha in resultados:
    print(linha)

#GROUP BY - agrupar resultados com base em uma ou mais colunas
resultados=cursor.execute(
    '''
SELECT SUM (idade) FROM Tabela_teste
GROUP BY Nome
'''
).fetchall()
for linha in resultados:
    print(linha)