{
    'name': 'School information',
    'version': '1.0',
    'sequence': 10,
    'description': """
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your """,
    'category': 'school',
    'author': "Mehedi Hasan",
    'website': 'https://www.school.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school.xml',
        'report/sudent_template.xml',
        'report/school_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
