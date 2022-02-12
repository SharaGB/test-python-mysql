

class Data:
    
    @statictmethod
    def get_companies():
        
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
    
    @statictmethod
    def get_branches():
        
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
    
    @statictmethod
    def get_thirds():
        thirds = [
            {
                "billAddress1": "CRA 8 69 76",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "contabilidad@fernandoramirez.com.co",
                "firstname": "GERMAN ALBERTO",
                "identificationDv": "8",
                "identificationNumber": "12239199",
                "lastname": "CHAVARRO",
                "maidenname": "RAMIREZ",
                "phone": "2129368",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CARRERA 59 NO 26 21",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 3,
                "email": "siifnacion.facturaelectronica@minhacienda.gov.co",
                "firstname": "",
                "identificationDv": "5",
                "identificationNumber": "800141397",
                "lastname": "",
                "maidenname": "",
                "phone": "3159000",
                "state": "ACTIVO",
                "tradename": "POLICIA NACIONAL DE COLOMBIA"
            },
            {
                "billAddress1": "CRA 8 NO 6 C 38",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 2,
                "email": "",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "800197268",
                "lastname": "",
                "maidenname": "",
                "phone": "5462200",
                "state": "ACTIVO",
                "tradename": "DIAN"
            },
            {
                "billAddress1": "CRA 15 NO. 134 A 25 APTO 406 CONTADOR",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "JORGE",
                "identificationDv": "6",
                "identificationNumber": "12269043",
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
                "email": "melcyrg@yahoo.com",
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
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "contabilidad@fernandoramirez.com.co",
                "firstname": "",
                "identificationDv": "1",
                "identificationNumber": "860003020",
                "lastname": "",
                "maidenname": "",
                "phone": "",
                "state": "ACTIVO",
                "tradename": "BANCO BBVA"
            },
            {
                "billAddress1": "CR 66 A N 43 18",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "forpo@forpo.gov.co",
                "firstname": "",
                "identificationDv": "0",
                "identificationNumber": "860020227",
                "lastname": "",
                "maidenname": "",
                "phone": "2200460",
                "state": "ACTIVO",
                "tradename": "FONDO ROTATORIO DE LA POLICIA"
            },
            {
                "billAddress1": "AV CLL 26 N 51 50 PISO 5",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "899999040",
                "lastname": "",
                "maidenname": "",
                "phone": "2202880",
                "state": "ACTIVO",
                "tradename": "REGISTRADURIA NACIONAL DEL ESTADO CIVIL"
            },
            {
                "billAddress1": "CARRERA 8 NO. 8 - 55",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "5",
                "identificationNumber": "830034348",
                "lastname": "",
                "maidenname": "",
                "phone": "3424100",
                "state": "ACTIVO",
                "tradename": "MINISTERIO DE CULTURA"
            },
            {
                "billAddress1": "CRA 8 NO 69 76",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "3",
                "identificationNumber": "800093816",
                "lastname": "",
                "maidenname": "",
                "phone": "5658500",
                "state": "ACTIVO",
                "tradename": "CONSEJO SUPERIOR DE LA JUDICATURA"
            },
            {
                "billAddress1": "CARRERA 50 # 18-06",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "800130632",
                "lastname": "",
                "maidenname": "",
                "phone": "3150111",
                "state": "ACTIVO",
                "tradename": "EJERCITO NACIONAL DIRECCION DE INGENIEROS"
            },
            {
                "billAddress1": "CRA 8 NO 69 76",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "2",
                "identificationNumber": "860002400",
                "lastname": "",
                "maidenname": "",
                "phone": "3434140",
                "state": "ACTIVO",
                "tradename": "LA PREVISORA COMPAÑIA DE SEGUROS"
            },
            {
                "billAddress1": "CRA 8 NO 69 76",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "3",
                "identificationNumber": "805027261",
                "lastname": "",
                "maidenname": "",
                "phone": "485 17 17",
                "state": "ACTIVO",
                "tradename": "RED DE SALUD DEL CENTRO ESE"
            },
            {
                "billAddress1": "DIA 45 45 45",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 2,
                "email": "",
                "firstname": "",
                "identificationDv": "8",
                "identificationNumber": "900583457",
                "lastname": "",
                "maidenname": "",
                "phone": "2451477",
                "state": "ACTIVO",
                "tradename": "CREAVISUAL SAS"
            },
            {
                "billAddress1": "CL 66 N 10 62 OFC 404",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 2,
                "email": "",
                "firstname": "",
                "identificationDv": "3",
                "identificationNumber": "900635468",
                "lastname": "",
                "maidenname": "",
                "phone": "2129368",
                "state": "ACTIVO",
                "tradename": "CONSULTORIA JURIDICA CORPORATIVA"
            },
            {
                "billAddress1": "1",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "BIBIANA MARCELA",
                "identificationDv": "0",
                "identificationNumber": "26652172",
                "lastname": "GARZON",
                "maidenname": "LOPEZ",
                "phone": "",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CALLE 43 NO. 57 - 14",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "",
                "identificationDv": "7",
                "identificationNumber": "899999001",
                "lastname": "",
                "maidenname": "",
                "phone": "2222800",
                "state": "ACTIVO",
                "tradename": "MINISTERIO DE EDUCACION NACIONAL"
            },
            {
                "billAddress1": "CALLE 53 NO 3 06",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 3,
                "email": "",
                "firstname": "MARTHA VIVIANA",
                "identificationDv": "0",
                "identificationNumber": "53135860",
                "lastname": "MUÑOZ",
                "maidenname": "CRUZ",
                "phone": "3214116869",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CRA 22 B NO 56 63",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 1,
                "email": "",
                "firstname": "SOREL",
                "identificationDv": "3",
                "identificationNumber": "19422835",
                "lastname": "VELASQUEZ",
                "maidenname": "QUINTERO",
                "phone": "",
                "state": "ACTIVO",
                "tradename": ""
            },
            {
                "billAddress1": "CRA 65 N 11 83",
                "cellPhone": None,
                "cityName": "BOGOTA",
                "companyid": 2,
                "email": "contabilidad@fernandoramirez.com.co",
                "firstname": "",
                "identificationDv": "4",
                "identificationNumber": "899999284",
                "lastname": "",
                "maidenname": "",
                "phone": "",
                "state": "ACTIVO",
                "tradename": "FONDO NACIONAL DEL AHORRO"
            }
        ]
        return thirds
    
    @statictmethod
    def get_colors():
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
    
    @statictmethod
    def get_items():
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
    
    
