from test_1 import get_companies_and_branches
from test_3 import get_thirds_by_name
from typing import List, Dict
from data import data
"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""


def add_company_to_thirds() -> List[Dict]:
    thirds = get_thirds_by_name()
    companies = get_companies_and_branches()

    for third in thirds:
        for company in companies:
            for branch in company['branches']:
                if third['branchId'] == branch['id']:
                    third['company'] = company['name']

    return thirds
