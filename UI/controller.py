import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._id_map_corsi = {}
        self.corso_selezionato = None

    def populate_dd_corso(self):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        for corso in self._model.getCorsi(): # itero la lista di oggetti di tipo Corso
            self._id_map_corsi[corso.codins] = corso # aggiungo l'oggetto corso alla mappa usando come chiave
                                                        # il codins (ordinati per la chiave)
            self._view.dd_corsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()

    def trovaIscritti(self, e):
        if self.corso_selezionato is None:
            self._view.create_alert("Selezionare un corso")
            return
        iscritti = self._model.getIscritti(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problemi nella connessione")
            return
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessun iscritto a questo corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti a questo corso"))
            for s in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{s}"))
        self._view.update_page()

    def leggi_corso(self, e):
        self.corso_selezionato =self._view.dd_corsi.value


    def cerca_studente(self, e):
        matricola = self._view.txt_matricola.value
        if matricola =="":
            self._view.create_alert("Inserire una matricola")
            return
        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel DB")
        else:
            self._view.txt_nome.value = f"{studente.nome}"
            self._view.txt_cognome.value = f"{studente.cognome}"
        self._view.update_page()


    def cerca_corsi(self, e):
        matricola = self._view.txt_matricola.value
        if matricola =="":
            self._view.create_alert("Inserire una matricola")
            return
        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel DB")
        else:
            corsi = self._model.getCorsoStudente(studente.matricola)
            if len(corsi) == 0:
                self._view.create_alert("La matricola non risulta iscritta a nessun corso")
                return
            else:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"Lo studente è iscritto ai seguenti corsi:"))
                for c in corsi:
                    self._view.txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()


    def iscrivi(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        codice_corso = self._view.dd_corsi.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        result = self._model.iscrivi_corso(matricola, codice_corso)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()





