{
    'name': 'Inventário de TI',
    'version': '15.0.0.0',
    'sumary': 'Inventário de materiais da empresa',
    'sequence': 1,
    'description': "Sistema para checagem de equipamentos e hardwares "
                   "Odoo v15",
    'website': 'https://www.google.com/',
    'category': 'Equipamentos e Hardwares',
    'author': 'Thales Gregorio',
    'images': [],
    'depends': ['base', 'product', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_access_data.xml',
        'views/inv_view.xml',
        'views/product_view.xml',
        'views/estoque_view.xml'
    ],
    'application': True
}