import mysql.connector

icao = input("Anna lentokentän ICAO-koodi: ")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)
sql = f"select name, iso_region from airport where ident = '{icao}'"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

print(result[0])
