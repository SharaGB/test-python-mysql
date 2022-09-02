
class Data:
    """ Data class """
    @staticmethod
    def get_companies():
        """ Get companies """
        companies = [
            {
                'id': 1,
                'name': 'Empresa Uno',
                'nit': '123456789',
                'dv': '1',
                'branches': [1, 3, 5]
            },
            {
                'id': 2,
                'name': 'Empresa Dos',
                'nit': '987654321',
                'dv': '2',
                'branches': [2]
            },
            {
                'id': 3,
                'name': 'Empresa Tres',
                'nit': '987654333',
                'dv': '3',
                'branches': [4]
            }
        ]
        return companies

    @staticmethod
    def get_branches():
        """ Get branches """
        branches = [
            {
                'id': 1,
                'name': 'Sucursal Uno',
                'address': 'Cll 123',
                'isMain': True
            },
            {
                'id': 2,
                'name': 'Sucursal Dos',
                'address': 'Cll 12 # 1-23',
                'isMain': True
            },
            {
                'id': 3,
                'name': 'Sucursal Tres',
                'address': 'Cll 1 # 11-23',
                'isMain': False
            },
            {
                'id': 4,
                'name': 'Sucursal Cuatro',
                'address': 'Cll 4 # 4-32',
                'isMain': True
            },
            {
                'id': 5,
                'name': 'Sucursal Cinco',
                'address': 'Cll 5 # 5-43',
                'isMain': False
            }
        ]
        return branches

    @staticmethod
    def get_thirds():
        """ Get thirds """
        thirds = [
            {
                "billAddress1": "CRA 8 69 76",
                "cellPhone": None,
                "cityName": "Ibague",
                "companyid": 1,
                "email": "prueba@test.com.co",
                "firstname": "GERMAN ALBERTO",
                "identificationDv": "8",
                "identificationNumber": "1111123",
                "lastname": "CHAVARRO",
                "maidenname": "RAMIREZ",
                "phone": "2136368",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CARRERA 59 NO 26 21",
                "cellPhone": None,
                "cityName": "Pasto",
                "companyid": 3,
                "email": "siifn@otra.co",
                "firstname": "",
                "identificationDv": "5",
                "identificationNumber": "8046924",
                "lastname": "",
                "maidenname": "",
                "phone": "3158000",
                "state": "ACTIVO",
                "tradename": "POLICIA NACIONAL DE COLOMBIA"
            },
            {
                "billAddress1": "CRA 8 NO 6 C 38",
                "cellPhone": None,
                "cityName": "Cucuta",
                "companyid": 2,
                "email": "",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "800168",
                "lastname": "",
                "maidenname": "",
                "phone": "542200",
                "state": "ACTIVO",
                "tradename": "DIAN"
            },
            {
                "billAddress1": "CRA 15 NO. 134 A 25 APTO 406 CONTADOR",
                "cellPhone": None,
                "cityName": "Sucre",
                "companyid": 1,
                "email": "",
                "firstname": "JORGE",
                "identificationDv": "6",
                "identificationNumber": "122693",
                "lastname": "RAMIREZ",
                "maidenname": "GASCA",
                "phone": "",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CRA 8 N 69-76",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "asrfs@no.com",
                "firstname": "MARIA ELCY",
                "identificationDv": "2",
                "identificationNumber": "26520933",
                "lastname": "RAMIREZ",
                "maidenname": "GASCA",
                "phone": "",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CRA 9 N 72-35",
                "cellPhone": None,
                "cityName": "Suarez",
                "companyid": 1,
                "email": "contabilidad@test.com.co",
                "firstname": "",
                "identificationDv": "1",
                "identificationNumber": "86250302",
                "lastname": "",
                "maidenname": "",
                "phone": "",
                "state": "ACTIVO",
                "tradename": "BANCO BBVA"
            },
            {
                "billAddress1": "CR 66 A N 43 18",
                "cellPhone": None,
                "cityName": "Cali",
                "companyid": 1,
                "email": "forpo@test.co",
                "firstname": "",
                "identificationDv": "0",
                "identificationNumber": "860020227",
                "lastname": "",
                "maidenname": "",
                "phone": "2209960",
                "state": "ACTIVO",
                "tradename": "FONDO ROTATORIO DE CASA"
            },
            {
                "billAddress1": "AV CLL 26 N 51 50 PISO 5",
                "cellPhone": None,
                "cityName": "Manizales",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "898969900",
                "lastname": "",
                "maidenname": "",
                "phone": "2236580",
                "state": "ACTIVO",
                "tradename": "MARISCOS DEL PACIFICO"
            },
            {
                "billAddress1": "CARRERA 8 NO. 8 - 55",
                "cellPhone": None,
                "cityName": "Tolima",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "5",
                "identificationNumber": "83085348",
                "lastname": "",
                "maidenname": "",
                "phone": "343100",
                "state": "ACTIVO",
                "tradename": "MINISTERIO DE CULTURA"
            },
            {
                "billAddress1": "CRA 8 NO 69 76",
                "cellPhone": None,
                "cityName": "Jamundí",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "3",
                "identificationNumber": "80365816",
                "lastname": "",
                "maidenname": "",
                "phone": "566980",
                "state": "ACTIVO",
                "tradename": "CONSEJO ESPACIAL"
            },
            {
                "billAddress1": "CARRERA 50 # 18-06",
                "cellPhone": None,
                "cityName": "Calarca",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "809888632",
                "lastname": "",
                "maidenname": "",
                "phone": "3325611",
                "state": "ACTIVO",
                "tradename": "LA CASA DEL PAN DE YUCA"
            },
            {
                "billAddress1": "CRA 8 NO 69 76",
                "cellPhone": None,
                "cityName": "Armenia",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "2",
                "identificationNumber": "86965100",
                "lastname": "",
                "maidenname": "",
                "phone": "34332560",
                "state": "ACTIVO",
                "tradename": "LA CASERONA"
            }
        ]
        return thirds

    @staticmethod
    def get_colors():
        """ Get colors """
        colors = [
            {
                "colorCode": "AMA",
                "colorName": "AMARILLO"
            },
            {
                "colorCode": "AZU",
                "colorName": "AZUL"
            },
            {
                "colorCode": "BLA",
                "colorName": "BLANCO"
            },
            {
                "colorCode": "CAR",
                "colorName": "CARMELITA"
            },
            {
                "colorCode": "FUS",
                "colorName": "FUSCIA"
            },
            {
                "colorCode": "NAR",
                "colorName": "NARANJA"
            },
            {
                "colorCode": "NEG",
                "colorName": "NEGRO"
            },
            {
                "colorCode": "PR",
                "colorName": "PUPURAL"
            },
            {
                "colorCode": "ROJ",
                "colorName": "ROJO"
            },
            {
                "colorCode": "ROS",
                "colorName": "ROSADO"
            },
            {
                "colorCode": "VER",
                "colorName": "VERDE"
            },
            {
                "colorCode": "VIO",
                "colorName": "VIOLETA"
            }
        ]
        return colors

    @staticmethod
    def get_items():
        """ Get items """
        items = [
            {
                'code': '001',
                'name': 'Celular',
                'color': 'BLA'
            },
            {
                'code': '002',
                'name': 'Camiseta',
                'color': 'NEG'
            },
            {
                'code': '003',
                'name': 'Lapíz',
                'color': 'NAR'
            },
            {
                'code': '004',
                'name': 'Lentes',
                'color': None
            },
            {
                'code': '005',
                'name': 'Zapatos',
                'color': 'ROS'
            },
            {
                'code': '006',
                'name': 'Vaso de cristal',
                'color': None
            },
            {
                'code': '007',
                'name': 'Portail HP',
                'color': 'ROJ'
            },
            {
                'code': '008',
                'name': 'Cuaderno',
                'color': None
            },
            {
                'code': '009',
                'name': 'Gorra',
                'color': 'VER'
            },
            {
                'code': '010',
                'name': 'Balón',
                'color': None
            }
        ]
        return items


data = Data()
