"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

tbl2 = pd.read_csv(r"files\input\tbl2.tsv", sep="\t")
tbl0 = pd.read_csv(r"files\input\tbl0.tsv", sep="\t")

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    suma_c5b = tbl2.groupby("c0")["c5b"].sum()
    nuevo_dt = pd.concat([tbl0, suma_c5b], axis=1)
    resultado = nuevo_dt.groupby("c1")["c5b"].sum()
    return resultado