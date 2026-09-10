{
    'name': "MM Timesheet",
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': "Registro de horas trabajadas por empleado",
    'description': """ """,
    'depends': ['hr'],
    'author': 'Matias Mendez',
    'data': [
        'security/ir.model.access.csv',
        'views/timesheet_time_views.xml',
        'views/timesheet_menus.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
