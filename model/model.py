import database.corso_DAO
from database import corso_DAO
from database import studente_DAO


class Model:
    def getCorsi(self):
        return corso_DAO.getAllCorsi()

    def getIscritti(self, codins):
        return corso_DAO.getAllIscritti(codins)

    def getStudente(self, matricola):
        return studente_DAO.getAllStudenti(matricola)

    def getCorsoStudente(self, matricola):
        return corso_DAO.getCorsoStudente(matricola)

    def iscrivi_corso(self, matricola, codins):
        return corso_DAO.iscriviStudente(matricola, codins)