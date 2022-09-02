from data import data
from typing import List, Dict
"""
  3) ordenar los terceros que se tienen en el archivo data.py
  por nombre, para obtener el nombre correcto se debe tener en
  cuenta la siguiente validación:

  si el tercero tiene un (tradename != '') entonces se muestra este valor,
  en caso contrario se debe obtener concatenando los siguientes
  campos: (firstname, lastname, maidenname) en el orden dado
"""


def get_thirds_by_name() -> List[Dict]:
    thirds = data.get_thirds()
    thirds.sort(key=lambda third: third['tradename'] if third['tradename'] !=
                '' else third['firstname'] + third['lastname'] + third['maidenname'])
    return thirds
