{
    'name': 'Funcionários',
    'version': '15.0.0.0',
    'sumary': 'School Management System',
    'sequence': 1,
    'description': "Sistema para cadastro de funcionarios da rede institucional "
                   "Odoo v15",
    'website': 'https://www.google.com/',
    'category': 'School',
    'author': 'Thales Gregorio',
    'images': [],
    'depends': ['base', 'school'],
    'data': [
        'security/ir.model.access.csv',
        'views/func_view.xml',
        'views/func_extend_view.xml'
    ],
    'application': True
}