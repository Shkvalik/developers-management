# -*- coding: utf-8 -*-
{
    'name': "Developers Management",
    'description': """
       Module for Managing Developers
    """,
    'author': "Valentyn Kovalenko",
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'Management',
    'version': '16.0',
    'depends': ['base'],
    'assets': {
        'web.assets_backend': [
            '/developers-management/static/src/views/form/form_controller.js',
            '/developers-management/static/src/views/form/form_controller.xml',
        ]
    },
    'data': [
        'security/ir.model.access.csv',
        'views/company.xml',
        'views/developer.xml',
        'views/menu.xml',
    ],
    'test': [
        'tests/test_developers_management.py',
    ],
    'license': 'GPL-3',
}
