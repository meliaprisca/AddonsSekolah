# -*- coding: utf-8 -*-
{
    'name': "Addons Sekolah",

    'summary': """
        addons_sekolah""",

    'description': """
        addons_sekolah
    """,

    'author': "Melia",
    'website': "https://github.com/meliaprisca",

    'category': 'uncategory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
            'base',
            # 'account'
            ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/mata_pelajaran.xml',
        'views/menu_item.xml',
        'views/jadwal.xml',
        'views/kelas.xml',
        'views/mata_pelajaran.xml',
        'views/siswa.xml',
        # 'wizard/account_discount_amount.xml',
        # 'views/keda_template.xml',
    ],
}
