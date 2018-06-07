#!/python3
import mysql.connector
import time


def mySQL_QUERY():
    #mySQL configuration parameters
    config = {
     'user': 'root',
     'password': 'hilo',
     'host': '192.168.84.56',
     'database': 'spotdyna',
     'raise_on_warnings': True,
     'use_pure': False,
     'port': 3306
    }
    print("Establish connection with mysql BBDD")
    #Connect with mySQL server
    print("connecting")
    try: 
        cnx = mysql.connector.connect(**config)
        print("conected :)")
        time.sleep(2)

        #Buffer cursor
        curA = cnx.cursor(buffered=True)

        #Configure query
        #query = ("select * FROM mxr_patrones_terminal WHERE COD_TERMINAL = 1426959; ")
        query = ("SELECT * FROM acciones WHERE id_accion=126; ")
        print("Test query")
        print (query)

        #Launch query
        curA.execute(query)
        for row in curA:
            print("Retrived values from BBDD")
            print(row)
        
        #Clossing connection
        print("Disconnecting")
        curA.close()
        cnx.close()
        return True

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return False



