import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self._controller = None
        self.dd_corsi = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.lst_result = None
        self.load_interface()

    def load_interface(self):
        self._page.title = "App Gestione Studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.controls.append(ft.Text("App Gestione Studenti", size=30, color="blue"))

        # Dropdown per selezionare il corso
        self.dd_corsi = ft.Dropdown(label="Seleziona la lingua", width=600)
        self._page.controls.append(ft.Row([self.dd_corsi, ft.ElevatedButton(text="Cerca iscritti", on_click=lambda
            e: self._controller.search_iscritti())]))

        # Matricola, nome e cognome
        self.txt_matricola = ft.TextField(label="Matricola", width=150)
        self.txt_nome = ft.TextField(label="Nome", width=150, read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", width=150, read_only=True)
        self._page.controls.append(ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome]))

        self._page.controls.append(ft.Row(
            [ft.ElevatedButton(text="Cerca studente", on_click=lambda e: self._controller.search_studente()),
             ft.ElevatedButton(text="Cerca corsi", on_click=lambda e: self._controller.search_corsi_studente()),
             ft.ElevatedButton(text="Iscrivi", on_click=lambda e: self._controller.iscrivi_studente())]))

        # ListView per visualizzare i risultati
        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lst_result)

        self._page.update()

    def set_controller(self, controller):
        self._controller = controller
        self._controller.set_corso()

    def set_corso_options(self, corsi):
        self.dd_corsi.options = [ft.dropdown.Option(key=corso.codins, text=str(corso)) for corso in corsi]
        self.dd_corsi.update()

    def update_iscritti_list(self, iscritti):
        self.lst_result.controls.clear()
        if iscritti:
            for studente in iscritti:
                self.lst_result.controls.append(ft.Text(str(studente)))
        else:
            self.lst_result.controls.append(ft.Text("Nessun iscritto trovato."))
        self.lst_result.update()

    def update_studente_info(self, studente):
        self.txt_nome.value = studente.nome
        self.txt_cognome.value = studente.cognome
        self.update_page()

    def update_corsi_studente_list(self, corsi):
        self.lst_result.controls.clear()
        if corsi:
            for corso in corsi:
                self.lst_result.controls.append(ft.Text(str(corso)))
        else:
            self.lst_result.controls.append(ft.Text("Nessun corso trovato."))
        self.lst_result.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
