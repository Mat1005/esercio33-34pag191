'''
In un laboratorio di analisi 

'''

Coda =[]
lung = int(input("Quanti pazienti sono in coda"))
for n in range(1, lung +1):
    paziente = input("inserire il nome del paziente")
    Coda.append(paziente)
primo_paziente = Coda[0]
print("Il primo paziente ad essere sottoposto all'esame è ",primo_paziente)