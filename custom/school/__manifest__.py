{
    'name': 'Escola',
    'version': '15.0.0.0',
    'sumary': 'School Management System',
    'sequence': 1,
    'description': "This is school management system software supported in "
                   "Odoo v15",
    'website': 'https://www.google.com/',
    'category': 'School',
    'author': 'Thales Gregorio',
    'images': [],
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/school_view.xml"
    ],
    'application': True
}
