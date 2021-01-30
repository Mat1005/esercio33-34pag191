'''
Le prenotazioni per la partecipazione a un convegno sono memorizzate
secondo l'ordine di arrivo, scrivi un programma che comprenda due funzionalità:
L'operazione per registrare i dati dei partecipanti;
l'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare
una lettera di conferma: si tratta dei nomi dell'elenco, 
eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco.
La funzione che produce l'elenco dei partecipanti ai quali è già stata inviata la lettera.
'''
Partecipanti = []
Lettera_inviata = []
Lettera_mancante = []
lunghezza  =  int(input( "Quanti partecipanti sono in coda" ))
for n in range(1, lunghezza + 1):
    partecipante = input("Inserire nome partecipante")
    età = int(input("Quanti anni ha?"))
    origine = input("Da dove viene?")
    lettera = input("Ha ricevuto la lettera?Scrivere Sì o No")
    Partecipante = {'nome': partecipante,
                    'età': età,
                    'origine': origine}
    Partecipanti.append(Partecipante)
    
    if lettera == "Sì":
        Lettera_inviata.append(partecipante)
    elif lettera == "No":
        Lettera_mancante.append(partecipante)
    else:
        print("Hai scritto male la risposta.")

print("Questo è l'elenco dei partecipanti con le loro generalità.")
print(Partecipanti)
print("Questo è l'elenco dei partecipanti a cui bisogna inviare la lettera di conferma.")
print(Lettera_mancante)
print("Questo è l'elenco dei partecipanti ai quali è già stata inviata la lettera.")
print(Lettera_inviata)