# -*- coding: utf-8 -*-
{
    'name': "Backend Programming",

    'summary': """
        Learning About Backend Programming - Views Odoo 9""",

    'description': """
        Backend Programming - Odoo 9, Views and api Decorators
    """,

    'author': "Learn Stuff",
    'website': "http://www.learnbeautifulstuff.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}