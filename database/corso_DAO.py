from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

def get_corsi() -> list[Corso] | None:
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def get_iscritti_corso(codins) -> list[Studente] | None:
    cnx = get_connection()
    result = []
    query = """SELECT studente.* 
                FROM iscrizione, studente 
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (codins,))
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def get_corsi_studente(matricola) -> list[Corso]:
    cnx = get_connection()
    result = []
    query = """ SELECT corso.* 
    FROM corso, iscrizione 
    WHERE iscrizione.codins=corso.codins AND iscrizione.matricola = %s"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (matricola,))
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return result

def iscrivi_corso(matricola, codins) -> bool:
    cnx = get_connection()
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
