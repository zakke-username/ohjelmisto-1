import mysql.connector

iso_country = input("Anna maakoodi: ").upper()

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)
sql = f"select type, count(*) from airport where iso_country = '{iso_country}' group by type"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

for row in result:
    print(row)
