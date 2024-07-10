# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.studente import Studente


def getAllStudenti(matricola):  # questo metodo restituisce un oggetto di tipo Studente
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente
                    WHERE matricola = %s"""
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        if row is not None:
            result= (Studente(**row))
        else:
            result = None
        cursor.close()
        cnx.close()
        return result
    else:
        print("Error in DB connection")
        return None



