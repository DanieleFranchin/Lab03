from logging import raiseExceptions

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.deposito = []
        self.lista_prestiti = []
        self.lista_id = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r") as f:
            for line in f:
                oggetto = {}
                linea = line.strip("\n").split(",")
                oggetto["codice"] = linea[0]
                oggetto["tipo"] = linea[1]
                oggetto["marca"] = linea[2]
                oggetto["anno acquisto"] = linea[3]
                oggetto["valore"] = linea[4]
                self.deposito.append(oggetto)
        return self.deposito

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if self.deposito is None:
            print("Prima carica il file")
        else:
            aggiunta = {
                "codice": f"S{len(self.deposito) + 1}",
                "tipo": tipo,
                "marca": marca,
                "anno acquisto": anno_acquisto,
                "valore" : valore
            }
        return self.deposito.append(aggiunta)

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.deposito, key=lambda x: x["marca"])

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        prestito = False
        for oggetto in self.deposito:
            if oggetto["codice"] == id_strumento:
                if id_strumento not in self.lista_id:
                    oggetto_prestato = {}
                    oggetto_prestato["id_prestito"] = f"P{len(self.lista_prestiti) + 1}"
                    oggetto_prestato["id_strumento"] = id_strumento
                    oggetto_prestato["tipo"] = oggetto["tipo"]
                    oggetto_prestato["cognome"] = cognome_allievo
                    oggetto_prestato["inizio_prestito"] = data
                    self.lista_id.append(id_strumento)
                    self.lista_prestiti.append(oggetto_prestato)
                    prestito = True
                    return oggetto_prestato["tipo"]
                else:
                    raise Exception("Questo strumento è già in prestito")
        if prestito == False:
            raise Exception("Questo strumento non è presente nell'inventario")

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for oggetto in self.lista_prestiti:
            if oggetto["id_prestito"] == id_prestito:
                self.lista_prestiti.remove(oggetto)
                self.lista_id.remove(oggetto["id_strumento"])

    def cambia_responsabile(self, responsabile_nuovo):
        self.responsabile = responsabile_nuovo
