from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    #funzione per creare una lista con tutti gli strumenti del database
    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        conn = get_connection()           #creo una connessione
        strumenti = []                    #creo una lista vuota che conterrà gli strumenti del database
        if conn is not None:
            cursor = conn.cursor(dictionary=True)        #creo un cursore
            cursor.execute("SELECT * FROM strumento")    #eseguo la query per trovare tutti gli strumenti nel database
            for strumento in cursor:
                #riempo la lista creata precedentemente con tutti gli elementi presenti nel cursore
                strumenti.append(Strumento(strumento["codice"], strumento["tipo"], strumento["marca"],
                                           strumento["anno_acquisto"], strumento["valore"], strumento["disponibile"]))
            cursor.close()                #chiudo il cursore
            conn.close()                  #chiudo la connessione
            return strumenti              #ritorna la lista con tutti gli strumenti del database
        else:
            print("Impossibile connettersi")    #messaggio stampato nel caso in cui non sia stato possibile connettersi
            return None

    # funzione per creare una lista con tutti gli strumenti del tipo ricercato del database
    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        conn = get_connection()             #creo una connessione
        strumenti_per_tipo = []         #creo una lista vuota che conterrà gli strumenti del tipo ricercato del database
        if conn is not None:
            cursor = conn.cursor(dictionary=True)    #creo un cursore
            #eseguo la query per trovare tutti gli strumenti del tipo ricercato nel database
            cursor.execute("SELECT * FROM strumento WHERE tipo = %s", (tipo,))
            for strumento in cursor:
                #riempo la lista creata precedentemente con tutti gli elementi presenti nel cursore
                strumenti_per_tipo.append(Strumento(strumento["codice"], strumento["tipo"], strumento["marca"],
                                           strumento["anno_acquisto"], strumento["valore"], strumento["disponibile"]))
            cursor.close()           #chiudo il cursore
            conn.close()             #chiudo la connessione
            return strumenti_per_tipo       #ritorna la lista con tutti gli strumenti del tipo ricercato del database
        else:
            print("Impossibile connettersi")     #messaggio stampato nel caso in cui non sia stato possibile connettersi
            return None
