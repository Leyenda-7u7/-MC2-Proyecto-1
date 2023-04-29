import subprocess
import random
import os

def generargrafo(vertices,aristas,recorrido):

    texto = 'graph {\n'
    texto += '\tlayout = neato'
    for vertice in vertices:
        texto += f'\t{vertice}[shape="point", width=0.2, fontsize=25 xlabel="{vertice}"] \n'
    texto2 = texto
    if aristas != []:
        for arista in aristas:
            r = random.uniform(1,5)
            texto += f'\t{arista} [penwidth=3, len={r}]\n'
            aux = arista.split('--')
            rever = f'{aux[1]}--{aux[0]}'
            if arista in recorrido:
                texto2 += f'\t{arista} [penwidth=3, len={r}, color="red"]\n'
            elif rever in recorrido:
                texto2 += f'\t{arista} [penwidth=3, len={r}, color="red"]\n'
            else:
                texto2 += f'\t{arista} [penwidth=3, len={r}]\n'

    texto += '}'
    texto2 += '}'
    Destino = open('Grafo.dot', 'w', encoding='utf-8')
    Destino.write(texto)
    Destino.close()
    cmd_str = "dot -Tpng Grafo.dot -o  Grafo.png"
    subprocess.run(cmd_str, shell=True)
    Destino2 = open('Grafo2.dot', 'w', encoding='utf-8')
    Destino2.write(texto2)
    Destino2.close()
    cmd_str = "dot -Tpng Grafo2.dot -o  Grafo2.png"
    subprocess.run(cmd_str, shell=True)

def generarrecorrido(vertices,aristas):
    pass