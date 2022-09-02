from data import data
"""
  8) realice una consulta al archivo data.py, muestre los items que si tienen colores, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente
"""


def get_items_with_colors():
    items = data.get_items()
    items_with_colors = []

    for item in items:
        if item['colors'] != []:
            items_with_colors.append(item)
    items_with_colors.sort(key=lambda item: item['name'])
    return items_with_colors
