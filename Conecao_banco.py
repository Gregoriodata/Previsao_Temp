dados_conexao = (
    "Driver={SQL Server};"  # Drive do banco utilizado.
    "Server=DESKTOP-NQ82MK2;"  # CMD HOSTNAME
    "Database=PRE_TEMPO;"  # Nome do Banco de dados
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao com o banco realizada com sucesso")

cursor = conexao.cursor()
comando = f"""INSERT INTO PREV_TEMP(CIDADE,DATA,TEMP,DESCRI)
        VALUES('{icity}','{data}','{temp}','{descri}')"""

print(comando)
cursor.execute(comando)
cursor.commit()
print("Seus dados foram salvos com sucesso")
# VALUES('Brasilia','2020-01-29',14,'uaheueahueahuaehuae'
# VALUES('{icity},{data},{temp},{descri}--, DATA, TEMP, DESCRI
