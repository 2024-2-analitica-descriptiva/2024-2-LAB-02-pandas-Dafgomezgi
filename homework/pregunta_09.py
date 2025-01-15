"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

tbl0=pd.read_csv("tbl0.tsv",sep="\t")

def pregunta_09():
    """
    Agregue el año como una columna al dataframe que contiene el archivo
    `tbl0.tsv`.

    Rta/
        c0 c1  c2          c3  year
    0    0  E   1  1999-02-28  1999
    1    1  A   2  1999-10-28  1999
    2    2  B   5  1998-05-02  1998
    ...
    36  36  B   8  1997-05-21  1997
    37  37  C   9  1997-07-22  1997
    38  38  E   1  1999-09-28  1999
    39  39  E   5  1998-01-26  1998

    """

    fechas = tbl0["c3"]
    fechas = fechas.map(
        lambda x: x.split("-")
    )
    tbl0["year"]= fechas.map(lambda x: x[0])
    return tbl0