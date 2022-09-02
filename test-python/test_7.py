from data import data
"""
  7) realice una consulta al archivo data.py, muestre los items que no tienen colores
  y ordenelos por nombre
"""


def get_items_without_colors():
    items = data.get_items()
    items_without_colors = []

    for item in items:
        if item['colors'] == []:
            items_without_colors.append(item)
    items_without_colors.sort(key=lambda item: item['name'])
    return items_without_colors
