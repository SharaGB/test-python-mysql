from data import data
from typing import List, Dict
"""
  4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
"""


def sort_thirds() -> List[Dict]:
    thirds = data.get_thirds()
    thirds.sort(key=lambda third: third['identificationNumber'])
    return thirds
