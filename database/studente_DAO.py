from database.DB_connect import get_connection
from model.studente import Studente

def cerca_studente(matricola) -> Studente | None:
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM studente WHERE matricola = %s"
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        if row:
            return Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        else:
            return None
    else:
        print("Could not connect")
        return None
