import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='disqueria',
                                         user='root',
                                         password='mariano')

    mySql_insert_query = """INSERT INTO album (id_album, cod_album, nombre, id_interprete,id_genero, cant_temas, id_discografica, id_formato,fec_lanzamiento, precio, cantidad,caratula) 
                           VALUES 
                           (null, 2625,'albumnuevo', 1, 1, 10,1,1,'2022-11-11',150,11,'caratula') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into album table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into categoria table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
