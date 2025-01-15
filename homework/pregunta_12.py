"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

tbl2=pd.read_csv("tbl2.tsv",sep="\t")

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    tbl2["combinada"] = tbl2["c5a"] + ":" + tbl2["c5b"].astype(str)   #Tengo que hacer str a _cb5, o sino da error
    num_unicos = tbl2["c0"].unique()
    dicc = {"c0":[],"c5":[]}
    for x in sorted(num_unicos):
        valores = sorted(list(tbl2[tbl2["c0"] == x]["combinada"]))
        cadena_unida = ",".join(map(lambda y: str(y), valores))
        dicc["c0"].append(x)
        dicc["c5"].append(cadena_unida)
    nuevo_dt = pd.DataFrame(dicc)
    return nuevo_dt
