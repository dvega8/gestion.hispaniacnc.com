{
    "name": "Custom Invoice",
    "version": "15",
    "license": "LGPL-3",
    "author": "Sidharth",
    "category": "Accounting/Accounting",
    "summary": '''
        This module git functionality to add pickings and display it on invoice.''',

    "depends": ['account', 'stock'],
    "data": [
        'reports/invoice.xml',
        'reports/invoice_with_del_qty.xml',
        'views/invoice_line_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
