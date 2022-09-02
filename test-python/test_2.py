from test_1 import get_companies_and_branches
from typing import List, Dict
"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales por su id, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""


def get_branches_by_id(id: int) -> Dict:
    companies = get_companies_and_branches()

    for company in companies:
        for branch in company['branches']:
            if branch['id'] == id:
                return branch
