{
    'name': 'School Inherit Views',
    'version': '15.0.0.0',
    'sumary': 'Criando diferentes views inherit teste',
    'sequence': 1,
    'description': "This is school management system software supported in "
                   "Odoo v15",
    'website': 'https://www.google.com/',
    'category': 'School',
    'author': 'Thales Gregorio',
    'images': [],
    'depends': ['base', 'school', 'school_student'],
    'data': [
        "views/student_extend.xml",
    ],
    'application': True,
}