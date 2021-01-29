'''
In un laboratorio di analisi i pazienti sono sottoposti ad un esame specialistico secondo l'ordine di arrivo.
Scrivi un programma che consenta di registrare i nomi dei pazienti mano a mano che arrivano.
Visualizza poi il nome del paziente che deve essere sottoposto all'esame
perchè è il primo della coda in attesa.

'''

Coda =[]
lunghezza = int(input("Quanti pazienti sono in coda"))
for n in range(1, lunghezza +1):
    paziente = input("inserire il nome del paziente")
    Coda.append(paziente)
primo_paziente = Coda[0]
print("Il primo paziente ad essere sottoposto all'esame è ",primo_paziente)
