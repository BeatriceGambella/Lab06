import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    #funzione che quando viene chiamata mi restituisce tutti gli strumenti del deposito
    def mostra_strumenti(self, e):
        #svuoto la lista degli strumenti del deposito da visualizzare nell'interfaccia
        self._view.lista_strumenti.controls.clear()
        #riempo una nuova lista con tutti gli strumenti del detabase chiamando la funzione nella sezione model
        lista_strumenti = self._model.get_strumenti()
        if lista_strumenti is not None:
            if len(lista_strumenti) > 0:                  #controllo che ci siano degli strumenti
                for strumento in lista_strumenti:
                    stato = "✅" if strumento.disponibile else "⛔"      #in base alla disponibilità assegno un simbolo
                    #riempo la lista da visualizzare nell'interfaccia
                    self._view.lista_strumenti.controls.append(ft.Text(f"{stato} {strumento}"))
                self._view.update()                        #aggiorno l'interfaccia
            else:
                #messaggio stampato nel caso non ci siano strumenti
                self._view.show_alert("❌ Non ci sono strumenti nel database")
        else:
            #messaggio stampato nel caso in cui non è stato possibile connettersi
            self._view.show_alert("❌ Impossibile connettersi al database")

    #funzione che quando viene chiamata mi restituisce tutti gli strumenti del deposito del tipo ricercato
    def cerca_strumenti(self, e):
        #svuoto la lista degli strumenti di un tipo ricercato da visualizzare nell'interfaccia
        self._view.lista_strumenti_ricerca.controls.clear()
        # aggiorna la pagina con la lista svuotata, così nel caso ci siano errori successivi non viene visualizzato nessuno strumento
        self._view.update()
        #riempo una nuova lista con gli strumenti del tipo ricercato del detabase chiamando la funzione nella sezione model
        strumenti_ricercati = self._model.cerca_strumenti_per_tipo(self._view.input_tipo_strumento.value)
        if strumenti_ricercati is not None:
            if len(strumenti_ricercati) > 0:                #controllo che ci siano degli strumenti
                for strumento in strumenti_ricercati:
                    stato = "✅" if strumento.disponibile else "⛔"      #in base alla disponibilità assegno un simbolo
                    # riempo la lista da visualizzare nell'interfaccia
                    self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"{stato} {strumento}"))
                self._view.update()             #aggiorno l'interfaccia
            else:
                #messaggio stampato nel caso non ci siano strumenti
                self._view.show_alert("❌ Non ci sono strumenti di questo tipo nel database")
        else:
            #messaggio stampato nel caso in cui non è stato possibile connettersi
            self._view.show_alert("❌ Impossibile connettersi al database")