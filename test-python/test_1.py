from data import data
from typing import List, Dict
"""
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro
  las sucursales que corresponden para cada empresa
"""


def get_companies_and_branches() -> List[Dict]:
    info: List[Dict] = data.get_companies()
    companies: List[Dict] = []

    for company in info:
        companies.append({
            'id': company['id'],
            'name': company['name'],
            'nit': company['nit'],
            'dv': company['dv'],
            'branches': company['branches']
        })

    branches: List[Dict] = data.get_branches()

    for company in companies:
        for branch in branches:
            if branch['id'] in company['branches']:
                company['branches'].remove(branch['id'])
                company['branches'].append(branch)

    companies.sort(key=lambda company: (
        company['name'], company['branches'][0]['id']))
    return companies
