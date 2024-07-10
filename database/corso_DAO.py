# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


def getAllCorsi(): #questo metodo restituisce una lista di oggetti di tipo Corso
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query= """SELECT * FROM corso"""
        cursor.execute(query)
        for row in cursor:
            result.append(Corso(**row))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Error in DB connection")
        return None

def getAllIscritti(codins): #questo metodo restituisce una lista di oggetti di tipo Corso
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query= """SELECT studente.* 
                FROM iscrizione, studente 
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""

        cursor.execute(query, (codins,))
        for row in cursor:
            result.append(Studente(**row))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Error in DB connection")
        return None

def getCorsoStudente(matricola): #questo metodo restituisce una lista di oggetti di tipo Corso
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query= """SELECT corso.*
                FROM corso, iscrizione 
                WHERE iscrizione.codins=corso.codins AND iscrizione.matricola=%s"""

        cursor.execute(query, (matricola,))
        for row in cursor:
            result.append(Corso(**row))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Error in DB connection")
        return None

def iscriviStudente(matricola, codins): #questo metodo restituisce una lista di oggetti di tipo Corso
    cnx = get_connection()
    result = []
    query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
        (`matricola`, `codins`) 
        VALUES(%s,%s)
        """
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query, (matricola, codins,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        print("Could not connect")
        return False




