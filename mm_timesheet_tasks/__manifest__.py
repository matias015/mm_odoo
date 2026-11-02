{
    'name': "MM Timesheet tasks",
    'version': '19.0.1.3.1',
    'category': 'Human Resources',
    'summary': "Registro de horas trabajadas por empleado en tareas",
    'description': """ """,
    'depends': ['mm_timesheet','project'],
    'author': 'Matias Mendez',
    'data': [
        'views/tasks.xml',
        'views/projects.xml',
        'views/time.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
