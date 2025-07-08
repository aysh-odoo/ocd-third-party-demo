# -*- coding: utf-8 -*-
{
    'name': "custom_contact",

    'summary': "Custom module made for the OCD Demonstration",

    'description': """
In this module a custom field is added in the contact form view
    """,

    'author': "Alay Shah",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],
    'license': 'LGPL-3',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': ['banner.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

