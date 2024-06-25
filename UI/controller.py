import flet as ft
from model.model import Model
from model.corso import Corso
from model.studente import Studente

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._view.set_controller(self)

    def set_corso(self):
        self._view.set_corso_options(self._model.get_corsi())

    def search_iscritti(self):
        corso = self._view.dd_corsi.value
        if corso:
            iscritti = self._model.get_iscritti_corso(corso)
            self._view.update_iscritti_list(iscritti)
        else:
            self._view.create_alert("Selezionare un corso!")

    def search_studente(self):
        matricola = self._view.txt_matricola.value
        if matricola:
            studente = self._model.cerca_studente(matricola)
            if studente:
                self._view.update_studente_info(studente)
            else:
                self._view.create_alert("Studente non trovato!")
        else:
            self._view.create_alert("Inserire una matricola!")

    def search_corsi_studente(self):
        matricola = self._view.txt_matricola.value
        if matricola:
            corsi = self._model.get_corsi_studente(matricola)
            if corsi:
                self._view.update_corsi_studente_list(corsi)
            else:
                self._view.create_alert("Studente non iscritto a nessun corso!")
        else:
            self._view.create_alert("Inserire una matricola!")

    def iscrivi_studente(self):
        matricola = self._view.txt_matricola.value
        corso = self._view.dd_corsi.value
        if matricola and corso:
            success = self._model.iscrivi_corso(matricola, corso)
            if success:
                self._view.create_alert("Studente iscritto con successo!")
            else:
                self._view.create_alert("Errore nell'iscrizione!")
        else:
            self._view.create_alert("Inserire matricola e selezionare un corso!")
