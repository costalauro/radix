import escadinha

def existeEscadinha(matriz):
    print(matriz)
    anterior = 0
    inutilizavel = False
    for j in range(len(matriz)):
        for i in range(len(matriz)):

            if j<11 and i<11 and matriz[j][i] != matriz[j + 1][i + 1] and matriz[j] != matriz[j+1]:
                if(j>1 and matriz[j][12] != matriz[j-1][0]):
                    inutilizavel = True
                elif matriz[j][i] == matriz[j][i-1]:
                    inutilizavel = False

            if j == len(matriz)-1 and matriz[j][i] == anterior:
                break
            elif j<len(matriz)-1 and i<11 and matriz[j][i]==matriz[j+1][i+1]:
                anterior = matriz[j][12]


    if inutilizavel==False:
        ordenarEscadinha(matriz)
    else:
        eraInutilizavel(inutilizavel)
        print('Não era escadinha =(')

def ordenarEscadinha(matriz):
    for i in range(len(matriz)):
        matriz[i] = sorted(matriz[i])
    print(matriz)

def eraInutilizavel(inutilizavel):
    if inutilizavel:
        print('Era inutilizavel')
#existeEscadinha(escadinha.matriz_correta)
existeEscadinha(escadinha.matrizNegativosEscadinha)

#Para	solucionar	o	problema,	entregue	um	código	que:
#1)	Verifica	se	há	escadinha,	dada	uma	matriz	como	os	exemplos	acima.
#2)	Se	houver	escadinha,	mapear	os	dados	corretamente,	retornando	a	matriz
#correta.
#3)	Se	não	houver	escadinha,	retorne	se	a	matriz	está	com	uma	formatação	que	pode
#ser	utilizada	(padrão	correto)	ou	se	corresponde	a	um	padrão	inutilizável.
#4)	Caso	fossem	possíveis	números	negativos	nos	valores	dos	meses	(não	no	total),	a
#sua	solução	ainda	seria	válida?	Caso	não,	como	seria	a	nova	solução?

#4 - Resposta - Sim