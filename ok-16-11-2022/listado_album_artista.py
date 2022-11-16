import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='disqueria',
                                         user='root',
                                         password='mariano')

  # mySql_query = "describe productos"
  # mySql_query = "select * from productos"
    mySql_query = "SELECT * FROM album a, interprete e WHERE a.id_interprete=e.id_interprete order by a.nombre asc"
  #  mySql_query = "select count(*) from productos"

    cursor = connection.cursor()
    cursor.execute(mySql_query)
   
    rows=cursor.fetchall()
    for row in rows:
    	print(row)

   
    cursor.close()


finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
