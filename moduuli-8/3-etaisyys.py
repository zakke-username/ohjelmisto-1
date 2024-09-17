from geopy import distance
import mysql.connector


icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)
sql = f"select latitude_deg, longitude_deg from airport where (ident = '{icao1}') or (ident = '{icao2}')"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

dist = round(distance.distance(result[0], result[1]).km)
print(f"Etäisyys: {dist} km")
