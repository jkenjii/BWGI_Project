
import datetime
def reconcile_accounts(lista1, lista2):
    resultado1 = []
    resultado2 = []
    usados = [False] * len(lista2)
    for t1 in lista1:
        melhor_indice = None
        melhor_data = None
        for i, t2 in enumerate(lista2):
            if usados[i]:
                continue
            data1 = datetime.datetime.strptime(t1[0], "%Y-%m-%d")
            data2 = datetime.datetime.strptime(t2[0], "%Y-%m-%d")
            dias = abs((data1 - data2).days)
            if dias <= 1 and t1[1:] == t2[1:]:
                if melhor_data is None or data2 < melhor_data:
                    melhor_data = data2
                    melhor_indice = i
        if melhor_indice is not None:
            usados[melhor_indice] = True
            resultado1.append(t1 + ["FOUND"])
        else:
            resultado1.append(t1 + ["MISSING"])
    for i, t2 in enumerate(lista2):
        status = "FOUND" if usados[i] else "MISSING"
        resultado2.append(t2 + [status])
    return resultado1, resultado2
